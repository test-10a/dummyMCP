#!/usr/bin/env python3
import requests
import json
import base64

# Test data
test_content = "Hello, this is a test file content that will be compressed. " * 100
test_filename = "test_file.txt"

# Encode content to base64
encoded_content = base64.b64encode(test_content.encode()).decode()

# MCP server endpoint
url = "http://localhost:8000/mcp"

# Test gzip compression
print("Testing gzip compression...")
gzip_request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
        "name": "compress_file",
        "arguments": {
            "content": encoded_content,
            "filename": test_filename,
            "format": "gzip"
        }
    }
}

response = requests.post(url, json=gzip_request)
print(f"Response status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

print("\n" + "="*50 + "\n")

# Test zip compression
print("Testing zip compression...")
zip_request = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "compress_file",
        "arguments": {
            "content": encoded_content,
            "filename": test_filename,
            "format": "zip"
        }
    }
}

response = requests.post(url, json=zip_request)
print(f"Response status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")