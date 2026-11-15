# AgentHarness101: Engineering Controlled AI Coding Workflows

Welcome to **AgentHarness101**, a hands-on curriculum and project repository exploring **Harness Engineering** for autonomous AI coding agents.

---

## Repository Contents

| Lab / Module | Topic | Description | Link |
|---|---|---|---|
| **Lab 1** | **Install and Compare AI Coding Tools** | A controlled benchmark comparing **Anthropic Claude Code**, **OpenAI Codex CLI**, and **Google Gemini CLI** on an identical Express API codebase. Focuses on reasoning, safety, context discovery, and implementation planning. | [lab1/lab1.md](./lab1/lab1.md) |
| **Lab 2** | **Build Your First AI Coding Harness** | Building a modular AI coding harness in Python featuring context collection, structured planning, human approval, command safety sandboxing, multi-tier automated verification, and bounded self-healing retry loops. | [lab2/README.md](./lab2/README.md) & [lab2/lab2.md](./lab2/lab2.md) |
| **Lab 3** | **Build a Claude Code Project** | Deep dive into configuring Claude Code: root and directory-scoped `CLAUDE.md` rules, cross-session project memory, Pre/PostToolUse automation hooks, dangerous command blocking, and reusable skills (`/add-endpoint`, `/check-project`, `/review-changes`). | [lab3/lab3.md](./lab3/lab3.md) |
| **Lab 4** | **Production Workflow with Codex CLI** | Production engineering workflow using OpenAI Codex CLI: `config.toml`, root and nested `AGENTS.md` instructions, planning-first feature workflows, human approval gates, Git diff inspection, automated reviews, and defect injection testing. | [lab4/lab4.md](./lab4/lab4.md) |
| **Lab 5** | **Gemini CLI Development Workflow** | Configuring Google Gemini CLI: `.gemini/settings.json`, persistent `GEMINI.md` rules, repository memory (`/memory show`, `/memory refresh`), plan-first code generation, and prompt optimization. | [lab5/lab5.md](./lab5/lab5.md) |
| **Lab 6** | **Optimize Context for Large Projects** | Context Engineering deep dive: contrasting zero-context, partial-context, and compressed-context strategies, pre-execution file retrieval, and blast-radius minimization. | [lab6/lab6.md](./lab6/lab6.md) |
| **Lab 7** | **Engineer Better Coding Prompts** | Prompt Engineering fundamentals: adding context, negative constraints, and explicit acceptance criteria to eliminate agent hallucinations and runaway refactoring. | [lab7/lab7.md](./lab7/lab7.md) |
| **Lab 8** | **AI Tool Calling Workflow** | Exploring tool-calling mechanics: read-only discovery, terminal execution, code edits, test runners, and mandatory human approval gates against destructive commands. | [lab8/lab8.md](./lab8/lab8.md) |
| **Section 7** | **Shared Agent Architecture** | Architecture walkthrough mapping the shared components of modern coding agents, the Observe-Think-Plan-Execute-Verify loop, and cross-tool comparisons (Claude Code, Codex CLI, Gemini CLI). | [section 7/section 7.md](./section%207/section%207.md) |
| **Section 13** | **Multi-Agent Systems & Collaboration** | Architectural walkthrough of Multi-Agent Systems: role specialization (Planner, Dev, Tester, Reviewer, Security, Docs), shared context, asynchronous message queues, parallel execution, workflow merging, and structured conflict resolution. | [section13/raw13.txt](./section13/raw13.txt) |

---

## Key Concepts Explored

```
+-----------------------------------------------------------------------------------------+
|                                    THE CORE PARADIGM                                    |
|                                                                                         |
|      Naked AI Model               AI Coding Harness             Production Engineering  |
|   (Prompt-Only / Chat)    ───►    (Outer Shell OS)     ───►    (Safe, Verified, Tested) |
|   • Probabilistic                 • Boundary Guards            • 100% Test Passing Rate |
|   • Hallucination-prone           • Automated Verifier         • Zero Runaway Edits     |
|   • Destructive shell risk        • Bounded Retry Loop         • Immutable Audit Trail  |
+-----------------------------------------------------------------------------------------+
```

1. **Control Plane vs. Data Plane Separation:**
   - **Control Plane:** Task intake, context gathering, structured planning, human approval gates, retry state machine, and JSONL telemetry.
   - **Data Plane:** Agent dispatch (Simulated / Claude / Codex / Gemini CLI), command safety filters, filesystem mutations, and multi-tier verification (pytest + AST checks).

2. **Objective Verification Over Self-Reporting:**
   - AI models should never self-validate their own solutions. Verification must be external and programmatic.

3. **Closed-Loop Self-Healing:**
   - Capturing execution failures and traceback logs, formatting them as diagnostic feedback, and prompting bounded retry cycles.

---

## Visual Architecture Diagrams

Interactive `.drawio` diagram files compatible with the VS Code Draw.io extension and [app.diagrams.net](https://app.diagrams.net):

- **[harness_architecture.drawio](./lab2/harness_architecture.drawio):** Full system architecture with Control Plane, Data Plane, Sandboxing, and Observability swimlanes.
- **[agent_harness_principles.drawio](./lab2/agent_harness_principles.drawio):** Theoretical principles of agent harness engineering mapped directly to the code components in this project.
- **[claude_code_harness_workflow.drawio](./lab3/claude_code_harness_workflow.drawio):** Claude Code runtime execution lifecycle and its direct alignment to Agent Harness Engineering principles (Context injection, Safety hooks, Invariants, SOP skills, and Verification).
- **[codex_cli_harness_workflow.drawio](./lab4/codex_cli_harness_workflow.drawio):** OpenAI Codex CLI production harness lifecycle and alignment matrix (Scoped `AGENTS.md`, `config.toml` sandboxing, planning-first human gates, defect injection, and review-only audit sessions).
- **[multi_agent_system_cooperation.drawio](./section13/multi_agent_system_cooperation.drawio):** Enterprise multi-agent collaboration architecture and workflow lifecycle (Role specialization, Shared Context Bus, Parallel execution tier, Workflow merging, Conflict resolution engine, and Continuous stage gates).
