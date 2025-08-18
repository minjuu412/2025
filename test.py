import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

export default function App() {
  const [missions, setMissions] = useState([
    { id: 1, text: "텀블러 사용하기", done: false },
    { id: 2, text: "대중교통 이용하기", done: false },
    { id: 3, text: "분리수거 인증하기", done: false },
  ]);

  const [score, setScore] = useState(0);

  const toggleMission = (id) => {
    setMissions((prev) =>
      prev.map((m) =>
        m.id === id ? { ...m, done: !m.done } : m
      )
    );
    setScore((prev) => prev + 1);
  };

  // 예시: 전 세계 실제 나무 심기 위치 데이터 (나중에 API 연동)
  const plantedTrees = [
    { id: 1, lat: -3.4653, lng: -62.2159, country: "브라질 아마존" },
    { id: 2, lat: 7.8731, lng: 80.7718, country: "스리랑카" },
    { id: 3, lat: -1.2921, lng: 36.8219, country: "케냐" },
  ];

  return (
    <div className="p-6 grid gap-6">
      <h1 className="text-2xl font-bold">🌱 함께 키우는 숲</h1>

      {/* 미션 카드 */}
      <Card>
        <CardContent className="p-4">
          <h2 className="text-xl mb-3">오늘의 친환경 챌린지</h2>
          <ul className="space-y-2">
            {missions.map((m) => (
              <li key={m.id} className="flex items-center justify-between">
                <span className={m.done ? "line-through" : ""}>{m.text}</span>
                <Button onClick={() => toggleMission(m.id)} size="sm">
                  {m.done ? "완료됨" : "완료하기"}
                </Button>
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>

      {/* 개인 점수 */}
      <Card>
        <CardContent className="p-4">
          <h2 className="text-xl mb-2">내 숲 성장도 🌳</h2>
          <p>현재 포인트: {score} 점</p>
        </CardContent>
      </Card>

      {/* 전 세계 나무 지도 */}
      <Card>
        <CardContent className="p-4">
          <h2 className="text-xl mb-3">전 세계 나무 심기 현황</h2>
          <MapContainer center={[20, 0]} zoom={2} style={{ height: "300px", width: "100%" }}>
            <TileLayer
              attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {plantedTrees.map((tree) => (
              <Marker key={tree.id} position={[tree.lat, tree.lng]}>
                <Popup>🌳 {tree.country}</Popup>
              </Marker>
            ))}
          </MapContainer>
        </CardContent>
      </Card>
    </div>
  );
}

