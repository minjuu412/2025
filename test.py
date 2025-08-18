#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
꿈 해석 & 오늘의 운세 (Python, tkinter)
-------------------------------------
- 꿈 내용을 입력하면 간단한 상징 사전 + 감정 키워드로 해석을 생성
- 이름+날짜+꿈 내용을 시드로 하루 동안 고정되는 운세(사랑/일·학업/건강/행운) 제공
- 기록 저장/불러오기/내보내기 지원 (dream_history.json)
- 외부 라이브러리 사용하지 않음 (표준 라이브러리만)

실행: python dream_fortune_kr.py
본 앱은 오락용입니다. 의학·심리 상담이 아닙니다.
"""

import json
import os
import random
import re
import sys
from datetime import date
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.scrolledtext import ScrolledText

APP_TITLE = "꿈 해석 & 오늘의 운세"
DATA_FILE = "dream_history.json"

# --- 상징 사전 (확장 가능) ---
SYMBOLS = {
    r"\b(날다|비행|하늘|flying|flight|soar)\b": "자유와 성취 욕구가 커지고 있어요. 새로운 시도를 응원합니다.",
    r"\b(물|바다|강|호수|비|water|river|sea|ocean|rain)\b": "감정의 흐름이 활발합니다. 정서적 정리와 휴식이 도움이 됩니다.",
    r"\b(아이|아기|baby|child)\b": "새로운 시작이나 아이디어의 탄생을 의미해요.",
    r"\b(나무|숲|tree|forest)\b": "성장과 회복을 상징합니다. 꾸준함이 결실로 이어질 거예요.",
    r"\b(돈|금|보석|money|coin|gold)\b": "자원과 기회의 확장을 예고합니다. 다만 지출 관리도 잊지 마세요.",
    r"\b(추락|떨어지다|fall|falling)\b": "통제감 상실의 불안을 시사합니다. 우선순위를 정리해보세요.",
    r"\b(쫓기다|추격|chase)\b": "미뤄둔 일이 마음을 압박 중일 수 있어요. 작은 단위로 지금 시작해 보세요.",
    r"\b(이빨|치아|teeth|tooth)\b": "자신감이나 표현에 대한 고민을 반영합니다. 솔직한 대화가 약입니다.",
    r"\b(시험|exam)\b": "평가에 대한 긴장감. 준비한 만큼 결과가 따라올 거예요.",
    r"\b(지각|late)\b": "일정 관리 신호. 알람과 루틴을 재정비해 보세요.",
}

POSITIVE_WORDS = {"행복", "기쁨", "웃", "축하", "성공", "빛", "clear", "bright", "win", "safe"}
NEGATIVE_WORDS = {"무섭", "두렵", "불안", "어둡", "슬픔", "눈물", "fail", "lost", "danger", "위험"}

TIPS = [
    "가벼운 스트레칭으로 몸을 풀어보세요.",
    "해야 할 일 3가지만 적고 시작해요.",
    "물을 충분히 마시고 짧은 산책을 하세요.",
    "공간을 정리하면 마음도 정리돼요.",
    "감사한 일 1가지를 기록해 보세요.",
]

FORTUNE_TEXT = {
    0: "차분히 정리하는 날. 작은 성과에 집중하세요.",
    1: "새로운 만남/아이디어에 행운이 있어요.",
    2: "도전이 필요한 날이지만 안전장치를 잊지 마세요.",
    3: "협업의 시너지. 도움을 요청해도 좋아요.",
    4: "휴식이 곧 생산성. 잠깐 멈춰 재충전하세요.",
}

CATEGORIES = ("사랑", "일·학업", "건강", "행운")

# --- 핵심 로직 ---

def simple_sentiment(text: str) -> float:
    t = text.lower()
    pos = sum(p in t for p in POSITIVE_WORDS)
    neg = sum(n in t for n in NEGATIVE_WORDS)
    if pos == 0 and neg == 0:
        return 0.0
    return (pos - neg) / max(1, pos + neg)


def interpret_dream(text: str) -> list:
    out = []
    for pattern, meaning in SYMBOLS.items():
        if re.search(pattern, text, re.IGNORECASE):
            out.append(meaning)
    s = simple_sentiment(text)
    if s > 0.2:
        out.append("전반적으로 긍정적인 정서가 느껴집니다. 이 흐름을 유지하세요.")
    elif s < -0.2:
        out.append("걱정이 큰 상태일 수 있어요. 할 수 있는 작은 행동부터 시작해요.")
    if not out:
        out.append("명확한 상징은 적지만, 최근의 감정과 일정을 돌아보면 힌트를 얻을 수 있어요.")
    return out


def daily_fortune(name: str, seed_text: str) -> dict:
    base = f"{date.today().isoformat()}::{name.strip()}::{seed_text.strip()}"
    rnd = random.Random(hash(base))
    result = {}
    for cat in CATEGORIES:
        score = rnd.randint(0, 4)  # 0..4
        result[cat] = {"score": score + 1, "text": FORTUNE_TEXT[score]}
    result["Tip"] = rnd.choice(TIPS)
    return result

# --- 저장/불러오기 ---

def load_history() -> list:
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_history(history: list) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

# --- UI ---
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("840x640")
        self.minsize(720, 560)
        self.history = load_history()

        # 상단: 이름
        top = tk.Frame(self)
        top.pack(fill=tk.X, padx=12, pady=8)
        tk.Label(top, text="이름(선택):").pack(side=tk.LEFT)
        self.name_var = tk.StringVar()
        tk.Entry(top, textvariable=self.name_var, width=24).pack(side=tk.LEFT, padx=8)

        # 꿈 입력
        tk.Label(self, text="꿈 내용을 입력하세요:").pack(anchor="w", padx=12)
        self.input_box = ScrolledText(self, height=10, wrap=tk.WORD)
        self.input_box.pack(fill=tk.BOTH, expand=False, padx=12, pady=6)

        # 버튼들
        btns = tk.Frame(self)
        btns.pack(fill=tk.X, padx=12, pady=4)
        tk.Button(btns, text="해석하기", command=self.on_analyze).pack(side=tk.LEFT)
        tk.Button(btns, text="입력 지우기", command=self.clear_input).pack(side=tk.LEFT, padx=6)
        tk.Button(btns, text="결과 내보내기", command=self.export_result).pack(side=tk.LEFT, padx=6)
        tk.Button(btns, text="기록 전체 삭제", command=self.delete_history).pack(side=tk.RIGHT)

        # 결과 출력
        tk.Label(self, text="꿈 해석 & 오늘의 운세:").pack(anchor="w", padx=12, pady=(8,0))
        self.output_box = ScrolledText(self, height=14, wrap=tk.WORD, state=tk.DISABLED)
        self.output_box.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)

        # 히스토리
        tk.Label(self, text="기록(더블클릭하면 불러오기):").pack(anchor="w", padx=12)
        self.listbox = tk.Listbox(self, height=6)
        self.listbox.pack(fill=tk.BOTH, expand=False, padx=12, pady=(0,12))
        self.listbox.bind("<Double-1>", self.on_history_load)
        self.refresh_history_list()

        self._last_result_text = ""

    # --- UI helpers ---
    def append_output(self, text: str):
        self.output_box.config(state=tk.NORMAL)
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, text)
        self.output_box.config(state=tk.DISABLED)

    def clear_input(self):
        self.input_box.delete("1.0", tk.END)
        self.append_output("")

    def export_result(self):
        if not self._last_result_text.strip():
            messagebox.showinfo("내보내기", "먼저 꿈을 해석해 주세요.")
            return
        fp = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("텍스트 파일", ".txt")],
            initialfile=f"dream_fortune_{date.today().isoformat()}.txt",
        )
        if fp:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(self._last_result_text)
            messagebox.showinfo("내보내기", "저장되었습니다.")

    def delete_history(self):
        if not self.history:
            messagebox.showinfo("기록", "삭제할 기록이 없습니다.")
            return
        if messagebox.askyesno("삭제", "모든 꿈 기록을 삭제할까요? 되돌릴 수 없습니다."):
            self.history = []
            save_history(self.history)
            self.refresh_history_list()
            messagebox.showinfo("삭제", "기록이 삭제되었습니다.")

    def refresh_history_list(self):
        self.listbox.delete(0, tk.END)
        # 최신 100개만 표시
        for item in reversed(self.history[-100:]):
            label = f"{item.get('date','')} - {item.get('name','(이름없음)')} - {item.get('preview','')}"
            self.listbox.insert(tk.END, label[:100])

    def on_history_load(self, _event=None):
        sel = self.listbox.curselection()
        if not sel:
            return
        # 리스트는 최신순 역순으로 넣었으므로 매핑 단순화
        idx_from_end = sel[0]
        idx = max(0, len(self.history) - 1 - idx_from_end)
        item = self.history[idx]
        self.input_box.delete("1.0", tk.END)
        self.input_box.insert(tk.END, item.get("dream", ""))
        self.name_var.set(item.get("name", ""))

    # --- 동작 ---
    def on_analyze(self):
        name = self.name_var.get().strip() or "(이름없음)"
        dream = self.input_box.get("1.0", tk.END).strip()
        if not dream:
            messagebox.showinfo("입력", "꿈 내용을 먼저 입력해 주세요.")
            return

        interps = interpret_dream(dream)
        fortune = daily_fortune(name, dream)

        lines = []
        lines.append(f"이름: {name}")
        lines.append(f"날짜: {date.today().isoformat()}")
        lines.append("")
        lines.append("꿈 해석:")
        for i, m in enumerate(interps, 1):
            lines.append(f"  {i}. {m}")
        lines.append("")
        lines.append("오늘의 운세:")
        for cat in CATEGORIES:
            info = fortune[cat]
            stars = "★" * info["score"] + "☆" * (5 - info["score"])  # 1~5
            lines.append(f"  {cat}: {stars} - {info['text']}")
        lines.append("")
        lines.append(f"Tip: {fortune['Tip']}")
        lines.append("\n— 본 앱은 오락용입니다 —")

        result = "\n".join(lines)
        self._last_result_text = result
        self.append_output(result)

        record = {
            "date": date.today().isoformat(),
            "name": name,
            "dream": dream,
            "preview": re.sub(r"\s+", " ", dream)[:30] + ("…" if len(dream) > 30 else ""),
        }
        self.history.append(record)
        save_history(self.history)
        self.refresh_history_list()


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

