# Module 8 · Deploying Your Agent to the Cloud

*Wrap your agent in a web API, containerize it with Docker, deploy it.*

## Three steps from demo to product

1. **FastAPI** turns your agent into a service that receives requests over the internet.
2. **Docker** packages the agent + Python + libraries into one portable container.
3. **Render.com** runs it constantly, giving it a real URL.

> A URL is the difference between a demo and a product.

## Install

```bash
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install fastapi uvicorn openai
export OPENAI_API_KEY='sk-...'
```

## Lab

1. Build [`agent_api.py`](agent_api.py) yourself.
2. Run it and test in the browser:

```bash
uvicorn agent_api:app --reload
# open http://localhost:8000/docs  → test /run-agent and /health
```

3. Create the [`Dockerfile`](Dockerfile) and [`requirements.txt`](requirements.txt). If you have Docker Desktop, build and run the container.
4. Push to a **public GitHub repo** — `agent_api.py`, `Dockerfile`, `requirements.txt`. Confirm `venv/` is in `.gitignore`. **Do not push `.env` or your API key.**

Once deployed on Render your agent has a URL like `https://my-agent.onrender.com`.

> **Security rule:** never put your API key in pushed code. On Render, set it in the
> dashboard — not in your code.
