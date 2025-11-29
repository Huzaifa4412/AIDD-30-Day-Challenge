# Spec-Kit Plus

Spec-Kit Plus is an SDD-RI (Specification-Driven Development with Reusable Intelligence) framework designed to help you not only deliver working code but also capture and preserve the intelligence behind decisions and processes. This framework is built around the idea of creating two distinct outputs for every project:

- Working Code (ephemeral): The actual, working feature that provides value but may be rewritten or replaced in the future without any loss.
- Reusable Intelligence (permanent): The reasoning behind decisions, decision frameworks, and prompt structures that help improve future work and can be reused across different projects.
  
---

## Key Concepts and Components

### The Two-Output Philosophy

- Working Code: Specific to the current project and technology stack, can be discarded or replaced.
- Reusable Intelligence: Documentation of decision-making and prompts used, saved for future reference to accelerate learning in future projects.

---

### Framework Components

- Templates: Standardized documents to capture reasoning and structure thinking.
- Specifications: What you're building.
- Plans: How you're building it.
- ADRs (Architectural Decision Records): Why you chose a certain approach.
- PHRs (Prompt History Records): Which prompts worked and why.

- Slash Commands: AI orchestration tools to guide the workflow.

/sp.specify, /sp.clarify, /sp.plan, /sp.tasks, /sp.implement

Directory Structure:

specs/: Specifications for each feature.

history/adr/: ADRs that document your reasoning.

history/prompts/: PHRs that document which prompts were successful.

### Horizontal Intelligence

- As you complete projects, your knowledge accumulates. You document decisions (ADRs) and prompts that worked (PHRs). This compounding expertise makes you faster and more confident in future projects.

### Vertical Intelligence (Components You Create)

You create reusable components (skills, subagents, tools) after successful sessions to handle recurring problems more effectively.

These components can be:

- Skills: Structured prompts that guide reasoning.
- Subagents: Specialized agents that execute complex tasks autonomously.
- Tools/MCP Servers: Custom capabilities for connecting external systems.

### ADRs (Architectural Decision Records)

- ADRs document the "WHY" behind significant decisions (not just the "WHAT").

- Example of a bad ADR: “Used PostgreSQL for user data storage.”

- Example of a good ADR: “Chose PostgreSQL because it provides ACID guarantees, aligns with team expertise, and suits the needs of financial transactions.”

### PHRs (Prompt History Records)

- PHRs document AI collaboration: capturing what prompts worked and what failed.

- Example of a generic prompt: "Generate a database schema."

- Example of a specific prompt: "Generate PostgreSQL schema for financial transactions with indexes, constraints, and audit trail."

- The PHR helps track which prompts consistently work better, aiding in future sessions.

- Automatic Creation: PHRs are automatically generated during the phases /sp.specify, /sp.plan, and /sp.implement.

---

## 5 core concepts of  SPECKit

### /constitution

- A Constitution defines immutable standards applying to all work in a project. It's distinct from a Specification, which applies to one feature.
- Constitution is One-Time, Feature Work is Repetitive
- You write the Constitution once per project. Then, for each paper:

- Initialize project
- Write Constitution (quality standards for ALL papers)
- Commit Constitution to git
- FOR EACH PAPER:
  - Run /sp.specify (new specification for this paper)
  - Run /sp.clarify (refine specification)
  - Run /sp.plan (new plan for this paper)
  - Run /sp.tasks (new tasks for this paper)
  - Run /sp.implement (write paper with AI)
  - Commit paper to git

### /Specification

- In AI-native development, your ability to write a clear specification is more valuable than your ability to write code. Bad code can be refactored—but a bad spec breaks everything downstream.

- The Specify phase involves creating clear, testable requirements for the project to ensure a focused and measurable approach to implementation.

### /Plan

- This phase is where you design the architecture of the system, make technology choices, and document your rationale in Architectural Decision Records (ADRs). It also includes creating an implementation roadmap with steps and milestones.
- The Plan phase is about designing the system’s architecture and creating an implementation roadmap, supported by decisions documented in ADRs to guide the development process.
  
### /tasks

- The Tasks phase is where you break down the implementation into smaller, manageable tasks, assign them to subagents, and monitor their progress. It also includes creating a task list and assigning them to subagents.
- The Tasks phase is about breaking down the implementation into smaller, manageable tasks, assigning them to subagents, and monitoring their progress. It also includes creating a task list and assigning them to subagents.

### /implement

- This is the execution phase where the tasks identified in the previous step are implemented with the help of AI tools. You create working code and implement the solution, ensuring that it meets the defined specifications and quality standards.
- The Implement phase is about creating working code and implementing the solution, ensuring that it meets the defined specifications and quality standards.

---

## Screenshot of Spec-Kit Plus

![Screenshot](/task_7/img.png)