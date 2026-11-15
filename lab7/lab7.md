# Hands-On Lab 7: Engineer Better Coding Prompts

---

## Lab Overview & Objectives

In this lab, you will learn how **Prompt Engineering** directly impacts the reliability, scope, and quality of AI-generated code. You will begin with a vague, unstructured prompt, and iteratively improve it by adding:
1. **Context** (Project tech stack and file locations)
2. **Constraints** (Boundary protection and dependency rules)
3. **Acceptance Criteria** (Precise HTTP status codes, edge-case validation, and test requirements)

### Estimated Time
Approximately 30–45 minutes

### Learning Objectives
By the end of this lab, you will be able to:
- Contrast agent responses between vague prompts and precision-engineered prompts.
- Establish negative constraints that prevent unauthorized dependencies and scope creep.
- Formulate clear acceptance criteria that guide the agent to produce verified, production-grade code.
- Prevent common agent pitfalls (hallucinations, excessive refactoring, missing error paths).

---

## Step 1: Create a Sample Project

Create a new Node.js project:

```bash
mkdir prompt-lab
cd prompt-lab

git init
npm init -y
npm install express
```

Create the following directory structure:

```text
prompt-lab/
│
├── src/
│   ├── app.js
│   └── users.js
│
└── test/
```

Quick setup:
- **macOS / Linux / Git Bash:**
  ```bash
  mkdir -p src test
  touch src/app.js src/users.js
  ```
- **Windows PowerShell:**
  ```powershell
  New-Item -ItemType Directory src, test -Force
  New-Item src\app.js, src\users.js
  ```

*(Assume the application already contains a basic User API implementation).*

---

## Step 2: Write a Poor Prompt

Open your preferred coding agent (Claude Code, Codex CLI, or Gemini CLI).

Submit this vague, unstructured prompt:

```text
Add user validation.
```

### Review and Record:
- [ ] Was the request clear?
- [ ] Did the AI ask clarifying questions, or did it assume requirements?
- [ ] Did it locate and modify the correct files?
- [ ] Was the validation comprehensive (e.g., empty string, email format, types)?
- [ ] Were corresponding tests added automatically?

---

## Step 3: Add Context

Improve the prompt by supplying baseline project information and file locations:

```text
This is an Express.js REST API.
 
User routes are located in src/users.js.
 
Add validation for creating new users.
```

Run the prompt again in a fresh session and compare the response with the first blind attempt.

---

## Step 4: Add Constraints

Now establish strict guardrails to prevent scope creep and unwanted dependencies:

```text
This is an Express.js REST API.
 
User routes are located in src/users.js.
 
Add validation for creating new users.
 
Constraints:
- Modify only src/users.js.
- Do not add new dependencies (e.g., Joi, Yup, Zod, express-validator).
- Preserve existing functionality.
- Keep the implementation simple and self-contained.
```

Observe whether the AI stays strictly within the requested file and dependency boundaries.

---

## Step 5: Add Acceptance Criteria

Now craft a production-quality prompt with explicit functional criteria, status codes, and verification requirements:

```text
Project: Express.js REST API
 
Task:
Add validation for creating new users.
 
Requirements:
- Name must not be empty.
- Email must be valid.
- Return HTTP 400 for invalid input with a JSON error message.
- Return HTTP 201 when user creation is successful.
- Modify only src/users.js.
- Do not add dependencies.
- Preserve existing functionality.
- Add unit tests covering successful and error paths.
- Explain which files changed.
- Run tests before completing the task.
```

Review the generated implementation and compare code clarity, error handling, and test coverage.

---

## Step 6: Compare the Results

Complete the following comparison matrix based on your findings:

| Prompt Type | Correct Files | Validation Complete | Tests Added | Scope Controlled | Overall Quality |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Poor Prompt** | | | | | |
| **Context Added** | | | | | |
| **Constraints Added** | | | | | |
| **Acceptance Criteria** | | | | | |

---

## Step 7: Build Your Own Prompt

Now apply these principles independently. Write an optimized prompt for the following feature:

> **"Add `PUT /users/:id` to update an existing user."**

### Ensure your prompt includes:
1. **Project context** (Express.js, file locations)
2. **Task description** (Endpoint, method, parameters)
3. **Constraints** (Files allowed to change, zero new packages)
4. **Acceptance Criteria** (400 on invalid input, 404 on missing user, 200 on success)
5. **Verification steps** (Unit tests, `npm test`, review diff)

Run the prompt in your agent and evaluate the generated output.

---

## Reflection Questions

Answer the following questions in complete sentences:

1. Which prompt strategy produced the cleanest and most accurate code?
2. How did providing explicit repository context improve file discovery?
3. Why are negative constraints (e.g., *"Do not install new packages"*) critical in production AI workflows?
4. How did explicit acceptance criteria (status codes and error payloads) eliminate ambiguity?
5. Which prompt format would you standardize across your engineering team, and why?

---

## Lab Conclusion

This lab demonstrated that **better prompts produce measurably better code**. 

A production-grade prompt does not merely state *what* to build—it engineers the complete constraint envelope:

$$\text{Project Context} \longrightarrow \text{Clear Task} \longrightarrow \text{Negative Constraints} \longrightarrow \text{Acceptance Criteria} \longrightarrow \text{Verification Requirements}$$

By clearly defining what success looks like, restricting the blast radius of changes, and mandating test verification, you eliminate hallucinations and turn AI agents into reliable engineering tools.
