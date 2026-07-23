<h2>MCP Server Example</h2>

This example shows how to add an MCP server installed on Claude Desktop. It uses the UV runtime, so you will need to have uv installed on your system.

To create the installer, you need the CLI tool from Anthropic

```
npm install -g @anthropic-ai/mcpb
```

Then run the command

```
mcpb pack
```

There will now be a simple-mcp-server.mcpb file in the repository. Open Claude Desktop and use the hamburger icon in the upper left corner to open the File -> Settings menu and select Extensions from the left side panel. Click the `Advanced Settings` then click the `Install Extension` button to open a file selection dialog. Navigate to the repository and select the simple-mcp-server.mcpb file and the MCP server installer will present a dialog to be filled out with site parameters. The username, password and server settings are for reference only and do not have any effect on the server. After the installation is complete, the MCP server will be available to the agent. Full details at [mcpb](https://github.com/modelcontextprotocol/mcpb). 

You can check the server functionality by asking the agent

```
Please show the cowsay mcp server version
```

and the agent should reply with the version 0.0.1, then ask the agent

```
what does the cow say
```

and the reply should be "The cow says moo"

You can check the environment variables by asking the agent

```
Please show the cowsay mcp server environment
```