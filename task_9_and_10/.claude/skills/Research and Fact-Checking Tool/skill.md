---

name: research_and_fact_checking
description: >
Use this skill when the user needs research, fact-checking, or validated
information from reliable sources. Claude should load this skill whenever
someone asks to verify a claim, compare sources, or perform structured
research.
version: 1.0
------------

# Research and Fact-Checking Tool — Reasoning Skill

## Purpose

This skill enables Claude to perform deep research, validate information, compare
sources, and provide fact‑checked responses.

## When to Activate

* User asks to verify a claim
* User asks for research on any topic
* User wants reliable sources
* User wants to check accuracy or misinformation

## Workflow

1. Interpret the research query.
2. Search across multiple reputable sources.
3. Extract key facts from results.
4. Compare sources for consistency.
5. Identify misinformation or contradictions.
6. Produce a fact‑checked, source-backed summary.

## Examples

### User:

"Is intermittent fasting scientifically proven to help with weight loss?"

### Claude:

* Detect research + verification request
* Load this skill
* Compare multiple studies and sources
* Output fact‑checked summary with sources

---
