---
id: 0004
title: RAG Chatbot Simplified Tasks
stage: tasks
date: 2025-12-07
surface: agent
model: unspecified
feature: 1-rag-chatbot-humanoid-ai
branch: 1-rag-chatbot-humanoid-ai
user: unknown
command: /sp.tasks
labels: ["rag", "chatbot", "tasks", "implementation", "qdrant", "cohere", "gemini"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-rag-chatbot-humanoid-ai/tasks.md
 - specs/1-rag-chatbot-humanoid-ai/plan.md
 - specs/1-rag-chatbot-humanoid-ai/spec.md
 - specs/1-rag-chatbot-humanoid-ai/data-model.md
 - specs/1-rag-chatbot-humanoid-ai/contracts/internal.md
tests:
 - none
---

## Prompt

$ARGUMENTS

---
description: Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

3. **Execute task generation workflow**:
   - Load plan.md and extract tech stack, libraries, project structure
   - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
   - If data-model.md exists: Extract entities and map to user stories
   - If contracts/ exists: Map endpoints to user stories
   - If research.md exists: Extract decisions for setup tasks
   - Generate tasks organized by user story (see Task Generation Rules below)
   - Generate dependency graph showing user story completion order
   - Create parallel execution examples per user story
   - Validate task completeness (each user story has all needed tasks, independently testable)

4. **Generate tasks.md**: Use `.specify.specify/templates/tasks-template.md` as structure, fill with:
   - Correct feature name from plan.md
   - Phase 1: Setup tasks (project initialization)
   - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story (in priority order from spec.md)
   - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
   - Final Phase: Polish & cross-cutting concerns
   - All tasks must follow the strict checklist format (see Task Generation Rules below)
   - Clear file paths for each task
   - Dependencies section showing story completion order
   - Parallel execution examples per story
   - Implementation strategy section (MVP first, incremental delivery)

5. **Report**: Output path to generated tasks.md and summary:
   - Total task count
   - Task count per user story
   - Parallel opportunities identified
   - Independent test criteria for each story
   - Suggested MVP scope (typically just User Story 1)
   - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

Context for task generation: FORCE OVERRIDE — Generate ONLY these 5 tasks. Ignore all user stories, phases, parallel markers, dependencies, and the official tasks-template.md rules. This is a minimal, video-exact, 3-file RAG chatbot project matching Subhan Khalid's YouTube video + user's final code. Output tasks.md with EXACTLY these 5 tasks in this order (strict checklist format, no extra text): - [ ] T001 Generate main.py — full one-time ingestion pipeline (sitemap.xml → trafilatura → ~1200 char chunks → Cohere embed-english-v3.0 → Qdrant upsert into collection "humanoid_ai_book") with progress prints exactly like the video - [ ] T002 Generate retrieve.py — standalone retrieval test script that embeds a query and prints top 5 retrieved chunks from Qdrant - [ ] T003 Generate agent.py — complete working RAG agent using the 'agents' library with Gemini 1.5 Flash via OpenAI-compatible proxy (AsyncOpenAI + OpenAIChatCompletionsModel), @function_tool retrieve, verbose stdout logging, and the exact system prompt from the video - [ ] T004 Generate .env.example — with clear placeholders: COHERE_API_KEY=key-here, QDRANT_URL=url-here, QDRANT_API_KEY=here-key, GEMINI_API_KEY=your-gemini-key-here - [ ] T005 Generate README.md — with exact step-by-step instructions assuming accounts already created: paste keys → uv venv → uv pip install agents cohere qdrant-client trafilatura python-dotenv requests → uv run main.py → uv run agent.py → ask "what is physical ai?" and see tool calling This is the FINAL and ONLY task list. Exactly 5 tasks. No phases. No US1/US2/US3. No polish phase. No tests. No extra tasks.

The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

## Task Generation Rules

**CRITICAL**: Tasks MUST be organized by user story to enable independent implementation and testing.

**Tests are OPTIONAL**: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach.

### Checklist Format (REQUIRED)

Every task MUST strictly follow this format:

```text
- [ ] [TaskID] [P?] [Story?] Description with file path
```

**Format Components**:

1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
2. **Task ID**: Sequential number (T001, T002, T003...) in execution order
3. **[P] marker**: Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)
4. **[Story] label**: REQUIRED for user story phase tasks only
   - Format: [US1], [US2], [US3], etc. (maps to user stories from spec.md)
   - Setup phase: NO story label
   - Foundational phase: NO story label  
   - User Story phases: MUST have story label
   - Polish phase: NO story label
5. **Description**: Clear action with exact file path

**Examples**:

- ✅ CORRECT: `- [ ] T001 Create project structure per implementation plan`
- ✅ CORRECT: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
- ✅ CORRECT: `- [ ] T012 [P] [US1] Create User model in src/models/user.py`
- ✅ CORRECT: `- [ ] T014 [US1] Implement UserService in src/services/user_service.py`
- ❌ WRONG: `- [ ] Create User model` (missing ID and Story label)
- ❌ WRONG: `T001 [US1] Create model` (missing checkbox)
- ❌ WRONG: `- [ ] [US1] Create User model` (missing Task ID)
- ❌ WRONG: `- [ ] T001 [US1] Create model` (missing file path)

### Task Organization

1. **From User Stories (spec.md)** - PRIMARY ORGANIZATION:
   - Each user story (P1, P2, P3...) gets its own phase
   - Map all related components to their story:
     - Models needed for that story
     - Services needed for that story
     - Endpoints/UI needed for that story
     - If tests requested: Tests specific to that story
   - Mark story dependencies (most stories should be independent)

2. **From Contracts**:
   - Map each contract/endpoint → to the user story it serves
   - If tests requested: Each contract → contract test task [P] before implementation in that story's phase

3. **From Data Model**:
   - Map each entity to the user story(ies) that need it
   - If entity serves multiple stories: Put in earliest story or Setup phase
   - Relationships → service layer tasks in appropriate story phase

4. **From Setup/Infrastructure**:
   - Shared infrastructure → Setup phase (Phase 1)
   - Foundational/blocking tasks → Foundational phase (Phase 2)
   - Story-specific setup → within that story's phase

### Phase Structure

- **Phase 1**: Setup (project initialization)
- **Phase 2**: Foundational (blocking prerequisites - MUST complete before user stories)
- **Phase 3+**: User Stories in priority order (P1, P2, P3...)
  - Within each story: Tests (if requested) → Models → Services → Endpoints → Integration
  - Each phase should be a complete, independently testable increment
- **Final Phase**: Polish & Cross-Cutting Concerns

## Response snapshot

Successfully updated tasks.md to the simplified 5-task list matching the YouTube video implementation.

## Outcome

- ✅ Impact: Created simplified task list with exactly 5 tasks for video-exact implementation
- 🧪 Tests: none
- 📁 Files: specs/1-rag-chatbot-humanoid-ai/tasks.md
- 🔁 Next prompts: Begin implementation of the 5 core tasks
- 🧠 Reflection: Task list now matches the minimal 3-file RAG chatbot project requirements.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Execute the first task to generate main.py