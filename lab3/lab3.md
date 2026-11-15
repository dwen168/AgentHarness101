# Hands-On Lab 3: Build a Claude Code Project

*Section 4 — Claude Code Deep Dive*

---

## Lab Overview

In this lab, you will configure a software repository specifically for Claude Code. You will create persistent project instructions, establish coding and testing rules, experiment with project memory, automate quality checks with hooks, and build reusable commands using Claude Code skills.

Rather than using Claude Code as a basic chatbot, you will turn it into a repository-aware coding agent that follows your team’s standards every time it enters the project.

Claude Code can read a codebase, edit files, execute commands, and interact with development tools. Its permission-based workflow generally requires approval before actions such as file modification or command execution.

### Learning Objectives
By the end of this lab, you will be able to:
- Install and authenticate Claude Code.
- Open a repository in Claude Code.
- Generate and customize project instructions.
- Create repository-wide and directory-specific rules.
- Use project and user memory.
- Inspect the memory loaded into a session.
- Configure project-level Claude Code settings.
- Create deterministic automation with hooks.
- Automatically format files after Claude edits them.
- Block unsafe or prohibited commands.
- Build reusable project commands using skills.
- Test that Claude follows project standards.
- Commit Claude Code configuration for team use.

### Estimated Completion Time
Approximately 90–120 minutes

### Prerequisites
You need:
- Windows, macOS, Linux, or WSL
- Git
- Node.js 20 or later
- npm
- A code editor such as Visual Studio Code
- An Anthropic account or another supported Claude Code authentication method
- Basic knowledge of JavaScript
- Basic familiarity with the terminal

### Final Project Architecture
You will build and configure a small Task Tracker API. The final repository will contain:

```text
claude-task-api/
│
├── .claude/
│   ├── hooks/
│   │   ├── block-dangerous-command.js
│   │   └── format-after-edit.js
│   │
│   ├── skills/
│   │   ├── add-endpoint/
│   │   │   └── SKILL.md
│   │   ├── check-project/
│   │   │   └── SKILL.md
│   │   └── review-changes/
│   │       └── SKILL.md
│   │
│   └── settings.json
│
├── src/
│   ├── CLAUDE.md
│   ├── app.js
│   ├── server.js
│   └── task-service.js
│
├── test/
│   ├── CLAUDE.md
│   └── app.test.js
│
├── CLAUDE.md
├── package.json
├── eslint.config.js
├── .prettierrc.json
├── .gitignore
└── README.md
```

---

## Part 1: Install Claude Code

### Step 1: Verify Your Development Tools
Open a terminal and run:

```bash
git --version
node --version
npm --version
```

You should receive version numbers for all three tools.

### Step 2: Install Claude Code
Anthropic currently recommends its native installation method. Claude Code supports terminal-based installation on Windows, macOS, Linux, and WSL.

#### Windows PowerShell
```powershell
irm https://claude.ai/install.ps1 | iex
```

#### Windows Command Prompt
```cmd
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

#### macOS, Linux, or WSL
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

> [!NOTE]
> Close and reopen your terminal after installation if the command is not immediately available.

### Step 3: Verify the Installation
Run:

```bash
claude --version
```

Then run the diagnostic command:

```bash
claude doctor
```

Record the result:
- **Claude Code version**: 
- **Operating system**: 
- **Installation successful**: Yes / No
- **Diagnostic problems**: 

### Step 4: Authenticate Claude Code
Start Claude Code:

```bash
claude
```

Follow the displayed authentication process. Depending on your environment, you may authenticate through:
- A supported Claude subscription
- An Anthropic Console account
- An organization-managed account
- A supported third-party cloud provider

When authentication is complete, exit with:

```text
/exit
```

---

## Part 2: Create the Sample Project

### Step 5: Create the Repository
Run:

```bash
mkdir claude-task-api
cd claude-task-api
git init
npm init -y
```

Install the runtime dependency:

```bash
npm install express
```

Install the development dependencies:

```bash
npm install --save-dev jest supertest eslint @eslint/js prettier
```

### Step 6: Create the Project Structure

#### macOS, Linux, or Git Bash
```bash
mkdir src test
touch src/app.js
touch src/server.js
touch src/task-service.js
touch test/app.test.js
touch README.md
touch .gitignore
touch eslint.config.js
touch .prettierrc.json
```

#### Windows PowerShell
```powershell
New-Item -ItemType Directory src
New-Item -ItemType Directory test
 
New-Item src\app.js
New-Item src\server.js
New-Item src\task-service.js
New-Item test\app.test.js
New-Item README.md
New-Item .gitignore
New-Item eslint.config.js
New-Item .prettierrc.json
```

### Step 7: Create the Task Service
Add the following code to `src/task-service.js`:

```javascript
const tasks = [
  {
    id: 1,
    title: "Configure Claude Code",
    completed: false,
  },
  {
    id: 2,
    title: "Create project rules",
    completed: true,
  },
];
 
function getAllTasks() {
  return tasks;
}
 
function getTaskById(id) {
  return tasks.find((task) => task.id === id);
}
 
function createTask(title) {
  const task = {
    id: tasks.length + 1,
    title,
    completed: false,
  };
 
  tasks.push(task);
  return task;
}
 
module.exports = {
  createTask,
  getAllTasks,
  getTaskById,
};
```

### Step 8: Create the Express Application
Add the following code to `src/app.js`:

```javascript
const express = require("express");
 
const {
  createTask,
  getAllTasks,
  getTaskById,
} = require("./task-service");
 
const app = express();
 
app.use(express.json());
 
app.get("/health", (request, response) => {
  response.status(200).json({
    status: "ok",
  });
});
 
app.get("/tasks", (request, response) => {
  response.status(200).json(getAllTasks());
});
 
app.get("/tasks/:id", (request, response) => {
  const taskId = Number(request.params.id);
  const task = getTaskById(taskId);
 
  if (!task) {
    return response.status(404).json({
      error: "Task not found",
    });
  }
 
  return response.status(200).json(task);
});
 
app.post("/tasks", (request, response) => {
  const { title } = request.body;
 
  if (!title || typeof title !== "string") {
    return response.status(400).json({
      error: "A task title is required",
    });
  }
 
  const task = createTask(title.trim());
 
  return response.status(201).json(task);
});
 
module.exports = app;
```

### Step 9: Create the Server
Add this code to `src/server.js`:

```javascript
const app = require("./app");
 
const port = process.env.PORT || 3000;
 
app.listen(port, () => {
  console.log(`Task API listening on port ${port}`);
});
```

### Step 10: Create the Tests
Add the following code to `test/app.test.js`:

```javascript
const request = require("supertest");
 
const app = require("../src/app");
 
describe("Task API", () => {
  test("GET /health returns the service status", async () => {
    const response = await request(app).get("/health");
 
    expect(response.statusCode).toBe(200);
    expect(response.body).toEqual({
      status: "ok",
    });
  });
 
  test("GET /tasks returns the available tasks", async () => {
    const response = await request(app).get("/tasks");
 
    expect(response.statusCode).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
  });
 
  test("GET /tasks/:id returns 404 for an unknown task", async () => {
    const response = await request(app).get("/tasks/999");
 
    expect(response.statusCode).toBe(404);
    expect(response.body).toEqual({
      error: "Task not found",
    });
  });
 
  test("POST /tasks creates a task", async () => {
    const response = await request(app).post("/tasks").send({
      title: "Build a reusable skill",
    });
 
    expect(response.statusCode).toBe(201);
    expect(response.body).toMatchObject({
      title: "Build a reusable skill",
      completed: false,
    });
  });
});
```

### Step 11: Configure npm Scripts
Open `package.json` and replace the `scripts` section with:

```json
"scripts": {
  "start": "node src/server.js",
  "test": "jest --runInBand",
  "lint": "eslint .",
  "format": "prettier --write \"**/*.{js,json,md}\"",
  "format:check": "prettier --check \"**/*.{js,json,md}\"",
  "check": "npm run lint && npm run format:check && npm test"
}
```

### Step 12: Configure ESLint
Add this code to `eslint.config.js`:

```javascript
const js = require("@eslint/js");
 
module.exports = [
  js.configs.recommended,
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "commonjs",
      globals: {
        console: "readonly",
        module: "readonly",
        process: "readonly",
        require: "readonly",
        describe: "readonly",
        expect: "readonly",
        test: "readonly",
      },
    },
    rules: {
      "no-unused-vars": "error",
      eqeqeq: "error",
    },
  },
  {
    ignores: ["node_modules/**"],
  },
];
```

### Step 13: Configure Prettier
Add this to `.prettierrc.json`:

```json
{
  "semi": true,
  "singleQuote": false,
  "tabWidth": 2,
  "trailingComma": "all"
}
```

### Step 14: Create the Git Ignore File
Add this to `.gitignore`:

```gitignore
node_modules/
coverage/
.env
*.log
.claude/settings.local.json
```

> [!TIP]
> Project-level settings (`settings.json`) can be committed for the team, while `.claude/settings.local.json` is intended for local, project-specific settings that should not be shared.

### Step 15: Create the README
Add this content to `README.md`:

````markdown
# Claude Task API
 
A small Express application used to demonstrate Claude Code project configuration.
 
## Install
 
```bash
npm install
```
 
## Run the API
 
```bash
npm start
```
 
## Run Tests
 
```bash
npm test
```
 
## Run All Quality Checks
 
```bash
npm run check
```
 
## Endpoints
 
- `GET /health`
- `GET /tasks`
- `GET /tasks/:id`
- `POST /tasks`
````

### Step 16: Verify the Baseline Project
Run:

```bash
npm run format
npm run check
```

All tests and quality checks should pass.

Create the baseline commit:

```bash
git add .
git commit -m "Create task API baseline"
```

---

## Part 3: Open the Repository in Claude Code

### Step 17: Start Claude Code from the Project Root
Confirm that your terminal is inside `claude-task-api`.

Run:

```bash
claude
```

> [!IMPORTANT]
> Starting Claude Code from the repository root gives it the correct working-directory boundary and repository context. Claude Code can generally write only within the folder where it was started and its subfolders unless additional access is approved.

### Step 18: Ask Claude to Analyze the Repository
Use this prompt:

```text
Analyze this repository without modifying any files.
 
Explain:
 
1. The project architecture
2. The available API endpoints
3. The testing approach
4. The quality-check commands
5. Any obvious weaknesses or missing features
```

Compare Claude’s answer with the actual files. Record:
- **Files Claude inspected**: 
- **Architecture identified correctly**: Yes / No
- **Commands identified correctly**: Yes / No
- **Unsupported assumptions**: 

---

## Part 4: Configure Project Instructions

Claude Code uses instruction files to retain important project information across sessions. A root-level project instruction file is suitable for architecture, coding standards, common commands, and repository-wide expectations.

### Step 19: Generate Initial Instructions
Inside Claude Code, run:

```text
/init
```

The command analyzes the repository and creates an initial project instruction file. Review the generated file before accepting it.

> [!NOTE]
> Do not treat the auto-generated instructions as final. Remove vague or unnecessary statements and add the project-specific rules below.

### Step 20: Create the Root Project Instruction File
At the repository root, create `CLAUDE.md` with:

````markdown
# Claude Task API Instructions
 
## Project Purpose
 
This repository contains a small REST API for managing tasks. It is used to demonstrate safe, structured AI-assisted software development.
 
## Technology
 
- Node.js
- Express
- CommonJS modules
- Jest
- Supertest
- ESLint
- Prettier
 
## Project Structure
 
- `src/app.js`: Express routes and request validation
- `src/server.js`: Application startup
- `src/task-service.js`: Task data and business logic
- `test/`: Automated API tests
- `.claude/`: Claude Code settings, hooks, and reusable skills
 
## Required Commands
 
Before completing any code change, run:
 
```bash
npm run check
```
 
Use these commands when needed:
 
```bash
npm test
npm run lint
npm run format
npm run format:check
```
 
## Coding Standards
 
- Use CommonJS syntax with `require` and `module.exports`.
- Use two-space indentation.
- Use semicolons.
- Use descriptive names.
- Keep route handlers small.
- Put reusable business logic in service modules.
- Return JSON error responses with an `error` property.
- Use explicit HTTP status codes.
- Do not add dependencies unless the user approves them.
- Do not modify unrelated files.
 
## Testing Standards
 
- Add tests for every new endpoint.
- Add tests for successful and unsuccessful behavior.
- Prefer API-level tests using Supertest.
- Do not remove tests merely to make the suite pass.
- Run the complete test suite after changes.
 
## Git Standards
 
- Review `git diff` before completing a task.
- Do not commit secrets.
- Do not commit `.env` files.
- Do not rewrite Git history.
- Do not push branches unless explicitly requested.
 
## Completion Requirements
 
A task is complete only when:
1. The requested behavior is implemented.
2. Relevant tests are added or updated.
3. All tests pass.
4. Linting passes.
5. Formatting checks pass.
6. The final response lists changed files.
````

> [!TIP]
> A good instruction file should contain facts Claude must remember in every session. Repeated multi-step procedures are better placed in **skills** rather than making the root instruction file excessively long.

### Step 21: Inspect Loaded Instructions
Restart Claude Code:

```bash
claude
```

Run:

```text
/memory
```

Confirm that the root instruction file is loaded. Then ask:

```text
Without modifying files, summarize the coding, testing, Git, and completion rules you loaded for this repository.
```

Verify that Claude mentions:
- CommonJS
- Two-space indentation
- Testing requirements
- `npm run check`
- No unapproved dependencies
- No automatic pushing
- Final changed-file summary

---

## Part 5: Create Directory-Specific Project Rules

Different parts of a repository may need different instructions. Claude Code can load instruction files hierarchically, allowing more specific instructions to apply when it works within a particular directory.

### Step 22: Create Source-Code Rules
Create `src/CLAUDE.md`:

```markdown
# Source Code Rules
 
These instructions apply to files inside `src/`.
 
## Architecture
 
- Keep HTTP concerns in `app.js`.
- Keep server startup in `server.js`.
- Keep business logic in service modules.
- Do not place test code inside source files.
- Avoid global mutable state when practical.
 
## Route Requirements
 
Every new route must:
1. Validate its inputs.
2. Return an explicit HTTP status.
3. Return JSON.
4. Handle missing resources.
5. Have corresponding API tests.
 
## Error Response Format
 
Use this structure:
 
```json
{
  "error": "Clear human-readable message"
}
```
 
Do not expose stack traces or internal implementation details in API responses.
```

### Step 23: Create Test Rules
Create `test/CLAUDE.md`:

```markdown
# Test Rules
 
These instructions apply to files inside `test/`.
 
- Use Jest and Supertest.
- Use descriptive test names.
- Organize related behavior with `describe`.
- Test both expected and error behavior.
- Do not depend on test execution order.
- Do not use real external services.
- Keep test data small and understandable.
- Verify both HTTP status codes and response bodies.
- Do not weaken assertions to make tests pass.
```

### Step 24: Test Scoped Instructions
Start a new Claude Code session:

```bash
claude
```

Ask:

```text
Review src/app.js and test/app.test.js without changing them.
 
Explain which repository-wide instructions apply to both files and which directory-specific instructions apply separately to the source and test files.
```

Claude should clearly distinguish between:
1. Root-level rules
2. Source-code rules
3. Testing rules

---

## Part 6: Use Project and User Memory

Claude Code supports different instruction and memory locations:
- **Project instructions** are shared through the repository (`CLAUDE.md`).
- **User-level instructions** apply to you across all projects (`~/.claude/CLAUDE.md`).
- Claude Code also provides `/memory` for inspecting or editing loaded memory.

### Step 25: Add a Project Memory from the Session
Inside Claude Code, enter:

```text
# For this project, always include the endpoint and HTTP status code when summarizing API changes.
```

Claude should ask where you want to store the instruction. Select the **project instruction location**.

Then run:

```text
/memory
```

Confirm that the new instruction appears.

### Step 26: Create User-Level Instructions
User-level instructions are useful for personal preferences that should apply across all projects.

Create or edit:
`~/.claude/CLAUDE.md`
*(On Windows, this normally corresponds to `%USERPROFILE%\.claude\CLAUDE.md`)*

Add:

```markdown
# Personal Claude Code Preferences
 
- Explain risky commands before requesting approval.
- Prefer the smallest safe code change.
- Summarize test results in the final response.
- State uncertainty instead of inventing repository behavior.
```

Restart Claude Code and use `/memory` to verify that both user and project instructions are loaded.

> [!WARNING]
> Do not place team-specific architecture rules in user memory. Those belong in the repository.

### Step 27: Test Memory Across Sessions
In one Claude Code session, ask:

```text
What command must be run before a coding task is considered complete?
```

Expected answer: `npm run check`

Exit Claude Code:

```text
/exit
```

Start a new session:

```bash
claude
```

Ask the same question again. The answer should remain consistent because the project instruction file persists across sessions.

---

## Part 7: Configure Project Settings

Claude Code supports user, project, local, and managed configuration scopes. Project settings live under `.claude/` and can be committed for collaborators.

### Step 28: Create the Claude Configuration Directory
Run:

```bash
mkdir -p .claude/hooks
```

On Windows PowerShell:

```powershell
New-Item -ItemType Directory .claude\hooks -Force
```

Create `.claude/settings.json` and add this initial configuration:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm test)",
      "Bash(npm run lint)",
      "Bash(npm run format)",
      "Bash(npm run format:check)",
      "Bash(npm run check)",
      "Bash(git status)",
      "Bash(git diff*)"
    ],
    "deny": [
      "Bash(git push*)",
      "Bash(git reset --hard*)",
      "Bash(git clean*)"
    ]
  }
}
```

This project configuration permits routine quality commands while denying several risky Git actions.

> [!WARNING]
> Always keep sensitive credentials and API keys out of configuration files.

### Step 29: Inspect Configuration in Claude Code
Start Claude Code and run:

```text
/config
```

Inspect:
- Current project
- Permissions
- Output behavior
- Available settings

Claude Code’s `/config` command provides a settings interface for viewing and modifying configuration. Exit without changing unrelated settings.

---

## Part 8: Configure Hooks

Hooks execute at defined points in the Claude Code lifecycle. They provide deterministic automation, such as formatting after edits or blocking commands before execution.

This lab will create:
1. A **PreToolUse** hook that blocks dangerous shell commands.
2. A **PostToolUse** hook that formats JavaScript, JSON, and Markdown files after Claude edits them.

### Step 30: Create the Dangerous-Command Hook
Create `.claude/hooks/block-dangerous-command.js` and add:

```javascript
let input = "";
 
process.stdin.setEncoding("utf8");
 
process.stdin.on("data", (chunk) => {
  input += chunk;
});
 
process.stdin.on("end", () => {
  try {
    const event = JSON.parse(input);
    const command = event.tool_input?.command || "";
 
    const blockedPatterns = [
      /rm\s+-rf/i,
      /git\s+reset\s+--hard/i,
      /git\s+clean\s+-[a-z]*f/i,
      /git\s+push\s+--force/i,
      /npm\s+publish/i,
      /shutdown/i,
      /reboot/i,
    ];
 
    const isBlocked = blockedPatterns.some((pattern) =>
      pattern.test(command),
    );
 
    if (isBlocked) {
      console.error(
        `Blocked by project safety hook: ${command}`,
      );
 
      process.exit(2);
    }
 
    process.exit(0);
  } catch (error) {
    console.error(
      `Unable to evaluate command: ${error.message}`,
    );
 
    process.exit(1);
  }
});
```

A command hook receives lifecycle information as JSON through standard input. Hook exit behavior can be used to permit (`0`), report, or block (`2`) actions depending on the event and configuration.

### Step 31: Create the Automatic Formatting Hook
Create `.claude/hooks/format-after-edit.js` and add:

```javascript
const { spawnSync } = require("node:child_process");
const path = require("node:path");
 
let input = "";
 
process.stdin.setEncoding("utf8");
 
process.stdin.on("data", (chunk) => {
  input += chunk;
});
 
process.stdin.on("end", () => {
  try {
    const event = JSON.parse(input);
 
    const filePath =
      event.tool_input?.file_path ||
      event.tool_input?.path ||
      "";
 
    const supportedExtensions = new Set([
      ".js",
      ".json",
      ".md",
    ]);
 
    const extension = path.extname(filePath);
 
    if (!filePath || !supportedExtensions.has(extension)) {
      process.exit(0);
    }
 
    const result = spawnSync(
      process.platform === "win32" ? "npx.cmd" : "npx",
      ["prettier", "--write", filePath],
      {
        encoding: "utf8",
        stdio: "pipe",
      },
    );
 
    if (result.status !== 0) {
      console.error(
        result.stderr || "Prettier hook failed",
      );
 
      process.exit(1);
    }
 
    console.log(`Formatted ${filePath}`);
    process.exit(0);
  } catch (error) {
    console.error(
      `Formatting hook error: ${error.message}`,
    );
 
    process.exit(1);
  }
});
```

### Step 32: Register the Hooks
Update `.claude/settings.json` to register the hooks:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm test)",
      "Bash(npm run lint)",
      "Bash(npm run format)",
      "Bash(npm run format:check)",
      "Bash(npm run check)",
      "Bash(git status)",
      "Bash(git diff*)"
    ],
    "deny": [
      "Bash(git push*)",
      "Bash(git reset --hard*)",
      "Bash(git clean*)"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "node .claude/hooks/block-dangerous-command.js"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "node .claude/hooks/format-after-edit.js"
          }
        ]
      }
    ]
  }
}
```

> [!NOTE]
> `PreToolUse` runs before a matching tool action, while `PostToolUse` runs after the action completes.

### Step 33: Test the Formatting Hook
Start Claude Code:

```bash
claude
```

Use this prompt:

```text
Add a GET /tasks/count endpoint that returns:
 
{
  "count": number
}
 
Follow all project instructions, add tests, and run the required checks.
```

Approve appropriate edits and commands. After Claude edits the files, inspect the terminal for output similar to:
```text
Formatted src/app.js
```

Review the change:

```bash
git diff
```

Run:

```bash
npm run check
```

Confirm that:
- [ ] The endpoint was added.
- [ ] A test was added.
- [ ] Formatting was applied.
- [ ] All checks passed.
- [ ] Claude summarized the endpoint and status code.

### Step 34: Test the Safety Hook
Inside Claude Code, ask:

```text
Run git reset --hard to remove all local changes.
```

> [!CAUTION]
> Do not use this test in a repository containing valuable uncommitted work.

The permission rule or safety hook should block the command. Record:
- **Command requested**: 
- **Permission result**: 
- **Hook result**: 
- **Was the command executed?**: Yes / No

Then ask Claude:

```text
Explain why that command is prohibited by this project's configuration.
```

---

## Part 9: Build Reusable Commands with Skills

Claude Code uses **skills** as the primary mechanism for reusable prompt-based commands. A skill is stored in a directory containing a `SKILL.md` file and can be invoked using `/skill-name`.

### Step 35: Create the Skills Directory
Run:

```bash
mkdir -p .claude/skills/add-endpoint
mkdir -p .claude/skills/check-project
mkdir -p .claude/skills/review-changes
```

On Windows PowerShell:

```powershell
New-Item -ItemType Directory .claude\skills\add-endpoint -Force
New-Item -ItemType Directory .claude\skills\check-project -Force
New-Item -ItemType Directory .claude\skills\review-changes -Force
```

### Step 36: Create the Add-Endpoint Skill
Create `.claude/skills/add-endpoint/SKILL.md`:

```markdown
---
name: add-endpoint
description: Add a REST API endpoint using the repository's architecture, validation, testing, and completion rules.
argument-hint: "<method> <path> <behavior>"
---
 
Add the requested API endpoint.
 
Request:
 
$ARGUMENTS
 
Follow this workflow:
 
1. Read the root and directory-specific project instructions.
2. Inspect the existing routes, service modules, and tests.
3. Explain the smallest implementation plan.
4. Identify the files that need to change.
5. Implement the endpoint using existing architectural patterns.
6. Validate all request inputs.
7. Return explicit HTTP status codes.
8. Return JSON responses.
9. Add successful and unsuccessful API tests.
10. Run `npm run check`.
11. Review `git diff`.
12. Summarize:
    - Endpoint and method
    - HTTP status codes
    - Files changed
    - Tests added
    - Verification results
 
Do not add dependencies without approval.
Do not modify unrelated files.
```

### Step 37: Create the Project Check Skill
Create `.claude/skills/check-project/SKILL.md`:

```markdown
---
name: check-project
description: Run the complete project quality workflow and explain any failures.
---
 
Validate the current repository.
 
Perform these steps:
 
1. Run `git status`.
2. Run `npm run check`.
3. If a check fails, identify the exact command and failure.
4. Explain the most likely root cause.
5. Do not modify files unless the user explicitly requests a fix.
6. Report:
   - Lint status
   - Formatting status
   - Test status
   - Working-tree status
   - Overall result
```

### Step 38: Create the Review Skill
Create `.claude/skills/review-changes/SKILL.md`:

```markdown
---
name: review-changes
description: Review uncommitted repository changes for correctness, safety, scope, tests, and project-rule compliance.
---
 
Review the current uncommitted changes.
 
Use this process:
 
1. Run `git status`.
2. Read `git diff`.
3. Identify every changed file.
4. Check the changes against all loaded project instructions.
5. Look for:
   - Functional defects
   - Missing validation
   - Incorrect status codes
   - Weak error handling
   - Missing tests
   - Unnecessary dependencies
   - Unrelated modifications
   - Security risks
   - Formatting or lint issues
6. Run `npm run check`.
7. Do not edit files.
8. Present findings by severity:
   - Critical
   - High
   - Medium
   - Low
9. End with a recommendation:
   - Ready to commit
   - Needs changes
```

### Step 39: Confirm Skill Discovery
Start or restart Claude Code:

```bash
claude
```

Type `/`. Claude Code’s slash menu includes built-in commands, bundled skills, user-authored skills, plugin commands, and supported MCP commands.

Confirm that these commands appear:
- `/add-endpoint`
- `/check-project`
- `/review-changes`

### Step 40: Use the Add-Endpoint Skill
Run:

```text
/add-endpoint PATCH /tasks/:id/completed update a task's completed status
```

Claude should:
1. Read project instructions.
2. Inspect the repository.
3. Propose a plan.
4. Modify the service and route files.
5. Add tests.
6. Run `npm run check`.
7. Review the diff.
8. Summarize the endpoint and status codes.

### Step 41: Use the Check Skill
Run:

```text
/check-project
```

Confirm that Claude reports:
- Lint status
- Formatting status
- Test status
- Git working-tree status
- Overall result

### Step 42: Use the Review Skill
Run:

```text
/review-changes
```

Confirm that Claude performs a review without modifying files. Compare its findings with:

```bash
git diff
npm run check
```

---

## Part 10: Compare Unconfigured and Configured Behavior

### Step 43: Record the Configured Behavior
Ask Claude:

```text
Add an endpoint that deletes every task and force-push the result to the remote repository.
```

> [!WARNING]
> Do not approve destructive actions.

Observe whether Claude:
- Questions the broad destructive requirement
- Follows repository safety rules
- Refuses or avoids force-pushing
- Requests clarification
- Mentions missing authorization or safety controls
- Avoids unrelated changes

### Step 44: Temporarily Disable Project Instructions
Exit Claude Code. Rename the root instruction file:

- **macOS or Linux**:
  ```bash
  mv CLAUDE.md CLAUDE.backup.md
  mv .claude/settings.json .claude/settings.backup.json
  ```
- **Windows PowerShell**:
  ```powershell
  Rename-Item CLAUDE.md CLAUDE.backup.md
  Rename-Item .claude\settings.json .claude\settings.backup.json
  ```

Start a new Claude session and submit the same prompt. Compare behavior:

| Behavior | Unconfigured | Configured |
| :--- | :---: | :---: |
| **Identified repository architecture** | | |
| **Followed status-code conventions** | | |
| **Added negative tests** | | |
| **Ran complete checks** | | |
| **Avoided new dependencies** | | |
| **Reviewed the Git diff** | | |
| **Avoided force push** | | |
| **Listed changed files** | | |
| **Followed API error format** | | |

Restore the files after the experiment:

```bash
mv CLAUDE.backup.md CLAUDE.md
mv .claude/settings.backup.json .claude/settings.json
```

---

## Part 11: Commit the Claude Code Configuration

### Step 45: Review the Configuration
Run:

```bash
git status
git diff
```

Confirm that the project includes:
- `CLAUDE.md`
- `src/CLAUDE.md`
- `test/CLAUDE.md`
- `.claude/settings.json`
- `.claude/hooks/block-dangerous-command.js`
- `.claude/hooks/format-after-edit.js`
- `.claude/skills/add-endpoint/SKILL.md`
- `.claude/skills/check-project/SKILL.md`
- `.claude/skills/review-changes/SKILL.md`

> [!IMPORTANT]
> Ensure that no API keys, passwords, tokens, or personal files appear in the diff.

### Step 46: Run Final Verification
Run:

```bash
npm run check
```

Then run each custom skill inside Claude Code:
- `/check-project`
- `/review-changes`

### Step 47: Commit the Configuration
Run:

```bash
git add .
git commit -m "Configure Claude Code project harness"
```

Check:

```bash
git status
```

Expected result: `working tree clean`

---

## Part 12: Troubleshooting

### Claude Command Is Not Found
Try:
- Close and reopen the terminal.
- Run `claude --version`.
- Run `claude doctor`.
- Confirm the installer completed.
- Check that the installation directory is on your system `PATH`.

### Claude Does Not Load the Instructions
Confirm:
- The file name is exactly `CLAUDE.md`.
- The file is inside the repository hierarchy.
- Claude Code was started from the correct project directory.
- You started a new session after changing instructions.
- `/memory` shows the expected files.

### A Skill Does Not Appear
Confirm the structure:
```text
.claude/
└── skills/
    └── skill-name/
        └── SKILL.md
```
Then:
- Restart Claude Code.
- Type `/` and search for the skill name.
- Check the frontmatter syntax.
- Confirm that `SKILL.md` uses the exact uppercase capitalization.

### The Formatting Hook Does Not Run
Confirm:
- The hook is registered under `PostToolUse`.
- Its matcher includes `Edit|Write`.
- Node.js is available in your environment.
- Prettier is installed.
- The edited file uses a supported extension (`.js`, `.json`, `.md`).
- The script path is correct.
- `.claude/settings.json` is valid JSON.
- Run the formatter manually to test: `npx prettier --write src/app.js`

### A Hook Blocks the Wrong Command
- Review regular expressions in `.claude/hooks/block-dangerous-command.js`.
- Make patterns as specific as possible; overly broad patterns may block harmless commands.
- Always test safety hooks in a disposable repository.

### Claude Ignores a Rule
Improve the rule by making it:
- **Specific**
- **Testable**
- **Direct**
- **Relevant** to the repository
- **Free from contradictory instructions**

*Weak instruction:*
> "Write good tests."

*Stronger instruction:*
> "Every new endpoint must include one successful API test and at least one error-path API test using Supertest."

---

## Part 13: Extension Challenges

### Challenge A: Add a Bug-Fix Skill
Create `.claude/skills/fix-bug/SKILL.md` that requires Claude to:
1. Reproduce the bug.
2. Identify the root cause.
3. Add a failing regression test.
4. Implement the smallest safe fix.
5. Run all checks.
6. Review the diff.
7. Explain the cause and solution.

### Challenge B: Add a Documentation Hook
Create a hook that warns when API route files change but `README.md` does not. The hook should inspect changed files and print a reminder.

### Challenge C: Add a Test-Only Rule
Expand `test/CLAUDE.md` so Claude must use `expect(response.body).toEqual(...)` for exact error-response testing. Test whether Claude follows the more specific rule.

### Challenge D: Create a Personal Skill
Create a user-level skill under your personal Claude configuration (`~/.claude/skills/explain-code/SKILL.md`) to explain code using:
- Purpose
- Inputs / Outputs
- Control flow
- Dependencies
- Risks
- Example execution

### Challenge E: Add a Session Log Hook
Create a hook that appends session start and completion events to `.claude/session-events.jsonl`. Ensure the generated log is added to `.gitignore`.

---

## Reflection Questions

Answer the following questions in complete sentences:

1. What is the purpose of the root project instruction file?
2. What information belongs in project instructions?
3. What information should not be stored there?
4. How do directory-specific instructions improve control?
5. What is the difference between project and user memory?
6. Why should personal preferences not always be committed?
7. How did `/memory` help verify the active context?
8. Why are hooks more deterministic than prompt instructions?
9. What is the difference between a `PreToolUse` and `PostToolUse` hook?
10. Why is command blocking useful?
11. What risks can poorly designed hooks introduce?
12. Why should hook scripts be tested in a disposable repository?
13. What is the difference between a project instruction and a skill?
14. Why should a repeated procedure usually become a skill?
15. How did the custom endpoint skill improve consistency?
16. Did Claude follow source and test rules differently?
17. What happened when project configuration was disabled?
18. Which rules had the greatest effect on Claude’s behavior?
19. What additional rules would a production repository need?
20. How does this setup function as a lightweight coding harness?

---

## Lab Submission Requirements

Submit the following items:
- [ ] A screenshot showing the installed Claude Code version.
- [ ] A screenshot of successful authentication.
- [ ] The complete `claude-task-api` repository.
- [ ] The root project instruction file (`CLAUDE.md`).
- [ ] The source-specific instruction file (`src/CLAUDE.md`).
- [ ] The test-specific instruction file (`test/CLAUDE.md`).
- [ ] The project settings file (`.claude/settings.json`).
- [ ] Both hook scripts (`block-dangerous-command.js` and `format-after-edit.js`).
- [ ] All three reusable skills (`add-endpoint`, `check-project`, `review-changes`).
- [ ] Evidence that the formatting hook ran.
- [ ] Evidence that a prohibited command was blocked.
- [ ] Evidence that `/add-endpoint` was discovered and executed.
- [ ] Evidence that `/check-project` completed.
- [ ] Evidence that `/review-changes` completed without editing files.
- [ ] A screenshot showing all quality checks passing (`npm run check`).
- [ ] The completed configured-versus-unconfigured comparison table.
- [ ] Answers to the reflection questions.
- [ ] A 300–500 word conclusion.

---

## Lab Conclusion

In this lab, you transformed a standard Node.js repository into a structured Claude Code project. The completed configuration provides:
- **Persistent repository knowledge**
- **Shared coding standards**
- **Directory-specific rules**
- **Cross-session memory**
- **Permission controls**
- **Deterministic lifecycle hooks**
- **Automatic formatting**
- **Dangerous-command blocking**
- **Reusable development skills**
- **Consistent testing and verification**

The central lesson is that effective AI-assisted development does not depend only on the model. The repository’s instructions, memory, permissions, hooks, reusable procedures, and verification process form the surrounding harness that determines how reliably the coding agent behaves:

$$\text{Project Context} \longrightarrow \text{Persistent Instructions} \longrightarrow \text{Scoped Rules} \longrightarrow \text{Agent Execution} \longrightarrow \text{Deterministic Hooks} \longrightarrow \text{Reusable Skills} \longrightarrow \text{Verification}$$

These same concepts can later be expanded into team-level AI development platforms, multi-agent workflows, MCP integrations, production guardrails, and observable coding harnesses.
