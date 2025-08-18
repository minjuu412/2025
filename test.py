import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

// Leaflet 기본 아이콘 경로 문제 해결
import iconUrl from "leaflet/dist/images/marker-icon.png";
import iconShadow from "leaflet/dist/images/marker-shadow.png";

const DefaultIcon = L.icon({
  iconUrl,
  shadowUrl: iconShadow,
  iconSize: [25, 41],
  iconAnchor: [12, 41],
});
L.Marker.prototype.options.icon = DefaultIcon;

export default function App() {
  const [missions, setMissions] = useState([
    { id: 1, text: "텀블러 사용하기", done: false },
    { id: 2, text: "대중교통 이용하기", done: false },
    { id: 3, text: "분리수거 인증하기", done: false },
  ]);

  const [score, setScore] = useState(0);

  const toggleMission = (id) => {
    setMissions((prev) =>
      prev.map((m) => {
        if (m.id === id) {
          if (!m.done) {
            setScore((prev) => prev + 1);
          } else {
            setScore((prev) => (prev > 0 ? prev - 1 : 0));
          }
          return { ...m, done: !m.done };
        }
        return m;
      })
    );
  };

  // 예시: 전 세계 실제 나무 심기 위치 데이터 (나중에 API 연동)
  const plantedTrees = [
    { id: "tree-1", lat: -3.4653, lng: -62.2159, country: "브라질 아마존" },
    { id: "tree-2", lat: 7.8731, lng: 80.7718, country: "스리랑카" },
    { id: "tree-3", lat: -1.2921, lng: 36.8219, country: "케냐" },
  ];

  // 커뮤니티 숲 (예시 팀 데이터)
  const [teams] = useState([
    { id: "team-1", name: "지구지킴이", score: 15 },
    { id: "team-2", name: "푸른하늘", score: 9 },
    { id: "team-3", name: "친환경러버스", score: 20 },
  ]);

  return (
    <div className="p-6 grid gap-6">
      <h1 className="text-2xl font-bold">🌱 함께 키우는 숲</h1>

      {/* 미션 카드 */}
      <Card>
        <CardContent className="p-4">
          <h2 className="text-xl mb-3">오늘의 친환경 챌린지</h2>
          <ul className="space-y-2">
            {missions.map((m) => (
              <li key={`mission-${m.id}`} className="flex items-center justify-between">
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

      {/* 커뮤니티 숲 */}
      <Card>
        <CardContent className="p-4">
          <h2 className="text-xl mb-2">커뮤니티 숲 🌲</h2>
          <ul className="space-y-2">
            {teams.map((team) => (
              <li key={team.id} className="flex items-center justify-between">
                <span>{team.name}</span>
                <span className="font-semibold">{team.score} 점</span>
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>

      {/* 전 세계 나무 지도 */}
      <Card>
        <CardContent className="p-4">
          <h2 className="text-xl mb-3">전 세계 나무 심기 현황</h2>
          <MapContainer center={[20, 0]} zoom={2} className="h-[300px] w-full">
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
