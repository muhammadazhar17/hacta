# Implementation Plan: RAG Chatbot for Physical AI Humanoid Robotics Textbook

**Branch**: `1-rag-chatbot-humanoid-ai` | **Date**: 2025-12-07 | **Spec**: [link to spec.md](spec.md)
**Input**: Feature specification from `/specs/1-rag-chatbot-humanoid-ai/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Develop a complete RAG (Retrieval-Augmented Generation) chatbot system for the Physical AI & Humanoid Robotics textbook. The system will include three main components: an ingestion pipeline (main.py) to extract content from the textbook's sitemap.xml, embed it using Cohere, and store in Qdrant; a retrieval test script (retrieve.py) to verify the search functionality; and a live RAG chatbot agent (agent.py) using the agents library with Gemini 1.5 Flash via OpenAI proxy.

## Technical Context

**Language/Version**: Python 3.13
**Primary Dependencies**: agents, cohere, qdrant-client, trafilatura, python-dotenv, uv
**Storage**: Qdrant Cloud vector database with "humanoid_ai_book" collection
**Testing**: pytest for unit tests, manual verification for integration
**Target Platform**: Linux/Mac/Windows server environment
**Project Type**: Web backend service with embedded chatbot
**Performance Goals**: Query response time under 5 seconds for 95% of requests
**Constraints**: Must use Cohere embed-english-v3.0 (1024 dimensions), COSINE distance, chunk size ~1200 chars
**Scale/Scope**: Support up to 10 concurrent users, handle textbook content size

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

No constitutional violations detected.

## Project Structure

### Documentation (this feature)

```text
specs/1-rag-chatbot-humanoid-ai/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── main.py          # Ingestion pipeline
│   ├── retrieve.py      # Standalone retrieval test
│   └── agent.py         # Live RAG chatbot agent
├── pyproject.toml
├── .env                 # Environment variables (gitignored)
├── .env.example         # Example environment variables
└── README.md
```

**Structure Decision**: Selected single project structure with three main components in the backend directory.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |