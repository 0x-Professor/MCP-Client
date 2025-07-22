from typing import Optional
from langchain_google_genai import GoogleGenerativeAI
import langchain_google_genai
from langchain_mcp_adapters import MCPAdapter
import langgraph
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import PromptReference, ResourceTemplateReference
import json
import os

class MCPClient:
    def __init__(self):
        self._stack = AsyncExitStack()
        self._client = stdio_client()
        self.session: Optional[ClientSession] = None
        self.exit_stack: Optional[AsyncExitStack] = None
        self.tools = []
        self.messages = []
        self.llm = langchain_google_genai.GoogleGenerativeAI
        self.model = "gemini-2.0-flash-exp"
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.llm = self.llm(api_key=self.api_key, model=self.model)
        self.adapter = MCPAdapter(self.llm)
        self.graph = langgraph.Graph(self.adapter)
        self.graph.add_node("llm", self.llm)
        self.graph.add_edge("llm", "output", "output")

#connect to the MCP Server



