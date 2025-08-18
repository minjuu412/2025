# -------------------------------------------------
# This is a React app (JSX). Do NOT run with Python.
# Save this file as App.jsx (or App.tsx) and run in
# a React environment (e.g., Next.js, Vite, CRA).
# -------------------------------------------------

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function App() {
  const [points, setPoints] = useState(0);
  const [trees, setTrees] = useState(0);
  const [history, setHistory] = useState([]);

  const TREE_COST = 100;

  const earnPoints = (amount) => setPoints((prev) => prev + amount);

  const plantTree = () => {
    if (points < TREE_COST) return;
    setPoints((prev) => prev - TREE_COST);
    setTrees((prev) => prev + 1);
    setHistory((prev) => [
      { id: Date.now(), when: new Date().toISOString(), cost: TREE_COST },
      ...prev,
    ]);
  };

  const needed = Math.max(0, TREE_COST - points);

  return (
    <div className="p-6 grid gap-6">
      <h1 className="text-2xl font-bold">Point Forest</h1>

      <Card>
        <CardContent className="p-4">
          <h2 className="text-xl mb-2">My Status</h2>
          <p>Points: {points}</p>
          <p>Trees planted: {trees}</p>
        </CardContent>
      </Card>

      <Card>
        <CardContent className="p-4 space-y-2">
          <h2 className="text-xl mb-2">Earn Points</h2>
          <div className="flex gap-2 flex-wrap">
            <Button onClick={() => earnPoints(10)}>+10 (mission)</Button>
            <Button onClick={() => earnPoints(50)}>+50 (challenge)</Button>
            <Button onClick={() => earnPoints(100)}>+100 (sponsor)</Button>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardContent className="p-4">
          <h2 className="text-xl mb-2">Plant a Tree</h2>
          <div className="flex items-center gap-3">
            <Button onClick={plantTree} disabled={points < TREE_COST}>
              Plant with {TREE_COST} points
            </Button>
            {points < TREE_COST && (
              <span className="text-sm">Need {needed} more points</span>
            )}
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardContent className="p-4">
          <h2 className="text-xl mb-2">Planting History</h2>
          {history.length === 0 ? (
            <p>No trees planted yet.</p>
          ) : (
            <ul className="space-y-1">
              {history.map((h) => (
                <li key={h.id} className="text-sm">
                  {h.when} - planted 1 tree ({h.cost} points)
                </li>
              ))}
            </ul>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
