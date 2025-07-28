from fastapi import FastAPI
import os, anthropic
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Dummy MCP",
    version="0.1.0",
    openapi_version="3.0.1",               # 🔧 3.0.x, not 3.1
    servers=[{
        "url": "https://dummy-mcp-sigma.vercel.app",
        "description": "Production"
    }],
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],)
CLAUDE_KEY = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Client(api_key=CLAUDE_KEY) if CLAUDE_KEY else None

@app.get("/")
async def root():
    print("🚀  Claude, I’m alive!")
    return {"msg": "🚀  Claude, I’m alive!"}

@app.post("/ask-claude")
async def ask(prompt: str):
    if not client:
        return {"error": "Claude key not set"}
    r = client.messages.create(
        model="claude-3-opus-2025-05-20",
        max_tokens=64,
        messages=[{"role": "user", "content": prompt}]
    )
    return {"claude_response": r.content[0].text}

from fastapi.responses import JSONResponse
from .mcp_manifest import MANIFEST

@app.get("/.well-known/mcp.json", include_in_schema=False)
async def manifest():
    return JSONResponse(MANIFEST)

