MANIFEST = {
    "schema_version": "v1",
    "name_for_human": "Dummy MCP",
    "name_for_model": "dummy_mcp",
    "description_for_human": "Tiny demo that either greets or forwards a prompt to Claude.",
    "description_for_model": (
        "Tools:\n"
        "• hello_claude() → returns greeting\n"
        "• ask_claude(prompt: str) → returns Claude’s reply\n"
    ),
    "auth": {"type": "none"},
    "contact_email": "your@email.com",
    "legal_info_url": "https://github.com/<you>/mcp-demo/blob/main/LICENSE",
    "api": {
        "type": "openapi",
        "url": "/openapi.json"          # 🔧 RELATIVE path
    }
}

