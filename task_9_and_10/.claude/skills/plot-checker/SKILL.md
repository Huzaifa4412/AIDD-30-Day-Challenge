---
name: plot_consistency_checker
description: >
    Use this skill when the user wants to check for plot holes, inconsistencies,
    timeline issues, or logical gaps in a story or novel.
version: 1.0
---

# Plot Consistency Checker — Reasoning Skill

## Purpose

Teach Claude how to analyze a story's logic, pacing, and continuity.

## When to Activate

-   User asks "find inconsistencies"
-   User wants plot hole checking
-   User provides summary/chapters for review
-   User wants timeline validation

## Workflow

1. Identify story timeline.
2. Map character motivations and decisions.
3. Compare events against:
    - Logic
    - Continuity
    - Motivation consistency
    - World rules
4. Highlight any contradictions.
5. Suggest fixes with narrative reasoning.

## Example

### User:

"Here is my plot. Tell me if anything doesn’t make sense."

### Claude:

-   Load the skill
-   Analyze events
-   Return a list of inconsistency flags
