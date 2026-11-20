from typing import Literal
from uuid import uuid4

from fastmcp import FastMCP
from mcp_server.database import (
    get_all_tasks,
    save_task,
    update_task_status_in_db
)

mcp = FastMCP("MCP Server")

@mcp.tool(name="create_task", description="This tool is created to create new task")
def create_task(title:str, priority: str="medium", description:str="") -> dict:
    """
    this function creates new task
    """
    task_id = str(uuid4())
    status = "todo"

    task = {"task_id":task_id, "title":title, 
            "description":description, "status":status, "priority":priority}

    save_task(task)
    return task

@mcp.tool(name="list_tasks", description="this tool provides all list of tasks in our databases")
def list_tasks() -> list[dict]:
    """
    This function returns all the tasks in our database
    """
    return get_all_tasks()

@mcp.tool(name="update_task_status", description="this tool will update a task status based on its ID")
def update_task_status(task_id:str, status:Literal['todo',"in progress", "done"]) -> dict:
    """
    this function will update status of a specific task based on its ID
    """
    return update_task_status_in_db(task_id, status)


if __name__=="__main__":
    mcp.run(transport="http", port = 8000)
    create_task(title="this is second task", description="this is a test")