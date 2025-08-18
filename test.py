import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function App() {
  const [points, setPoints] = useState(0);
  const [trees, setTrees] = useState(0);

  // 포인트 추가 (예: 미션 완료)
  const earnPoints = (amount) => {
    setPoints((prev) => prev + amount);
  };

  // 일정 포인트로 나무 심기 (예: 100포인트 = 1그루)
  const plantTree = () => {
    if (points >= 100) {
      setPoints((prev) => prev - 100);
      setTrees((prev) => prev + 1);
      alert("🎉 나무 1그루가 심어졌습니다!");
    } else {
      alert("포인트가 부족합니다. 100포인트가 필요해요.");
    }
  };

  return (
    <div className="p-6 grid gap-6">
      <h1 className="text-2xl font-bold">🌱 포인트 숲</h1>

      {/* 현재 상태 */}
      <Card>
        <CardContent className="p-4">
          <h2 className="text-xl mb-2">내 현황</h2>
          <p>현재 포인트: {points} 점</p>
          <p>내가 심은 나무: {trees} 그루</p>
        </CardContent>
      </Card>

      {/* 포인트 적립 버튼 */}
      <Card>
        <CardContent className="p-4 space-y-2">
          <h2 className="text-xl mb-2">포인트 적립</h2>
          <Button onClick={() => earnPoints(10)}>+10점 (미션 완료)</Button>
          <Button onClick={() => earnPoints(50)}>+50점 (특별 챌린지)</Button>
        </CardContent>
      </Card>

      {/* 나무 심기 */}
      <Card>
        <CardContent className="p-4">
          <h2 className="text-xl mb-2">나무 심기</h2>
          <Button onClick={plantTree} disabled={points < 100}>
            🌳 100포인트로 나무 심기
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}
