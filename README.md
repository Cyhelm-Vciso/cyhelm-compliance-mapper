# CyHelm UAE Compliance Mapper

[![CI](https://github.com/Cyhelm-Vciso/cyhelm-compliance-mapper/actions/workflows/ci.yml/badge.svg)](https://github.com/Cyhelm-Vciso/cyhelm-compliance-mapper/actions)

An API-first, reviewer-controlled crosswalk between UAE and international cybersecurity frameworks. The MVP searches curated mappings and exposes the relationship, rationale, and confidence rather than presenting cross-framework equivalence as fact.

## MVP

- Typed mappings for ISO 27001:2022, NIST CSF, UAE NESA and CIS Controls v8
- Search by framework or control identifier
- Relationship labels (`equivalent`, `partial`, `related`) and reviewer confidence
- OpenAPI at `/docs`; sample mappings embedded for a zero-setup demo

## Quick start

```bash
docker compose up --build
curl "http://localhost:8000/v1/mappings?framework=ISO27001"
```

For local development:

```bash
python -m venv .venv
pip install -e ".[dev]"
uvicorn cyhelm.main:app --reload
pytest
```

## Architecture

`main.py` currently contains the HTTP contract and a tiny reviewed sample dataset. Production evolution should split this into API, domain, repository and import/adaptor layers, use PostgreSQL, preserve mapping provenance and review history, and require named reviewers before publication.

## Data and legal notice

The repository contains original summaries and identifiers only—not reproduced framework text. Obtain the applicable standards from their publishers and verify licensing before importing control text. Mappings are analytical aids, not proof of compliance or legal advice.

See [SECURITY.md](SECURITY.md) for disclosure and deployment guidance.
