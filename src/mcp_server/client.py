import asyncio

from fastmcp import Client

client = Client("http://127.0.0.1:8000/mcp")

async def get_tools_from_server():
    async with client:
        tools = await client.list_tools()

        for tool in tools:
            print(tool.name)

        return tools 

async def create_task_using_mcp():
    async with client:
        result = await client.call_tool(
            "create_task",
            {
                "title":"task3",
                "priority": "high",
                "description": "this is a test "
            }
        )
        print(result.data)
    return result.data

async def update_task_status_from_mcp():
    async with client:
        result = await client.call_tool(
            "update_task_status",
            {
                "task_id":"c20f559e-fe7a-477e-9551-34d48a56ce4c",
                "status":"todo",

            }
        )
        print(result.data)
    return result.data

async def list_tasks_using_mcp():
    async with client:
        result = await client.call_tool(
            "list_tasks"
        )
        print(result.data)
    return result.data

async def main():
    await get_tools_from_server()
    await list_tasks_using_mcp()
    await update_task_status_from_mcp()
    await list_tasks_using_mcp()

if __name__ == "__main__":
    asyncio.run(main())