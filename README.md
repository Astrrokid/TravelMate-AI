# TripMate AI — A Multi-Agent Travel Planner with LangGraph

An open-source AI travel planner that turns a natural-language trip request into a practical travel plan with flight suggestions, hotel ideas, and a day-by-day itinerary. The project uses a multi-agent workflow built with LangGraph, LangChain, and FastAPI.

## Why this project?

Planning a trip usually means jumping between multiple websites, tools, and spreadsheets. This project brings that flow into one experience by combining:

- a flight-search agent,
- a hotel-research agent,
- an itinerary-planning agent, and
- a final response agent,

all coordinated through a LangGraph workflow.

## Features

- ✈️ Flight research using AviationStack
- 🏨 Hotel suggestions using Tavily search
- 🧠 Multi-agent orchestration with LangGraph
- 📝 Structured travel itinerary generation
- 🌐 FastAPI backend with a simple web interface
- 💾 Conversation state persistence using PostgreSQL
- ⚡ LLM-powered responses with Groq

## Tech Stack

- Python 3.11+
- FastAPI
- Jinja2 + HTML/CSS/JavaScript frontend
- LangGraph
- LangChain
- Groq LLMs
- PostgreSQL
- Tavily API
- AviationStack API

## Project Structure

```text
.
├── app.py                # FastAPI app entry point
├── backend.py            # LangGraph travel workflow
├── requirements.txt      # Python dependencies
├── static/               # Static frontend assets
├── templates/            # HTML templates
└── tools/                # Flight and web search integrations
```

## Prerequisites

Before running the project locally, make sure you have:

- Python 3.11 or newer (the project pins Python 3.11 in `.python-version`)
- PostgreSQL running and accessible
- API keys for:
  - Groq
  - Tavily
  - AviationStack

## Environment Variables

Create a .env file in the project root with the following variables:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/travel_db
GROQ_API_KEY=your_groq_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
TAVILY_API_KEY=your_tavily_api_key
DEFAULT_ORIGIN_IATA=DAC
```

## Installation

Run the following commands from the project root.

### Using uv

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if it is not already available:

```bash
python -m pip install uv
```

Create the virtual environment and install the locked dependencies:

```bash
uv sync --locked
```

This creates `.venv` using the Python version in `.python-version` and installs dependencies from `pyproject.toml` and `uv.lock`. uv downloads Python if the requested version is unavailable. You do not need to activate the environment when using `uv run`.

### Using pip

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the App

Start the FastAPI server:

With uv:

```bash
uv run --locked python app.py
```

With pip (after activating `.venv`):

```bash
python app.py
```

Then open your browser at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

- GET /health - Health check
- POST /api/travel - Submit a travel request

Example request:

```bash
curl -X POST http://127.0.0.1:8000/api/travel \
  -H "Content-Type: application/json" \
  -d '{"message":"Plan a 3-day trip to Tokyo with a budget of $1200"}'
```

## How the Workflow Works

1. The user submits a travel request.
2. The flight agent gathers flight-related information.
3. The hotel agent searches for accommodation suggestions.
4. The itinerary agent creates a practical travel plan.
5. The final agent formats the result into a polished response.

## Contributing

Contributions are welcome. If you want to improve the app, add new travel features, or fix issues:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Open a pull request

## Acknowledgments

This project is built with the help of modern LLM tooling and travel APIs, and it is intended as a practical example of combining LangGraph agents with real-world applications.
