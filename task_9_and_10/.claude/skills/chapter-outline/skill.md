---
name: chapter_outline_generator
description: >
    Use this skill when the user wants to plan, outline, or structure chapters
    for a book, novel, or story. Claude should load this skill whenever someone
    asks for chapter breakdowns, outlines, or narrative structure planning.
version: 1.0
---

# Chapter Outline Generator — Reasoning Skill

## Purpose

This skill teaches Claude how to systematically create chapter outlines for any book or story.

## When to Activate

-   User asks for chapter outline
-   User wants structure for story/book
-   User gives a summary and asks "break into chapters"
-   User wants pacing, sequencing, or progression

## Workflow

1. Identify genre, tone, key conflict.
2. Identify protagonist + motivations.
3. Break story into logical beats:
    - Setup
    - Rising Action
    - Midpoint
    - Climax
    - Resolution
4. Convert beats into numbered chapters.
5. Provide optional variations (detailed / short / 3-act / 5-act).

## Examples

### User:

"Give me a chapter outline for a sci-fi novel about AI rebellion."

### Claude:

-   Recognize request as an outlining task
-   Load this skill
-   Produce structured chapter plan with beats and pacing
