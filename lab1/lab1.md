# Hands-On Lab 1: Install and Compare AI Coding Tools

## Lab Overview

In this lab, you will install and test three leading terminal-based AI coding agents:
- **Claude Code**
- **OpenAI Codex CLI**
- **Gemini CLI**

You will open the same sample software repository in each tool, submit the same prompt, and compare how each agent understands the codebase, plans its work, recommends changes, and communicates its results.

This lab focuses on controlled comparison. You will initially instruct the tools to analyze the repository without modifying any files. This makes it easier to compare their reasoning, repository understanding, and proposed implementation plans.

### Estimated Completion Time
Approximately 60–90 minutes

### Learning Objectives
By the end of this lab, you will be able to:
- Install Claude Code, Codex CLI, and Gemini CLI.
- Authenticate each tool using a supported account or API key.
- Verify that all three command-line tools are working.
- Open an existing software repository from the terminal.
- Give the same repository-level task to multiple AI coding agents.
- Compare their plans, accuracy, clarity, safety, and usefulness.
- Select an appropriate AI coding tool for a development task.

---

## Part 1: Prepare Your Computer

### Step 1: Confirm the Required Software
You need:
- A Windows, macOS, or Linux computer
- An internet connection
- A terminal or command-line application
- Git
- A code editor such as Visual Studio Code
- An account or API access for each AI provider you plan to test

For this lab, students using Windows may use PowerShell, Command Prompt, Git Bash, or Windows Subsystem for Linux (WSL).

Claude Code officially supports current Windows, macOS, and common Linux environments. Its documented minimum hardware requirement is 4 GB of RAM.

### Step 2: Open Your Terminal
Use the appropriate terminal for your operating system:

- **Windows**: Open PowerShell by searching for `PowerShell`
- **macOS**: Open **Applications → Utilities → Terminal**
- **Linux**: Open your preferred terminal application.

### Step 3: Verify Git
Run:
```bash
git --version
```

Expected output:
```text
git version 2.x.x
```

If Git is not installed, install it before proceeding.

### Step 4: Verify Node.js and npm
Gemini CLI supports installation through npm, and npm is also an optional installation method for Codex CLI and Claude Code.

Run:
```bash
node --version
npm --version
```

Expected output should resemble:
```text
v22.x.x
10.x.x
```

For the smoothest lab experience, use a current Long-Term Support (LTS) version of Node.js.

Claude Code also offers a native installation that does not require npm. Its npm installation currently expects Node.js 22 or later.

### Step 5: Create a Lab Workspace
Run:
```bash
mkdir ai-coding-tools-lab
cd ai-coding-tools-lab
```

Confirm your location:

- **macOS, Linux, or Git Bash**:
  ```bash
  pwd
  ```
- **Windows PowerShell**:
  ```powershell
  Get-Location
  ```

---

## Part 2: Install Claude Code

### Step 6: Install Claude Code
Claude Code provides native installers for Windows, macOS, Linux, and WSL. Anthropic currently recommends the native installation method.

#### Windows PowerShell
Run:
```powershell
irm https://claude.ai/install.ps1 | iex
```

#### Windows Command Prompt
Run:
```cmd
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

#### macOS, Linux, or WSL
Run:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

#### Alternative npm Installation
You may alternatively run:
```bash
npm install -g @anthropic-ai/claude-code
```

### Step 7: Verify Claude Code
Close and reopen the terminal if necessary, then run:
```bash
claude --version
```

You should see an installed version number.

You can also run:
```bash
claude doctor
```

This checks the installation and reports common configuration or update problems.

### Step 8: Authenticate Claude Code
Start Claude Code:
```bash
claude
```

Follow the authentication instructions displayed in the terminal.

Individual users can authenticate with a Claude account. Team and enterprise environments may use organizational accounts, cloud providers, or other supported authentication configurations.

Complete the browser login if prompted.

After authentication, exit the session using:
```text
/exit
```
You may also press `Ctrl+C`.

### Step 9: Record Your Claude Code Setup
Write down:
- **Installed successfully**: Yes / No
- **Version**: 
- **Authentication method**: 
- **Installation problems**: 

---

## Part 3: Install OpenAI Codex CLI

### Step 10: Install Codex CLI
OpenAI provides native installation scripts and package-manager options for Codex CLI.

#### Windows PowerShell
Run:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

#### macOS or Linux
Run:
```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

#### Alternative npm Installation
Run:
```bash
npm install -g @openai/codex
```

#### Alternative Homebrew Installation
On supported macOS or Linux systems:
```bash
brew install --cask codex
```

### Step 11: Verify Codex CLI
Run:
```bash
codex --version
```

You should see the currently installed version.

Then start Codex:
```bash
codex
```

### Step 12: Authenticate Codex CLI
When Codex starts, select:
```text
Sign in with ChatGPT
```

Complete the browser-based login.

OpenAI recommends ChatGPT sign-in for users accessing Codex through an eligible ChatGPT plan. API-key authentication is also supported but requires additional configuration.

After authentication, exit the session.

### Step 13: Optional API-Key Authentication
> [!WARNING]
> Only perform this step when your instructor requires API-based authentication.
>
> Never paste an API key directly into:
> - Source code
> - A README file
> - A Git commit
> - A screenshot
> - A shared classroom document
> - A prompt sent to another AI tool
>
> Store credentials using environment variables or the authentication method recommended by the provider.

### Step 14: Record Your Codex Setup
Write down:
- **Installed successfully**: Yes / No
- **Version**: 
- **Authentication method**: 
- **Installation problems**: 

---

## Part 4: Install Gemini CLI

### Step 15: Install Gemini CLI
Google provides npm, npx, Homebrew, MacPorts, and Conda-based installation options.

#### Recommended Global npm Installation
Run:
```bash
npm install -g @google/gemini-cli
```

#### Run Without Installing
You may test Gemini CLI directly with:
```bash
npx @google/gemini-cli
```

#### Homebrew Installation
On supported macOS or Linux systems:
```bash
brew install gemini-cli
```

### Step 16: Verify Gemini CLI
Run:
```bash
gemini --version
```

Then start Gemini CLI:
```bash
gemini
```

### Step 17: Authenticate with Google
For most individual users, Google recommends starting Gemini CLI and selecting:
```text
Sign in with Google
```

A browser window should open. Complete the login process and return to the terminal. Credentials are then cached for future sessions.

Some organizational or Google Workspace accounts may require a Google Cloud project.

### Step 18: Optional Gemini API-Key Authentication
Instead of Google account sign-in, you may use a Gemini API key from Google AI Studio.

- **macOS, Linux, or Git Bash**:
  ```bash
  export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
  ```
- **Windows PowerShell**:
  ```powershell
  $env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
  ```

Then run:
```bash
gemini
```

Select the API-key authentication option when prompted.

> [!WARNING]
> Google warns that Gemini API keys must be treated as sensitive credentials. Do not place your real key inside the sample repository.

### Step 19: Record Your Gemini Setup
Write down:
- **Installed successfully**: Yes / No
- **Version**: 
- **Authentication method**: 
- **Installation problems**: 

---

## Part 5: Verify All Three Tools

### Step 20: Run the Verification Commands
Run:
```bash
claude --version
codex --version
gemini --version
git --version
node --version
npm --version
```

Complete the checklist:
- [ ] Claude Code opens successfully
- [ ] Codex CLI opens successfully
- [ ] Gemini CLI opens successfully
- [ ] Authentication works in Claude Code
- [ ] Authentication works in Codex CLI
- [ ] Authentication works in Gemini CLI
- [ ] Git is installed
- [ ] Node.js and npm are available

> [!IMPORTANT]
> Do not continue until all required tools are working.

---

## Part 6: Create the Sample Repository

### Step 21: Create the Project Folder
From the lab workspace, run:
```bash
mkdir task-manager-api
cd task-manager-api
```

Initialize Git:
```bash
git init
```

### Step 22: Create the Package File
Run:
```bash
npm init -y
```

Install Express:
```bash
npm install express
```

Install a development tool for testing:
```bash
npm install --save-dev supertest
```

### Step 23: Create the Project Structure
Create the following folders:
```bash
mkdir src
mkdir test
```

Create these files:
- `src/app.js`
- `src/server.js`
- `test/app.test.js`
- `README.md`
- `.gitignore`

On PowerShell, you can create the files with:
```powershell
New-Item src/app.js
New-Item src/server.js
New-Item test/app.test.js
New-Item README.md
New-Item .gitignore
```

On macOS, Linux, or Git Bash:
```bash
touch src/app.js src/server.js test/app.test.js README.md .gitignore
```

### Step 24: Add the Application Code
Place the following code in `src/app.js`:
```javascript
const express = require("express");
 
const app = express();
app.use(express.json());
 
const tasks = [
  {
    id: 1,
    title: "Install AI coding tools",
    completed: false,
  },
  {
    id: 2,
    title: "Compare repository analysis",
    completed: true,
  },
];
 
app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});
 
app.get("/tasks", (req, res) => {
  res.json(tasks);
});
 
app.get("/tasks/:id", (req, res) => {
  const task = tasks.find((item) => item.id === Number(req.params.id));
 
  res.json(task);
});
 
module.exports = app;
```

This application intentionally contains a weakness: requesting an unknown task returns an empty result instead of a proper `404 Not Found` response.

### Step 25: Add the Server Code
Place this code in `src/server.js`:
```javascript
const app = require("./app");
 
const port = process.env.PORT || 3000;
 
app.listen(port, () => {
  console.log(`Task Manager API running on port ${port}`);
});
```

### Step 26: Add the Initial Test
Place this code in `test/app.test.js`:
```javascript
const request = require("supertest");
const app = require("../src/app");
 
describe("Task Manager API", () => {
  test("GET /health returns the API status", async () => {
    const response = await request(app).get("/health");
 
    expect(response.statusCode).toBe(200);
    expect(response.body).toEqual({ status: "ok" });
  });
});
```

### Step 27: Configure the Test Command
Open `package.json`.

Replace the existing `scripts` section with:
```json
"scripts": {
  "start": "node src/server.js",
  "test": "jest"
}
```

Install Jest:
```bash
npm install --save-dev jest
```

### Step 28: Add the Git Ignore File
Place this in `.gitignore`:
```gitignore
node_modules/
.env
coverage/
*.log
```

### Step 29: Add the README
Place this content in `README.md`:
````markdown
# Task Manager API
 
A small Express API used to compare AI coding agents.
 
## Commands
 
Install dependencies:
 
```bash
npm install
```
 
Run tests:
 
```bash
npm test
```
 
Start the API:
 
```bash
npm start
```
 
## Available Endpoints
 
- `GET /health`
- `GET /tasks`
- `GET /tasks/:id`
````

### Step 30: Run the Test
Run:
```bash
npm test
```

Expected result:
```text
1 test passed
```

### Step 31: Test the Application Manually
Start the server:
```bash
npm start
```

Open a browser and visit:
```text
http://localhost:3000/health
```

Expected response:
```json
{
  "status": "ok"
}
```

Visit:
```text
http://localhost:3000/tasks/999
```

Observe that the application does not return a well-designed 404 response.

Stop the server with `Ctrl+C`.

### Step 32: Create the Baseline Commit
Run:
```bash
git add .
git commit -m "Create task manager comparison project"
```

This baseline makes it possible to identify or reverse any modifications made by an agent.

Check the repository:
```bash
git status
```

Expected output:
```text
working tree clean
```

---

## Part 7: Prepare the Comparison Prompt

### Step 33: Use the Same Prompt in Every Tool
Copy the prompt below exactly:

```text
Analyze this repository as a senior software engineer.
 
The GET /tasks/:id endpoint does not correctly handle a task that does not exist.
 
Do not modify any files yet.
 
Please:
 
1. Explain the current repository structure.
2. Identify the exact cause of the problem.
3. Propose the smallest safe code change.
4. Identify the files that would need to change.
5. Propose the tests that should be added.
6. Mention any edge cases or risks.
7. End with a numbered implementation plan.
 
Keep the answer focused on this repository and do not implement the solution.
```

> [!IMPORTANT]
> Using the exact same prompt is essential. Changing the wording between tools would make the comparison less fair.

---

## Part 8: Test Claude Code

### Step 34: Confirm You Are Inside the Repository
Run:
```bash
pwd
```
or (PowerShell):
```powershell
Get-Location
```

The final folder should be `task-manager-api`.

### Step 35: Check the Git Status
Run:
```bash
git status
```

Confirm that the working tree is clean.

### Step 36: Start Claude Code
Run:
```bash
claude
```

Claude Code is designed to read codebases, edit files, run commands, and work with development tools.

### Step 37: Submit the Comparison Prompt
Paste the shared prompt.

> [!WARNING]
> Do not approve file modifications because this phase is analysis-only.

### Step 38: Save the Claude Response
Copy the response into a file outside the sample repository, or paste it into your lab worksheet under:
`Claude Code Response`

Record:
- **Time to first useful response**:
- **Files inspected**:
- **Did it identify the missing 404 behavior?**:
- **Did it mention Number conversion or invalid IDs?**:
- **Did it recommend tests?**:
- **Did it attempt to modify files?**:
- **Was the plan clear?**:

### Step 39: Exit and Confirm No Changes
Exit Claude Code.

Run:
```bash
git status
```

The expected result is:
```text
working tree clean
```

If Claude changed files, do not compare those modified files with the next tool. Restore the baseline first:
```bash
git restore .
```

---

## Part 9: Test Codex CLI

### Step 40: Start Codex
From the same repository, run:
```bash
codex
```

Codex CLI runs locally and can inspect and work with the repository in which it is launched.

### Step 41: Submit the Same Prompt
Paste the exact comparison prompt without making any changes.

Do not approve implementation or file editing during this phase.

### Step 42: Save the Codex Response
Record:
- **Time to first useful response**:
- **Files inspected**:
- **Did it identify the missing 404 behavior?**:
- **Did it mention invalid or nonnumeric IDs?**:
- **Did it recommend tests?**:
- **Did it attempt to modify files?**:
- **Was the plan clear?**:

### Step 43: Exit and Confirm No Changes
Run:
```bash
git status
```

If necessary, restore the repository:
```bash
git restore .
```

---

## Part 10: Test Gemini CLI

### Step 44: Start Gemini CLI
Run:
```bash
gemini
```

Gemini CLI includes repository analysis, file operations, shell-command capabilities, web tools, and extensibility features.

### Step 45: Submit the Same Prompt
Paste the exact comparison prompt.

Do not authorize implementation during this phase.

### Step 46: Save the Gemini Response
Record:
- **Time to first useful response**:
- **Files inspected**:
- **Did it identify the missing 404 behavior?**:
- **Did it mention invalid or nonnumeric IDs?**:
- **Did it recommend tests?**:
- **Did it attempt to modify files?**:
- **Was the plan clear?**:

### Step 47: Exit and Confirm No Changes
Run:
```bash
git status
```

Restore the baseline if required:
```bash
git restore .
```

---

## Part 11: Compare the Responses

### Step 48: Complete the Comparison Matrix
Score each category from 1 to 5:
- **1**: Poor
- **2**: Limited
- **3**: Acceptable
- **4**: Strong
- **5**: Excellent

| Evaluation Category | Claude Code | Codex CLI | Gemini CLI |
| :--- | :---: | :---: | :---: |
| Installation experience | | | |
| Authentication experience | | | |
| Repository understanding | | | |
| Root-cause identification | | | |
| Accuracy of proposed fix | | | |
| Test recommendations | | | |
| Edge-case awareness | | | |
| Clarity of implementation plan | | | |
| Respect for “do not modify” instruction | | | |
| Response speed | | | |
| Overall usefulness | | | |

### Step 49: Check for Important Technical Observations
A strong response should identify several of the following points:
- [ ] The endpoint searches for a task by numeric ID.
- [ ] The code does not check whether a matching task exists.
- [ ] Express currently sends an undefined or empty result.
- [ ] The endpoint should return HTTP 404 when no task exists.
- [ ] The response should include a useful error object or message.
- [ ] A test should be added for an existing task.
- [ ] A test should be added for a missing task.
- [ ] Invalid IDs such as `/tasks/abc` may require separate handling.
- [ ] The smallest fix is likely limited to `app.js` and `app.test.js`.
- [ ] Existing endpoint behavior should remain unchanged.

### Step 50: Identify Hallucinations or Unsupported Claims
For each tool, ask:
- Did it mention files that do not exist?
- Did it describe a database even though the project uses an in-memory array?
- Did it claim tests already exist when they do not?
- Did it recommend unnecessary architectural changes?
- Did it ignore the instruction not to modify files?
- Did it recommend a large refactor for a small defect?
- Did it assume a framework or dependency not present in the repository?

Record any unsupported claims.

---

## Part 12: Optional Implementation Comparison
*This part is optional but strongly recommended.*

To compare actual code changes fairly, create one Git branch per tool.

### Step 51: Create the Claude Branch
Run:
```bash
git switch -c comparison/claude
```

Start Claude Code and use:
```text
Implement the approved fix for the missing-task behavior.
 
Requirements:
 
- Return HTTP 404 when a numeric task ID does not exist.
- Return a JSON error message.
- Preserve existing successful behavior.
- Add tests for an existing task and a missing task.
- Run the full test suite.
- Do not add unnecessary dependencies.
- Summarize every file changed.
```

After reviewing the changes:
```bash
npm test
git diff
```

Commit them:
```bash
git add .
git commit -m "Implement missing task handling with Claude"
```

### Step 52: Create the Codex Branch
Return to the baseline:
```bash
git switch master
```
*(If your default branch is named `main`, use `git switch main`)*

Create a Codex branch:
```bash
git switch -c comparison/codex
```

Run Codex with the same implementation prompt.

Then run:
```bash
npm test
git diff
git add .
git commit -m "Implement missing task handling with Codex"
```

### Step 53: Create the Gemini Branch
Return to the baseline:
```bash
git switch master
```
*(or `git switch main`)*

Create the branch:
```bash
git switch -c comparison/gemini
```

Run Gemini CLI with the same implementation prompt.

Then run:
```bash
npm test
git diff
git add .
git commit -m "Implement missing task handling with Gemini"
```

### Step 54: Compare the Implementations
Compare branches using:
```bash
git diff comparison/claude..comparison/codex
git diff comparison/claude..comparison/gemini
git diff comparison/codex..comparison/gemini
```

Evaluate:
- Number of files changed
- Number of lines changed
- Correctness
- Test coverage
- Error-message quality
- Handling of invalid IDs
- Unnecessary changes
- Code readability
- Whether tests pass
- Whether the tool explained its work

---

## Part 13: Reflection Questions
Answer the following questions in complete sentences:

1. Which tool was easiest to install, and why?
2. Which authentication experience was the clearest?
3. Which tool understood the repository structure most accurately?
4. Which tool identified the root cause most directly?
5. Which tool produced the safest and smallest proposed change?
6. Which tool suggested the strongest tests?
7. Did any tool attempt to modify files despite being told not to?
8. Did any response include unsupported assumptions or hallucinations?
9. Which tool was most verbose?
10. Which tool produced the clearest numbered implementation plan?
11. Which tool would you choose for a small bug fix?
12. Which tool would you choose for understanding an unfamiliar repository?
13. Which tool would you trust most with autonomous file changes?
14. What additional instructions could improve the shared prompt?
15. What did this experiment teach you about the difference between an AI model and an AI coding harness?

---

## Lab Submission Requirements
Submit the following:
- A screenshot showing the installed version of all three tools.
- A completed setup record for Claude Code, Codex CLI, and Gemini CLI.
- The original shared prompt.
- The response produced by each tool.
- The completed comparison matrix.
- Your answers to the reflection questions.
- A screenshot of the final Git status.
- *Optional*: Git diffs from the three implementation branches.
- A short conclusion of approximately 200–300 words explaining which tool performed best for this repository and why.

---

## Troubleshooting Guide

### Command Not Found
If the terminal reports that `claude`, `codex`, or `gemini` cannot be found:
- Close and reopen the terminal.
- Confirm that the installation completed successfully.
- Check whether the global npm directory is included in your system `PATH`.
- Run the version command again.
- Reinstall using the native installer when available.

### npm Permission Error
Avoid using unrestricted administrator access unless required by your environment.

Possible solutions include:
- Using the provider's native installer
- Using a Node version manager
- Correcting the npm global package directory
- Using `npx` for Gemini CLI
- Using Homebrew on supported systems

### Browser Login Does Not Open
- Copy the authentication address shown in the terminal and open it manually in a browser.
- For remote or headless environments, API-key authentication may be easier than browser-based authentication.

### API Key Does Not Work
Confirm that:
- The environment variable name is correct.
- There are no extra quotation marks or spaces.
- The key belongs to the correct provider.
- Billing or quota access is available where required.
- The terminal was reopened after creating a persistent variable.
- The key has not been exposed or revoked.

### Agent Attempts to Modify Files
Decline the permission request and restate:
```text
Do not modify files. Perform analysis only.
```

Then check:
```bash
git status
```

Restore unintended changes:
```bash
git restore .
```

### Tests Fail Before the AI Comparison
Run:
```bash
npm install
npm test
```

Check that:
- `src/app.js` exports the Express application.
- The test imports `../src/app`.
- Jest is installed.
- Supertest is installed.
- The test script is configured correctly.

---

## Lab Conclusion
In this lab, you installed and evaluated three modern AI coding agents using the same repository and prompt. You observed that the underlying model is only one part of the experience. The surrounding harness—including repository access, command execution, permissions, planning behavior, context collection, authentication, and user interface—significantly affects the quality and safety of an AI-assisted coding workflow.

The goal is not to declare one universal winner. Different tools may perform better for different repositories, tasks, operating systems, account configurations, and engineering workflows. A professional Harness Engineer must know how to evaluate these differences systematically instead of relying only on brand names or isolated demonstrations.
