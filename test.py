#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dream Interpreter & Daily Fortune
---------------------------------
A standalone Python app (tkinter) that:
  • Lets a user type a dream
  • Generates an interpretation based on simple symbolic rules
  • Provides a deterministic “daily fortune” (love/work/health/luck) seeded by
    the user's name + today's date so it is stable for the day
  • Saves dream history to a local JSON file

No external libraries required. Run with:  python dream_fortune.py

Note: This is for entertainment only and not psychological advice.
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

APP_TITLE = "Dream Interpreter & Daily Fortune"
DATA_FILE = "dream_history.json"

# --- Simple symbolic dictionary (extend as you like) ---
SYMBOLS = {
    # positive themes
    r"\b(flying|flight|soar|날다|비행|하늘)\b": "자유와 성취 욕구가 커지고 있어요. 새로운 시도를 응원합니다.",
    r"\b(water|river|sea|ocean|rain|물|바다|강|호수|비)\b": "감정의 흐름이 활발합니다. 정서적 정리와 휴식이 도움이 됩니다.",
    r"\b(baby|child|아이|아기)\b": "새로운 시작이나 아이디어의 탄생을 의미해요.",
    r"\b(tree|forest|나무|숲)\b": "성장과 회복을 상징합니다. 꾸준함이 큰 결실로 이어질 수 있어요.",
    r"\b(money|coin|gold|돈|금|보석)\b": "자원과 기회의 확장을 예고합니다. 다만 지출 관리도 함께 하세요.",
    # challenge themes
    r"\b(fall|falling|추락|떨어지다)\b": "통제감 상실의 불안을 시사합니다. 우선순위를 정리해보세요.",
    r"\b(chase|쫓기다|추격)\b": "미뤄둔 일이 마음을 압박 중일 수 있어요. 작은 단위로 당장 시작해 보세요.",
    r"\b(teeth|tooth|이빨|치아)\b": "자신감이나 표현에 대한 고민을 반영합니다. 솔직한 대화가 약이 됩니다.",
    r"\b(exam|시험)\b": "평가에 대한 긴장감. 준비한 만큼 결과가 따라올 거예요.",
    r"\b(late|지각)\b": "일정 관리 신호. 알람과 루틴을 재정비해 보세요.",
}

POSITIVE_WORDS = {
    "행복", "기쁨", "웃", "축하", "성공", "빛", "clear", "bright", "win", "safe",
}
NEGATIVE_WORDS = {
    "무섭", "두렵", "불안", "어둡", "슬픔", "눈물", "fail", "lost", "danger", "위험",
}

TIPS = [
    "가벼운 스트레칭으로 몸을 풀어보세요.",
    "해야 할 일 3가지만 적고 시작해요.",
    "물을 충분히 마시고 짧은 산책을 하세요.",
    "방을 정리하면 마음도 정리돼요.",
    "감사한 일 1가지를 기록해 보세요.",
]

FORTUNE_TEXT = {
    0: "오늘은 차분히 정리하는 날. 작은 성과에 집중하세요.",
    1: "새로운 만남/아이디어에 행운이 있어요.",
    2: "도전이 필요한 날! 하지만 안전 장치를 잊지 마세요.",
    3: "협업의 시너지. 도움을 요청해도 좋아요.",
    4: "휴식이 곧 생산성. 잠깐 멈춰 재충전하세요.",
}

CATEGORIES = ("Love", "Work/Study", "Health", "Luck")

# --- Core logic ---

def simple_sentiment(text: str) -> float:
    """Return sentiment score in [-1, 1] using naive keyword counts."""
    t = text.lower()
    pos = sum(p in t for p in POSITIVE_WORDS)
    neg = sum(n in t for n in NEGATIVE_WORDS)
    if pos == 0 and neg == 0:
        return 0.0
    return (pos - neg) / max(1, pos + neg)


def interpret_dream(text: str) -> list:
    """Return list of matched interpretations based on SYMBOLS and sentiment."""
    interpretations = []
    for pattern, meaning in SYMBOLS.items():
        if re.search(pattern, text, re.IGNORECASE):
            interpretations.append(meaning)
    # sentiment layer
    s = simple_sentiment(text)
    if s > 0.2:
        interpretations.append("전반적으로 긍정적인 정서가 느껴집니다. 이 흐름을 유지하세요.")
    elif s < -0.2:
        interpretations.append("걱정이 큰 상태일 수 있어요. 할 수 있는 작은 행동부터 시작해요.")
    if not interpretations:
        interpretations.append("명확한 상징은 적지만, 최근의 감정과 일정을 돌아보면 힌트를 얻을 수 있어요.")
    return interpretations


def daily_fortune(name: str, seed_text: str) -> dict:
    """Deterministic daily fortune seeded by date+name+dream."""
    base = f"{date.today().isoformat()}::{name.strip()}::{seed_text.strip()}"
    rnd = random.Random(hash(base))
    result = {}
    for cat in CATEGORIES:
        score = rnd.randint(0, 4)
        result[cat] = {
            "score": score + 1,  # 1..5
            "text": FORTUNE_TEXT[score],
        }
    result["Tip"] = rnd.choice(TIPS)
    return result


# --- Persistence ---

def load_history() -> list:
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_history(history: list) -> None:
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        messagebox.showerror("Save Error", str(e))


# --- UI ---
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("820x620")
        self.minsize(720, 560)
        self.history = load_history()

        # Top: name
        top = tk.Frame(self)
        top.pack(fill=tk.X, padx=12, pady=8)
        tk.Label(top, text="Name (optional):").pack(side=tk.LEFT)
        self.name_var = tk.StringVar()
        tk.Entry(top, textvariable=self.name_var, width=24).pack(side=tk.LEFT, padx=8)

        # Dream input
        tk.Label(self, text="Your Dream (paste/type here):").pack(anchor="w", padx=12)
        self.input_box = ScrolledText(self, height=10, wrap=tk.WORD)
        self.input_box.pack(fill=tk.BOTH, expand=False, padx=12, pady=6)

        # Buttons
        btns = tk.Frame(self)
        btns.pack(fill=tk.X, padx=12, pady=4)
        tk.Button(btns, text="Analyze", command=self.on_analyze).pack(side=tk.LEFT)
        tk.Button(btns, text="Clear", command=self.clear_input).pack(side=tk.LEFT, padx=6)
        tk.Button(btns, text="Export Result", command=self.export_result).pack(side=tk.LEFT, padx=6)
        tk.Button(btns, text="Delete History", command=self.delete_history).pack(side=tk.RIGHT)

        # Output
        tk.Label(self, text="Interpretation & Today's Fortune:").pack(anchor="w", padx=12, pady=(8,0))
        self.output_box = ScrolledText(self, height=14, wrap=tk.WORD, state=tk.DISABLED)
        self.output_box.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)

        # History list
        tk.Label(self, text="History (double-click to load):").pack(anchor="w", padx=12)
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
            messagebox.showinfo("Export", "Nothing to export yet.")
            return
        fp = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", ".txt")],
            initialfile=f"dream_fortune_{date.today().isoformat()}.txt",
        )
        if fp:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(self._last_result_text)
            messagebox.showinfo("Export", f"Saved to {os.path.basename(fp)}")

    def delete_history(self):
        if not self.history:
            messagebox.showinfo("History", "No history to delete.")
            return
        if messagebox.askyesno("Delete", "Delete all history? This cannot be undone."):
            self.history = []
            save_history(self.history)
            self.refresh_history_list()
            messagebox.showinfo("Delete", "History deleted.")

    def refresh_history_list(self):
        self.listbox.delete(0, tk.END)
        for i, item in enumerate(reversed(self.history[-100:])):
            label = f"{item.get('date','')} - {item.get('name','(anon)')} - {item.get('preview','')}"
            self.listbox.insert(tk.END, label[:100])

    def on_history_load(self, _event=None):
        sel = self.listbox.curselection()
        if not sel:
            return
        index_from_end = sel[0]
        # We displayed reversed last 100 items; map back to original index
        idx = max(0, len(self.history) - 100) + (99 - index_from_end)
        idx = min(idx, len(self.history) - 1)
        item = self.history[idx]
        self.input_box.delete("1.0", tk.END)
        self.input_box.insert(tk.END, item.get("dream", ""))
        self.name_var.set(item.get("name", ""))

    # --- Core actions ---
    def on_analyze(self):
        name = self.name_var.get().strip() or "(anon)"
        dream = self.input_box.get("1.0", tk.END).strip()
        if not dream:
            messagebox.showinfo("Dream", "Please type your dream first.")
            return

        interps = interpret_dream(dream)
        fortune = daily_fortune(name, dream)

        lines = []
        lines.append(f"Name: {name}")
        lines.append(f"Date: {date.today().isoformat()}")
        lines.append("")
        lines.append("Interpretation:")
        for i, m in enumerate(interps, 1):
            lines.append(f"  {i}. {m}")
        lines.append("")
        lines.append("Today's Fortune:")
        for cat in CATEGORIES:
            info = fortune[cat]
            stars = "★" * info["score"] + "☆" * (5 - info["score"])  # uses unicode stars
            lines.append(f"  {cat}: {stars}  - {info['text']}")
        lines.append("")
        lines.append(f"Tip: {fortune['Tip']}")
        lines.append("\n— This app is for entertainment only —")

        result = "\n".join(lines)
        self._last_result_text = result
        self.append_output(result)

        # Save history
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
