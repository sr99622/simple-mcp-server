from __future__ import annotations

from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("cowsay")

USER_AGENT = "cowsay-app/1.0"
VERSION = "0.0.1"

@mcp.tool()
async def get_cowsay_mcp_version() -> str:
    """
    Get the version of the cowsay application.

    Returns:
        The version string.
    """
    return VERSION

@mcp.tool()
async def get_cowsay_mcp_environment() -> str:
    """
    Collect information about the environment under which cowsay server is running
    
    Args:
        None

    Returns:
        A delimited string containing environment variable settings

    """

    output = []
    output.append(os.environ.get("COWSAY_USERNAME", "Empty $env:COWSAY_USERNAME"))
    output.append(os.environ.get("COWSAY_PASSWORD", "Empty $env:COWSAY_PASSWORD"))
    output.append(os.environ.get("STREAM_SERVER_IP", "Empty $env:STREAM_SERVER_IP"))
    output.append(os.environ.get("PATH", "Empty $env:PATH"))

    return "\n--\n".join(output)

@mcp.tool()
async def what_does_cowsay() -> str:
    """
    A simple tool that returns what the cow says

    Args:
        None

    Returns:
        What the cow says
    """
    return "The cow says moo"


def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()