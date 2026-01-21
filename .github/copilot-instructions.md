# OctoFit Tracker Development Guide

## Project Overview

This is a learning workshop repo for building a fitness tracking app (OctoFit Tracker) using GitHub Copilot agent mode. The app helps students at Mergington High School track workouts, compete in teams, and earn achievements.

**Tech Stack:**
- Frontend: React.js (port 3000)
- Backend: Django REST Framework (port 8000)  
- Database: MongoDB (port 27017, local only)
- Environment: GitHub Codespaces

## Critical Project Structure

```
octofit-tracker/
├── backend/
│   ├── venv/              # Python virtual environment (DO NOT modify)
│   ├── octofit_tracker/   # Django project root
│   ├── manage.py
│   └── requirements.txt
└── frontend/              # React app
```

**Never change directories when running commands** - always use absolute paths or prefix commands with the directory path.

## Key Development Patterns

### Python Virtual Environment

Always activate the venv before Python operations:
```bash
source octofit-tracker/backend/venv/bin/activate
pip install -r octofit-tracker/backend/requirements.txt
```

All Django commands must run from within the activated venv. The `.vscode/launch.json` is pre-configured to use the venv Python interpreter.

### Django Backend Configuration

**settings.py** must include Codespaces hostname support:
```python
import os
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
if os.environ.get('CODESPACE_NAME'):
    ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")
```

**Database:** Use Django's ORM with Djongo connector - never write direct MongoDB scripts. Database name is `octofit_db` with collections for users, teams, activities, leaderboard, and workouts.

**CORS:** Configure to allow all origins in `settings.py` for development.

### React Frontend Setup

Install packages with `--prefix` to avoid directory changes:
```bash
npx create-react-app octofit-tracker/frontend --template cra-template --use-npm
npm install bootstrap react-router-dom --prefix octofit-tracker/frontend
```

Bootstrap CSS must be imported first in `src/index.js`.

### MongoDB Management

- Check service status: `ps aux | grep mongod`
- Use `mongosh` client (official tool, installed via post_create.sh)
- mongodb-org is the official package
- User collection requires unique index on `email` field
- Test data uses superhero themes (Team Marvel vs Team DC)

## Running the Application

**Launch from VS Code:**
- Backend: Use "Launch Django Backend" debug config
- Frontend: Use "Launch React Frontend" debug config  
- Or run both with compound launch (if configured)

**Port forwarding:** Ports 3000 and 8000 are public, 27017 is private (configured in devcontainer.json)

## Testing Workflows

Test REST API endpoints with curl:
```bash
curl http://localhost:8000/api/users/
```

In Codespaces, replace `localhost:8000` with `$CODESPACE_NAME-8000.app.github.dev`

## Custom Instructions & Prompts

The `.github/instructions/` directory contains scoped rules:
- `octofit_tracker_setup_project.instructions.md` - applies to all files (`**`)
- `octofit_tracker_django_backend.instructions.md` - applies to `octofit-tracker/backend/**`
- `octofit_tracker_react_frontend.instructions.md` - applies to `octofit-tracker/frontend/**`

The `.github/prompts/` directory contains agent mode task templates for complex workflows like creating the Django project and populating test data.

## Common Pitfalls

- **Do not** change directories with `cd` - use absolute paths or `--prefix`
- **Do not** create direct MongoDB scripts - use Django ORM and management commands
- **Do not** forward additional ports beyond 3000, 8000, 27017
- **Do not** create new Python virtual environments - use existing `octofit-tracker/backend/venv`
- **Do not** run Django without activating venv first
