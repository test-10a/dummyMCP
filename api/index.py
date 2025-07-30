from fastapi import FastAPI, HTTPException
import os, anthropic
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional
app = FastAPI(
    title="Dummy MCP",
    version="0.1.0",
    openapi_version="3.1.0",
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

class ToolRequest(BaseModel):
    name: str
    arguments: Optional[Dict[str, Any]] = {}

class ToolResponse(BaseModel):
    content: str
    is_error: bool = False

@app.post("/tools/hello_claude")
async def hello_claude(request: ToolRequest) -> ToolResponse:
    return ToolResponse(content="🚀 Hello from Dummy MCP! I'm alive and well!")

@app.post("/tools/ask_claude")
async def ask_claude(request: ToolRequest) -> ToolResponse:
    if not client:
        return ToolResponse(content="Claude API key not configured", is_error=True)
    
    prompt = request.arguments.get("prompt")
    if not prompt:
        return ToolResponse(content="Missing 'prompt' argument", is_error=True)
    
    try:
        r = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=64,
            messages=[{"role": "user", "content": prompt}]
        )
        return ToolResponse(content=r.content[0].text)
    except Exception as e:
        return ToolResponse(content=f"Error calling Claude: {str(e)}", is_error=True)

from fastapi.responses import JSONResponse
from .mcp_manifest import MANIFEST

@app.get("/.well-known/mcp.json", include_in_schema=False)
async def manifest():
    return JSONResponse(MANIFEST)

@app.get("/openapi.json", include_in_schema=False)
async def openapi():
    return app.openapi()

