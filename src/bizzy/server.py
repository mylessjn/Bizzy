import logging
from mcp.server.fastmcp import FastMCP

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# If we want to send it to a file instead of console : logging.basicConfig(filename='bizzyserver.log', level=logging.INFO)

mcp = FastMCP("Bizzy Server", json_response=True)

# @mcp.resource need to implement live snapshots of the data that we'll be testing from

@mcp.tool()
def record_sale(item_sold: str, qty: int) -> str:
    """
    Record a sale and then deduct it from inventory for management
    
    Args: 
        item_sold: is the name of the item that was sold
        qty: is the number of units sold
        """
    return "Not yet implemented"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")

