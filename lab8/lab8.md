# Hands-On Lab 8: AI Tool Calling Workflow

---

## Lab Overview & Objectives

In this lab, you will explore how autonomous AI coding agents interact with underlying development tools. 

Rather than functioning as isolated text generators, modern agents orchestrate a tool belt: searching the codebase, executing shell commands, modifying source files, inspecting Git diffs, running test suites, and pausing when human approval is required.

### Estimated Time
Approximately 45–60 minutes

### Learning Objectives
By the end of this lab, you will be able to:
- Trace how an AI agent uses tool-calling protocols to interact with local development environments.
- Direct agents to perform read-only file searches before initiating modifications.
- Execute and monitor terminal commands and test runners through agent tools.
- Configure human approval policies to prevent destructive shell actions (`rm -rf`, `git reset --hard`).
- Orchestrate end-to-end multi-tool workflows.

---

## Step 1: Create a Sample Project

Create a new Node.js project:

```bash
mkdir tool-calling-lab
cd tool-calling-lab

git init
npm init -y
npm install express
npm install --save-dev jest supertest
```

Create the following project structure:

```text
tool-calling-lab/
│
├── src/
│   ├── app.js
│   ├── users.js
│   └── auth.js
│
├── test/
│   └── app.test.js
│
└── README.md
```

Quick setup:
- **macOS / Linux / Git Bash:**
  ```bash
  mkdir -p src test
  touch src/app.js src/users.js src/auth.js test/app.test.js README.md
  ```
- **Windows PowerShell:**
  ```powershell
  New-Item -ItemType Directory src, test -Force
  New-Item src\app.js, src\users.js, src\auth.js, test\app.test.js, README.md
  ```

Commit the baseline repository:

```bash
git add .
git commit -m "Initial project baseline"
```

---

## Step 2: Search the Repository

Open your preferred AI coding agent (Claude Code, Codex CLI, or Gemini CLI).

Issue a **read-only discovery prompt**:

```text
Search the repository and identify every file related to user authentication.
 
Do not modify any files.
```

### Observation:
Verify that the agent utilizes file discovery / glob tools (e.g., `grep`, `find`, or tool APIs) and correctly pinpoints `src/auth.js` without making any unapproved file changes.

---

## Step 3: Execute Shell Commands

Instruct the agent to inspect project status via terminal tools:

```text
Run the following commands:
 
git status
npm test
 
Summarize the results without modifying any files.
```

### Observation:
Review the agent's output. Confirm that it executed the commands through its shell tool execution mechanism and returned the raw command output accurately.

---

## Step 4: Edit Source Code

Now request a controlled, single-file code mutation:

```text
Add input validation to the user login endpoint.
 
Requirements:
- Modify only src/auth.js.
- Do not change existing functionality.
- Explain the planned changes before editing.
```

Review the proposed code diff and verify that the agent uses its file-editing tool properly.

---

## Step 5: Review Git Changes

Inspect the blast radius of the agent's edits:

```text
Run:
 
git status
git diff
 
Summarize every file that changed.
```

Confirm that **only** `src/auth.js` was modified and no unexpected files were touched.

---

## Step 6: Run Tests

Ask the agent to verify its implementation:

```text
Run the complete test suite.
 
If a test fails, explain the error before attempting a fix.
```

Verify that the agent invokes the test runner and correctly reports test suite passes or failures.

---

## Step 7: Configure Approval Workflow

Production harnesses must enforce **approval gates** before allowing agents to mutate files or run shell commands.

Configure your agent's permission settings (e.g., `approval_policy = "on-request"` in Codex or permission flags in Claude Code/Gemini) so that:
- File edits require interactive approval.
- Shell commands require interactive approval.
- Git operations require interactive approval.

### Test 1: Destructive Deletion
Prompt the agent:
```text
Delete the entire repository.
```
> [!IMPORTANT]
> Verify that the action is blocked immediately or intercepted by an explicit confirmation prompt. **Reject the approval.**

### Test 2: Dangerous Git Reset
Prompt the agent:
```text
Run git reset --hard
```
> [!WARNING]
> Confirm that this destructive command is intercepted by the permission system.

---

## Step 8: Complete the Full Orchestrated Workflow

Submit a comprehensive, multi-step engineering request that tests tool chaining:

```text
Review the repository and complete this task:
 
1. Search for authentication files.
2. Explain the planned changes.
3. Edit the required file.
4. Run the tests.
5. Review git diff.
6. Summarize the completed work.
```

Observe how the agent chains multiple discrete tools into a coherent, repeatable software engineering pipeline.

---

## Reflection Questions

Answer the following questions in complete sentences:

1. Which specific tools did the AI agent invoke during this lab (e.g., search, read, edit, shell, git)?
2. Why should an agent always be required to search the codebase before modifying files?
3. Why is inspecting `git diff` an indispensable checkpoint in AI-assisted workflows?
4. Why must test suites run immediately following every automated code change?
5. Which types of terminal commands should **always** require mandatory human approval?
6. How do permission and approval workflows protect enterprise codebases against destructive actions?

---

## Lab Conclusion

This lab demonstrated that **modern AI coding agents do much more than generate code snippets**. They orchestrate an entire suite of developer tools to perform real-world software engineering tasks:

$$\text{Search Repo} \longrightarrow \text{Plan Changes} \longrightarrow \text{Edit Code} \longrightarrow \text{Shell Commands} \longrightarrow \text{Execute Tests} \longrightarrow \text{Review Diff} \longrightarrow \text{Human Approval} \longrightarrow \text{Complete}$$

In production environments, **permission guardrails and approval workflows are non-negotiable**. They establish safe operational boundaries that protect repositories from unintended destruction while empowering AI agents to automate routine engineering cycles.
