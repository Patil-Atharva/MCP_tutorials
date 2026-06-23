from fastmcp import FastMCP


mcp = FastMCP(name = 'Calculator')

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers
    
    Args:
        a (float): The first number
        b (float): The second number

    returns:
        float: The product of the two numbers
    """
    return a * b

@mcp.tool(
    name = 'add',
    description = 'Add two numbers',
    tags = ['math', 'addition','arithmetic']
)
def add_numbers(a: float, b: float) -> float:
    """Add two numbers
    
    Args:
        a (float): The first number
        b (float): The second number

    returns:
        float: The sum of the two numbers
    """
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract two numbers
    
    Args:
        a (float): The first number
        b (float): The second number

    returns:
        float: The difference of the two numbers
    """
    return a - b

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide two numbers
    
    Args:
        a (float): The first number
        b (float): The second number

    returns:
        float: The quotient of the two numbers
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__": 
    mcp.run() #STDIO by default 
    #mcp.run(transport="http",host="localhost",port=8003)

# npx @modelcontextprotocol/inspector python fastmcp_calc.py