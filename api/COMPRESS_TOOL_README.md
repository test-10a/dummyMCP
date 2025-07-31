# File Compression Tool for Dummy MCP

The `compress_file` tool has been added to the dummy-mcp server to provide file compression capabilities.

## Tool Details

### Name
`compress_file`

### Description
Compress file content using gzip or zip format

### Parameters

1. **content** (required)
   - Type: string
   - Description: The base64-encoded content to compress
   
2. **filename** (required)
   - Type: string
   - Description: The filename for the compressed content
   
3. **format** (optional)
   - Type: string
   - Values: "gzip" or "zip"
   - Default: "gzip"
   - Description: The compression format to use

### Response

The tool returns:
- Success message with compression statistics
- Original size in bytes
- Compressed size in bytes
- Compression ratio as percentage
- Output filename (with .gz or .zip extension)
- Base64-encoded compressed content

### Example Usage

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "compress_file",
    "arguments": {
      "content": "SGVsbG8sIFdvcmxkIQ==",
      "filename": "hello.txt",
      "format": "gzip"
    }
  }
}
```

### Error Handling

The tool handles the following errors:
- Missing required arguments (content or filename)
- Invalid base64 content
- Unsupported compression format
- General compression errors

## Testing

Run the test script to verify the compression tool:

```bash
python test_compress.py
```

Note: Make sure the MCP server is running locally on port 8000 before running the test.