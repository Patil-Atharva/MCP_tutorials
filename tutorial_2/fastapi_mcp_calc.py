from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
# pip install fastapi fastapi mcp uvicorn[standard]

# lets make a fastapi app first
app = FastAPI(title='Calculator API')

@app.post("/multiply")
def multiply(a: float, b: float):
    """Multiplies two numbers together and returns the result."""
    result = a * b
    return {"result": result}

@app.post("/divide")
def divide(a: float, b: float):
    """Divides the first number by the second and returns the result."""
    if b == 0:
        return {"error": "Cannot divide by zero."}
    result = a / b
    return {"result": result}

@app.post("/add")
def add(a: float, b: float):
    """Adds two numbers together and returns the result."""
    result = a + b
    return {"result": result}

@app.post("/subtract")
def subtract(a: float, b: float):
    """Subtracts the second number from the first and returns the result."""
    result = a - b
    return {"result": result}


mcp = FastApiMCP(app,name="Calculator MCP")
mcp.mount_http()
#python fastapi_mcp_calc.py

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8002)