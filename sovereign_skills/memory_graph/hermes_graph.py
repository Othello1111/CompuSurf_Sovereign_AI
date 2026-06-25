"""HermesGraph — persistent local memory graph for agent context."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import networkx as nx
except ImportError:
    nx = None  # type: ignore

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GRAPH_PATH = PACKAGE_ROOT / "data" / "hermes_graph.json"


class HermesGraph:
    def __init__(self, graph_path: str | Path | None = None):
        if nx is None:
            raise ImportError("networkx required: pip install networkx")
        self.graph_path = Path(graph_path or DEFAULT_GRAPH_PATH).expanduser()
        self.G = nx.DiGraph()
        self._load_graph()

    def _load_graph(self) -> None:
        if self.graph_path.exists():
            data = json.loads(self.graph_path.read_text(encoding="utf-8"))
            self.G = nx.node_link_graph(data, directed=True)
        else:
            self.G = nx.DiGraph()

    def save(self) -> None:
        self.graph_path.parent.mkdir(parents=True, exist_ok=True)
        data = nx.node_link_data(self.G)
        self.graph_path.write_text(
            json.dumps(data, indent=2, default=str),
            encoding="utf-8",
        )

    def add_node(self, node_id: str, node_type: str, data: dict[str, Any]) -> None:
        self.G.add_node(
            node_id,
            type=node_type,
            **data,
            updated=datetime.now().isoformat(),
        )
        self.save()

    def add_edge(
        self,
        source: str,
        target: str,
        relation: str,
        weight: float = 1.0,
    ) -> None:
        self.G.add_edge(source, target, relation=relation, weight=weight)
        self.save()

    def seed_v2_baseline(self) -> None:
        """Idempotent seed for CompuSurf v2.0 + Forge context."""
        if self.G.number_of_nodes() > 0:
            return
        nodes = [
            (
                "project:compusurf_v2",
                "project",
                {"title": "CompuSurf Sovereign AI Mastery v2.0", "phase": "1"},
            ),
            (
                "project:forge_v06",
                "project",
                {"title": "Sovereign Forge Engine v0.6", "connectors": 21},
            ),
            (
                "project:family_guardian",
                "project",
                {"title": "Family Guardian Agent", "status": "MVP"},
            ),
            ("project:tradeshield", "project", {"title": "TradeShield", "status": "In Progress"}),
            (
                "decision:local_first",
                "decision",
                {"text": "Ollama local-first; Gemini/Claude hybrid fallback only"},
            ),
            (
                "decision:human_gate",
                "decision",
                {"text": "Human gate before public changes and file apply"},
            ),
            (
                "skill:sovereign_skills",
                "skill",
                {"text": "SovereignSkills + HermesGraph layer integrated"},
            ),
        ]
        for node_id, node_type, data in nodes:
            self.add_node(node_id, node_type, data)
        edges = [
            ("project:compusurf_v2", "project:forge_v06", "uses"),
            ("project:compusurf_v2", "project:family_guardian", "ships"),
            ("project:compusurf_v2", "project:tradeshield", "ships"),
            ("project:forge_v06", "skill:sovereign_skills", "extends"),
            ("decision:local_first", "project:forge_v06", "governs"),
            ("decision:human_gate", "project:compusurf_v2", "governs"),
        ]
        for src, tgt, rel in edges:
            self.add_edge(src, tgt, rel)

    def get_relevant_context(self, query: str, max_nodes: int = 15) -> str:
        query_lower = query.lower()
        relevant_nodes: list[str] = []

        for node, attrs in self.G.nodes(data=True):
            text = " ".join(str(v) for v in attrs.values()).lower()
            if any(word in text for word in query_lower.split() if len(word) > 3):
                relevant_nodes.append(node)

        if not relevant_nodes:
            return ""

        parts = ["\n=== HERMES GRAPH CONTEXT ==="]
        for node in relevant_nodes[:max_nodes]:
            attrs = dict(self.G.nodes[node])
            node_type = attrs.pop("type", "node")
            attrs.pop("updated", None)
            parts.append(f"\n[{str(node_type).upper()}] {node}")
            for key, value in attrs.items():
                parts.append(f"  {key}: {value}")
        return "\n".join(parts)

    def summary(self) -> dict[str, Any]:
        types: dict[str, int] = {}
        for _, attrs in self.G.nodes(data=True):
            t = attrs.get("type", "unknown")
            types[t] = types.get(t, 0) + 1
        return {
            "nodes": self.G.number_of_nodes(),
            "edges": self.G.number_of_edges(),
            "types": types,
            "path": str(self.graph_path),
        }
