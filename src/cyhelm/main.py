from enum import Enum

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field


class Framework(str, Enum):
    iso27001 = "ISO27001"
    nist_csf = "NIST-CSF"
    nesa = "UAE-NESA"
    cis = "CIS-v8"


class Mapping(BaseModel):
    source_framework: Framework
    source_control: str
    target_framework: Framework
    target_control: str
    relationship: str = Field(pattern="^(equivalent|partial|related)$")
    rationale: str
    confidence: float = Field(ge=0, le=1)


MAPPINGS = [
    Mapping(source_framework="ISO27001", source_control="A.5.9", target_framework="NIST-CSF",
            target_control="ID.AM-01", relationship="partial",
            rationale="Both require inventories of assets supporting organizational objectives.",
            confidence=0.91),
    Mapping(source_framework="ISO27001", source_control="A.5.15", target_framework="CIS-v8",
            target_control="6.1", relationship="related",
            rationale="Access-control policy supports an inventory of enterprise accounts.",
            confidence=0.82),
    Mapping(source_framework="UAE-NESA", source_control="T3.1.1", target_framework="ISO27001",
            target_control="A.8.20", relationship="related",
            rationale="Network security controls align at an objective level; implementation detail differs.",
            confidence=0.76),
]

app = FastAPI(title="CyHelm UAE Compliance Mapper", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/v1/mappings", response_model=list[Mapping])
def list_mappings(
    framework: Framework | None = None,
    control: str | None = Query(default=None, max_length=40),
) -> list[Mapping]:
    needle = control.casefold() if control else None
    return [
        item for item in MAPPINGS
        if (framework is None or framework in {item.source_framework, item.target_framework})
        and (needle is None or needle in item.source_control.casefold()
             or needle in item.target_control.casefold())
    ]


@app.get("/v1/mappings/{framework}/{control}", response_model=list[Mapping])
def control_crosswalk(framework: Framework, control: str) -> list[Mapping]:
    matches = [
        item for item in MAPPINGS
        if framework in {item.source_framework, item.target_framework}
        and control.casefold() in {item.source_control.casefold(), item.target_control.casefold()}
    ]
    if not matches:
        raise HTTPException(status_code=404, detail="No reviewed mapping found")
    return matches
