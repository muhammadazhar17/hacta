---
id: 0002
title: RAG Chatbot Implementation Plan
stage: plan
date: 2025-12-07
surface: agent
model: unspecified
feature: 1-rag-chatbot-humanoid-ai
branch: 1-rag-chatbot-humanoid-ai
user: unknown
command: /sp.plan
labels: ["rag", "chatbot", "implementation", "plan", "qdrant", "cohere", "gemini"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-rag-chatbot-humanoid-ai/plan.md
 - specs/1-rag-chatbot-humanoid-ai/research.md
 - specs/1-rag-chatbot-humanoid-ai/data-model.md
 - specs/1-rag-chatbot-humanoid-ai/quickstart.md
 - specs/1-rag-chatbot-humanoid-ai/contracts/internal.md
 - QWEN.md
tests:
 - none
---

## Prompt

$ARGUMENTS

---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType qwen`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

---

/sp.plan Plan the exact 3-file project matching the video + user's final code:
File 1: main.py → One-time ingestion script
   • Extract all URLs from sitemap.xml
   • Download + clean text with trafilatura
   • Chunk text (~1200 chars)
   • Embed each chunk with Cohere embed-english-v3.0
   • Recreate Qdrant collection + upsert points with payload {url, text, chunk_id}
   • Print progress exactly like video ("Processing:", "Saved chunk X")

File 2: retrieve.py → Test retrieval
   • Simple script to embed query and search Qdrant
   • Print retrieved chunks

File 3: agent.py → Live RAG chatbot
   • Use agents library with Gemini 1.5 Flash via OpenAI proxy
   • Cohere + Qdrant clients
   • @function_tool retrieve() that returns list of text chunks
   • Agent instructions: "You are an AI tutor for the Physical AI & Humanoid Robotics textbook. First call retrieve tool. ONLY use retrieved content. If not found → I don't know."
   • Enable verbose logging to see tool calling
   • Test query: "what is physical ai?"

Use uv for everything, .env for keys, assume all API keys accounts are already created.

## Response snapshot

Successfully completed the implementation planning for the RAG chatbot system, creating all required planning artifacts including plan.md, research.md, data-model.md, quickstart.md, contracts, and updating the agent context.

## Outcome

- ✅ Impact: Created comprehensive implementation plan for RAG chatbot with 3-file architecture
- 🧪 Tests: none
- 📁 Files: specs/1-rag-chatbot-humanoid-ai/plan.md, specs/1-rag-chatbot-humanoid-ai/research.md, specs/1-rag-chatbot-humanoid-ai/data-model.md, specs/1-rag-chatbot-humanoid-ai/quickstart.md, specs/1-rag-chatbot-humanoid-ai/contracts/internal.md, QWEN.md
- 🔁 Next prompts: Implementation of the 3-file RAG system as specified
- 🧠 Reflection: Following the structured planning approach ensures all technical decisions are documented and aligned with constitutional principles.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation phase