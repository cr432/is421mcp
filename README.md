# MCP Toolbox

A simple AI-powered toolbox with 3 demo tools connected via a Flask backend and HTML frontend.

## Setup Instructions

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Add your OpenAI API key to `.env` (copy `.env.example`):

```bash
cp .env.example .env
```

3. Start the server:

```bash
cd backend
flask run
```

4. Open `frontend/index.html` in your browser.