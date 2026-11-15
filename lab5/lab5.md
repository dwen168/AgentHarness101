# Hands-On Lab 5: Gemini CLI Development Workflow

---

## Lab Overview

In this lab, you will configure Google Gemini CLI for a software project, create persistent project rules (`GEMINI.md`), build repository memory, use Gemini to edit code, and compare weak prompts with optimized prompts.

Rather than issuing open-ended requests, you will learn to supply scope, constraints, acceptance criteria, and verification steps to turn Gemini CLI into a reliable coding partner.

### Estimated Time
Approximately 45–60 minutes

### Learning Objectives
By the end of this lab, you will be able to:
- Install and authenticate Gemini CLI.
- Configure project-level settings (`.gemini/settings.json`).
- Create persistent repository instructions (`GEMINI.md`).
- Inspect and refresh Gemini’s project memory (`/memory show`, `/memory refresh`).
- Use Gemini to make controlled, plan-first code changes.
- Improve coding prompts with explicit scope, constraints, and acceptance criteria.

---

## Part 1: Install Gemini CLI

### Step 1: Verify Node.js
Open your terminal and run:

```bash
node --version
npm --version
```

### Step 2: Install Gemini CLI
Install the official global package:

```bash
npm install -g @google/gemini-cli
```

Verify the installation:

```bash
gemini --version
```

### Step 3: Authenticate
Start Gemini CLI:

```bash
gemini
```

Select **Sign in with Google** and complete the browser login.

> [!NOTE]
> API-key authentication is also supported when required (via `export GEMINI_API_KEY="..."`).

Exit the session after authentication:

```text
/quit
```

---

## Part 2: Create the Sample Project

### Step 4: Create the Repository
Run:

```bash
mkdir gemini-task-api
cd gemini-task-api

git init
npm init -y
npm install express
npm install --save-dev jest supertest
```

Create the folders:

```bash
mkdir src test
```

Create the initial files:
- `src/app.js`
- `src/server.js`
- `test/app.test.js`

### Step 5: Add the Application Code
Add the following code to `src/app.js`:

```javascript
const express = require("express");
 
const app = express();
app.use(express.json());
 
const tasks = [
  {
    id: 1,
    title: "Configure Gemini CLI",
    completed: false,
  },
];
 
app.get("/tasks", (request, response) => {
  response.status(200).json(tasks);
});
 
app.get("/tasks/:id", (request, response) => {
  const taskId = Number(request.params.id);
  const task = tasks.find((item) => item.id === taskId);
 
  if (!task) {
    return response.status(404).json({
      error: "Task not found",
    });
  }
 
  return response.status(200).json(task);
});
 
module.exports = app;
```

Add the following code to `src/server.js`:

```javascript
const app = require("./app");
 
const port = process.env.PORT || 3000;
 
app.listen(port, () => {
  console.log(`Task API running on port ${port}`);
});
```

### Step 6: Add the Tests
Add the following code to `test/app.test.js`:

```javascript
const request = require("supertest");
 
const app = require("../src/app");
 
describe("Task API", () => {
  test("GET /tasks returns all tasks", async () => {
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
});
```

Update the `scripts` section in `package.json`:

```json
"scripts": {
  "start": "node src/server.js",
  "test": "jest --runInBand"
}
```

Run tests to establish your baseline:

```bash
npm test
```

Create the baseline commit:

```bash
git add .
git commit -m "Create Gemini CLI lab project"
```

---

## Part 3: Configure Gemini CLI

Gemini CLI supports user settings in `~/.gemini/settings.json` and project settings in `.gemini/settings.json`. Project settings apply when Gemini CLI is run from that repository root.

### Step 7: Create Project Settings
Create `.gemini/settings.json`:

```json
{
  "general": {
    "preferredEditor": "vscode"
  }
}
```

You may also open the interactive Gemini settings interface from inside the CLI:

```text
/settings
```

---

## Part 4: Create Project Rules

Gemini CLI uses a project context file named `GEMINI.md` to store persistent instructions and coding standards.

### Step 8: Create the Project Instruction File
Create `GEMINI.md` in the repository root:

````markdown
# Task API Project Rules
 
## Project Technology
 
- Node.js
- Express
- CommonJS
- Jest
- Supertest
 
## Coding Rules
 
- Use two-space indentation.
- Use semicolons.
- Use descriptive names.
- Keep route handlers small.
- Return explicit HTTP status codes.
- Return errors as JSON with an `error` property.
- Do not add dependencies without approval.
- Do not modify unrelated files.
 
## Testing Rules
 
- Add tests for every new endpoint.
- Test successful and unsuccessful behavior.
- Verify status codes and response bodies.
- Run `npm test` after code changes.
 
## Workflow Rules
 
Before editing:
1. Inspect the relevant files.
2. Explain the current behavior.
3. Propose the smallest safe change.
4. List the files that will change.
5. Wait for approval.
 
After editing:
1. Run `npm test`.
2. Run `git diff`.
3. List all changed files.
4. Report the test results.
````

---

## Part 5: Build Repository Memory

### Step 9: Start Gemini in the Repository
Start Gemini CLI from the repository root:

```bash
gemini
```

Inspect the active memory:

```text
/memory show
```

Gemini displays the combined project context loaded from the repository’s context files.

Ask:

```text
Summarize the coding, testing, and workflow rules currently loaded for this repository.
```

Confirm that Gemini mentions:
- CommonJS
- Explicit status codes
- Tests for new endpoints
- Planning before editing
- Running `npm test`
- Reviewing `git diff`

### Step 10: Update Repository Memory
Add this line to `GEMINI.md`:
```markdown
- Every final response must list the endpoint, status codes, files changed, and test result.
```

Reload the memory:

```text
/memory refresh
```

Inspect it again to verify the update:

```text
/memory show
```

---

## Part 6: Use Gemini to Plan a Change

The task is to add:
`POST /tasks`

Required behavior:
- Accept a JSON body containing `title`.
- Reject missing or empty titles.
- Return `400` for invalid input.
- Return `201` with the new task.
- Add tests.
- Do not add dependencies.

### Step 11: Submit a Planning Prompt
Inside Gemini CLI, enter:

```text
Analyze this repository and plan the following feature:
 
POST /tasks
 
Requirements:
 
- Accept a JSON body containing title.
- Title must be a non-empty string.
- Return 400 for invalid input.
- Return 201 with the created task.
- Add successful and invalid-input tests.
- Do not add dependencies.
 
Do not modify files yet.
 
Provide:
 
1. Current behavior
2. Files that need to change
3. Proposed implementation
4. Tests to add
5. Edge cases
6. Numbered execution plan
 
Wait for approval.
```

Review the plan. A suitable plan should strictly limit changes to:
- `src/app.js`
- `test/app.test.js`

---

## Part 7: Execute Code Edits

### Step 12: Approve the Plan
Enter:

```text
The plan is approved.
 
Implement the feature now.
 
Follow all project rules.
 
After editing:
 
- Run npm test.
- Run git diff.
- Do not commit.
- List all changed files.
- Report the endpoint, status codes, and test results.
```

> [!WARNING]
> Review every requested file edit or command before approving it in the CLI.

### Step 13: Inspect the Generated Code
A clean route implementation may resemble:

```javascript
app.post("/tasks", (request, response) => {
  const { title } = request.body;
 
  if (
    typeof title !== "string" ||
    title.trim().length === 0
  ) {
    return response.status(400).json({
      error: "A valid task title is required",
    });
  }
 
  const task = {
    id: tasks.length + 1,
    title: title.trim(),
    completed: false,
  };
 
  tasks.push(task);
 
  return response.status(201).json(task);
});
```

A successful test may resemble:

```javascript
test("POST /tasks creates a task", async () => {
  const response = await request(app)
    .post("/tasks")
    .send({
      title: "Optimize Gemini prompts",
    });
 
  expect(response.statusCode).toBe(201);
  expect(response.body).toMatchObject({
    title: "Optimize Gemini prompts",
    completed: false,
  });
});
```

An invalid-input test may resemble:

```javascript
test("POST /tasks rejects an empty title", async () => {
  const response = await request(app)
    .post("/tasks")
    .send({
      title: "   ",
    });
 
  expect(response.statusCode).toBe(400);
  expect(response.body).toEqual({
    error: "A valid task title is required",
  });
});
```

### Step 14: Verify the Work Manually
Run:

```bash
npm test
git status
git diff
```

Check:
- [ ] Only the expected files changed
- [ ] `POST /tasks` was added
- [ ] Empty titles are rejected
- [ ] Whitespace-only titles are rejected
- [ ] Successful creation returns 201
- [ ] Invalid input returns 400
- [ ] All tests pass
- [ ] No dependencies were added

---

## Part 8: Optimize Prompts

### Step 15: Try a Weak Prompt
Start from a clean branch or restore the original project. Use:

```text
Add task creation.
```

Record:
- Did Gemini understand the exact endpoint name?
- Did it add validation?
- Did it add tests?
- Did it use the correct status codes?
- Did it modify unrelated files?

### Step 16: Use an Optimized Prompt
Use:

```text
Add POST /tasks to the existing Express application.
 
Acceptance criteria:
 
- Accept JSON containing title.
- Title must be a non-empty string after trimming.
- Return 400 with {"error":"A valid task title is required"} for invalid input.
- Return 201 with the created task for valid input.
- Set completed to false.
- Add one successful test.
- Add tests for missing, empty, and whitespace-only titles.
- Use the existing in-memory task array.
- Do not add dependencies.
- Change only src/app.js and test/app.test.js.
- Run npm test and review git diff.
 
Before editing, provide a plan and wait for approval.
```

Compare the results between the two prompts:

| Evaluation Area | Weak Prompt | Optimized Prompt |
| :--- | :---: | :---: |
| **Scope was clear** | | |
| **Status codes were defined** | | |
| **Validation was complete** | | |
| **Tests were added** | | |
| **Files were limited** | | |
| **Unrelated changes were avoided** | | |
| **Verification was performed** | | |

---

## Final Review

Ask Gemini:

```text
Review the current uncommitted changes.
 
Do not edit files.
 
Check:
 
1. Functional correctness
2. Input validation
3. Status codes
4. Error responses
5. Test coverage
6. Unrelated changes
7. Compliance with GEMINI.md
 
End with either:
- Ready to commit
- Needs changes
```

Run the final verification yourself:

```bash
npm test
git diff
```

Commit only after reviewing the generated code:

```bash
git add src/app.js test/app.test.js GEMINI.md .gemini/settings.json
git commit -m "Configure Gemini CLI development workflow"
```

---

## Lab Submission

Students should submit:
- [ ] Screenshot of the Gemini CLI version.
- [ ] Project settings file (`.gemini/settings.json`).
- [ ] Project instruction file (`GEMINI.md`).
- [ ] Output from `/memory show`.
- [ ] Gemini’s implementation plan.
- [ ] Generated code changes.
- [ ] Passing test results (`npm test`).
- [ ] Git diff (`git diff`).
- [ ] The completed weak-prompt versus optimized-prompt comparison table.
- [ ] A short explanation of how project memory and stronger prompts improved the result.

---

## Lab Conclusion

In this lab, you configured Gemini CLI as a repository-aware coding agent. You created persistent project rules, loaded them into repository memory, planned a feature before editing, approved controlled code changes, verified the results, and compared weak prompts with optimized prompts.

The main takeaway is that Gemini produces significantly more reliable code when governed by a structured harness:

$$\text{Project Rules} \longrightarrow \text{Repository Memory} \longrightarrow \text{Clear Objective} \longrightarrow \text{Acceptance Criteria} \longrightarrow \text{Scope \& Constraints} \longrightarrow \text{Verification}$$

A strong prompt does not merely describe *what* to build. It explicitly defines successful behavior, scope boundaries, validation rules, testing standards, and completion requirements.
