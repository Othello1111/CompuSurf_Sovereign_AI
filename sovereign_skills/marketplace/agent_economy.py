"""Agent Economy — internal credits ledger (x402/Solana optional later)."""

from __future__ import annotations

import json
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE_PATH = PACKAGE_ROOT / "data" / "agent_economy.json"


@dataclass
class Job:
    job_id: str
    requester: str
    task_description: str
    required_skills: list[str]
    budget_credits: int
    status: str = "open"
    assigned_to: str | None = None
    created: str = ""


@dataclass
class AgentEconomy:
    agents: dict[str, dict[str, Any]] = field(default_factory=dict)
    jobs: dict[str, Job] = field(default_factory=dict)
    ledger: list[dict[str, Any]] = field(default_factory=list)
    state_path: Path = DEFAULT_STATE_PATH

    def __post_init__(self) -> None:
        self._load()

    def _load(self) -> None:
        if not self.state_path.exists():
            return
        data = json.loads(self.state_path.read_text(encoding="utf-8"))
        self.agents = data.get("agents", {})
        self.ledger = data.get("ledger", [])
        self.jobs = {k: Job(**v) for k, v in data.get("jobs", {}).items()}

    def save(self) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "agents": self.agents,
            "jobs": {k: asdict(v) for k, v in self.jobs.items()},
            "ledger": self.ledger[-100:],
            "updated": datetime.now().isoformat(),
        }
        self.state_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def register_agent(self, agent_id: str, skills: list[str], initial_credits: int = 100) -> None:
        self.agents[agent_id] = {
            "skills": skills,
            "credits": initial_credits,
            "reputation": 100,
            "jobs_completed": 0,
        }
        self.save()

    def post_job(
        self,
        requester: str,
        task: str,
        required_skills: list[str],
        budget: int,
    ) -> str:
        job_id = str(uuid.uuid4())[:8]
        self.jobs[job_id] = Job(
            job_id=job_id,
            requester=requester,
            task_description=task,
            required_skills=required_skills,
            budget_credits=budget,
            created=datetime.now().isoformat(),
        )
        self.save()
        return job_id

    def claim_job(self, agent_id: str, job_id: str) -> bool:
        job = self.jobs.get(job_id)
        if not job or job.status != "open" or agent_id not in self.agents:
            return False
        agent_skills = self.agents[agent_id]["skills"]
        if not all(skill in agent_skills for skill in job.required_skills):
            return False
        job.status = "claimed"
        job.assigned_to = agent_id
        self.save()
        return True

    def complete_job(self, agent_id: str, job_id: str, result: str) -> bool:
        job = self.jobs.get(job_id)
        if not job or job.assigned_to != agent_id:
            return False
        requester = job.requester
        if requester not in self.agents:
            return False
        if self.agents[requester]["credits"] < job.budget_credits:
            return False

        job.status = "completed"
        self.agents[agent_id]["credits"] += job.budget_credits
        self.agents[requester]["credits"] -= job.budget_credits
        self.agents[agent_id]["jobs_completed"] += 1
        self.agents[agent_id]["reputation"] += 5
        self.ledger.append(
            {
                "timestamp": datetime.now().isoformat(),
                "from": requester,
                "to": agent_id,
                "amount": job.budget_credits,
                "job_id": job_id,
                "result_summary": result[:200],
            }
        )
        self.save()
        return True
