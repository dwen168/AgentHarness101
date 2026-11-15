# Hands-On Lab 6: Optimize Context for Large Projects

---

## Lab Overview & Objectives

In this lab, you will learn how **Context Engineering** improves AI coding performance. You will compare how an AI coding agent (Claude Code, OpenAI Codex CLI, or Gemini CLI) performs under three different operational conditions on the same codebase:
1. **No Context** (Blind prompt)
2. **Partial Context** (Ad-hoc unstructured notes)
3. **Well-Structured / Compressed Context** (Curated architectural boundaries)

### Estimated Time
Approximately 45–60 minutes

### Learning Objectives
By the end of this lab, you will be able to:
- Understand the direct impact of Context Engineering on agent accuracy and speed.
- Contrast agent performance across zero-context, raw-context, and compressed-context strategies.
- Enforce a "Retrieve-Before-Edit" workflow to prevent runaway modifications.
- Minimize token usage, hallucinations, and out-of-scope edits on medium-to-large repositories.

---

## Step 1: Create a Sample Repository

Create a new project folder:

```bash
mkdir context-lab
cd context-lab

git init
npm init -y
```

Create the following project structure:

```text
context-lab/
│
├── src/
│   ├── auth/
│   │   ├── login.js
│   │   ├── register.js
│   │   └── jwt.js
│   │
│   ├── users/
│   ├── database/
│   ├── middleware/
│   ├── routes/
│   └── utils/
│
├── test/
└── README.md
```

You can create the structure quickly:
- **macOS / Linux / Git Bash:**
  ```bash
  mkdir -p src/auth src/users src/database src/middleware src/routes src/utils test
  touch src/auth/login.js src/auth/register.js src/auth/jwt.js README.md
  ```
- **Windows PowerShell:**
  ```powershell
  New-Item -ItemType Directory src\auth, src\users, src\database, src\middleware, src\routes, src\utils, test -Force
  New-Item src\auth\login.js, src\auth\register.js, src\auth\jwt.js, README.md
  ```

> [!NOTE]
> The goal is to simulate a multi-module repository where the agent must identify the correct files before making changes rather than blindly guessing.

---

## Step 2: Test Without Context

Open your preferred coding agent (Claude Code, Codex CLI, or Gemini CLI) from the project root.

Submit this blind prompt without providing background information:

```text
Add request logging to the user authentication process.
```

### Observe:
- Which files does the agent inspect?
- Does it accurately identify the authentication module?
- Does it ask clarifying questions or guess your stack?
- Does it attempt to edit unrelated files (e.g., `src/database/` or `src/routes/`)?

*Record your observations.*

---

## Step 3: Provide Repository Context

Now run a new session and provide uncompressed, narrative context:

```text
Project Information:

• Express.js application
• Authentication code is located in src/auth
• JWT generation is handled by jwt.js
• User routes are inside src/routes
• Tests are located in test/

Only modify authentication-related files.
```

Now submit the same task request:

```text
Add request logging to the user authentication process.
```

Compare the agent's response and file inspection path with the previous blind attempt.

---

## Step 4: Compress the Context

Instead of providing raw narrative paragraphs or dumping the entire file tree, provide a **concise, structured architecture summary**:

```text
Repository Summary:

Backend: Express.js
Authentication: src/auth/
Database: src/database/
Routes: src/routes/
Middleware: src/middleware/
Testing: Jest

Goal:
Only update authentication files.
Do not modify routes or database logic.
```

Submit the request again.

> [!TIP]
> Notice how a concise, structured summary often produces faster, more accurate results than either no context or dumping entire file contents into the prompt.

---

## Step 5: Retrieve Relevant Files

In production harness workflows, **retrieval must always precede execution**. Before allowing the agent to edit code, ask it to identify and justify the target files:

```text
Analyze the repository.

List only the files that are required to add request logging to the authentication process.

Do not modify any files.
```

### Evaluation Criteria:
- **Expected files to identify:**
  - `src/auth/login.js`
  - `src/auth/register.js`
  - `src/auth/jwt.js`
- **Files it must avoid touching:**
  - `src/database/`
  - `src/utils/`
  - `README.md`

---

## Step 6: Execute the Change

After confirming that the agent has isolated the exact required files, approve the implementation:

```text
Update the authentication process by adding request logging.

Requirements:

- Only modify files inside src/auth
- Do not change existing functionality
- Keep logging simple
- Explain which files were modified
```

Review the generated diff before accepting or committing the changes.

---

## Step 7: Measure Output Quality

Complete the following comparison matrix based on your findings:

| Context Strategy | Correct Files Selected | Accurate Response | Needed Clarification | Overall Quality |
| :--- | :---: | :---: | :---: | :---: |
| **No Context** | | | | |
| **Partial Context** | | | | |
| **Compressed Context** | | | | |

---

## Reflection Questions

Answer the following questions in complete sentences:

1. Which context strategy produced the most accurate result?
2. Did providing the repository structure reduce unnecessary file selection and token consumption?
3. Why is a concise repository summary often superior to loading every file in the project?
4. How does separating **file retrieval** from **file editing** improve agent safety?
5. How does Context Engineering scale when working with enterprise repositories containing tens of thousands of files?

---

## Lab Conclusion

This lab demonstrated that **Context Engineering is one of the most critical pillars of modern AI-assisted software development**. 

Rather than overwhelming the model with an entire codebase or leaving it unguided in the dark, reliable engineering workflows supply **curated, high-density project boundaries**:

$$\text{Raw Repository} \longrightarrow \text{Context Filtering \& Compression} \longrightarrow \text{Target File Retrieval} \longrightarrow \text{Controlled Execution}$$

By enforcing structured summaries and pre-execution file discovery, you significantly reduce reasoning latency, eliminate unnecessary token waste, prevent unintended file mutations, and generate higher-quality code.
