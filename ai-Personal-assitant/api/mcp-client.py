from typing import Optional
from langchain_google_genai import GoogleGenerativeAI
from langchain_mcp_adapters import MCPAdapter
import langgraph
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import PromptReference, ResourceTemplateReference

class MCPClient:
    def __init__(self):
        self._stack = AsyncExitStack()
        self._client = stdio_client()
