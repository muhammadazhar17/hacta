# Implementation Tasks: RAG Chatbot for Physical AI Humanoid Robotics Textbook

**Feature**: RAG Chatbot for Physical AI Humanoid Robotics Textbook
**Branch**: `1-rag-chatbot-humanoid-ai`
**Generated**: 2025-12-07
**Input**: spec.md, plan.md, data-model.md, contracts/internal.md

## Task List

This is the FINAL and ONLY task list. Exactly 5 tasks. No phases. No US1/US2/US3. No polish phase. No tests. No extra tasks.

- [X] T001 Generate main.py — full one-time ingestion pipeline (sitemap.xml → trafilatura → ~1200 char chunks → Cohere embed-english-v3.0 → Qdrant upsert into collection "humanoid_ai_book") with progress prints exactly like the video
- [X] T002 Generate retrieve.py — standalone retrieval test script that embeds a query and prints top 5 retrieved chunks from Qdrant
- [X] T003 Generate agent.py — complete working RAG agent using the 'agents' library with Gemini 1.5 Flash via OpenAI-compatible proxy (AsyncOpenAI + OpenAIChatCompletionsModel), @function_tool retrieve, verbose stdout logging, and the exact system prompt from the video
- [X] T004 Generate .env.example — with clear placeholders: COHERE_API_KEY=key-here, QDRANT_URL=url-here, QDRANT_API_KEY=here-key, GEMINI_API_KEY=your-gemini-key-here
- [X] T005 Generate README.md — with exact step-by-step instructions assuming accounts already created: paste keys → uv venv → uv pip install agents cohere qdrant-client trafilatura python-dotenv requests → uv run main.py → uv run agent.py → ask "what is physical ai?" and see tool calling