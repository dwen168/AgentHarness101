# AgentHarness101: Engineering Controlled AI Coding Workflows

Welcome to **AgentHarness101**, a hands-on curriculum and project repository exploring **Harness Engineering** for autonomous AI coding agents.

---

## Repository Contents

| Lab / Module | Topic | Description | Link |
|---|---|---|---|
| **Lab 1** | **Install and Compare AI Coding Tools** | A controlled benchmark comparing **Anthropic Claude Code**, **OpenAI Codex CLI**, and **Google Gemini CLI** on an identical Express API codebase. Focuses on reasoning, safety, context discovery, and implementation planning. | [lab1/lab1.md](./lab1/lab1.md) |
| **Lab 2** | **Build Your First AI Coding Harness** | Building a modular AI coding harness in Python featuring context collection, structured planning, human approval, command safety sandboxing, multi-tier automated verification, and bounded self-healing retry loops. | [lab2/README.md](./lab2/README.md) & [lab2/lab2.md](./lab2/lab2.md) |

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

The `lab2/` directory includes interactive `.drawio` diagram files compatible with the VS Code Draw.io extension and [app.diagrams.net](https://app.diagrams.net):

- **[harness_architecture.drawio](./lab2/harness_architecture.drawio):** Full system architecture with Control Plane, Data Plane, Sandboxing, and Observability swimlanes.
- **[agent_harness_principles.drawio](./lab2/agent_harness_principles.drawio):** Theoretical principles of agent harness engineering mapped directly to the code components in this project.
