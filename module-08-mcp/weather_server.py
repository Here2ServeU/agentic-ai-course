# Module 8 · weather_server.py — your first MCP server.
# Install: pip install "mcp[cli]" openai     (Python 3.11 required)
# Run:     python3 weather_server.py
# The server starts and waits quietly until an agent connects.

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")


@mcp.tool()
def get_forecast(city: str) -> str:
    """Get today's weather forecast for a city."""
    fake_weather = {
        "chicago": "Sunny, 72 degrees, light wind.",
        "miami": "Cloudy, 86 degrees, chance of rain.",
        "sioux falls": "Clear, 74 degrees, dry.",
        "dallas": "Clear, 94 degrees, dry.",
    }
    return fake_weather.get(city.lower(), "No forecast available for that city.")


if __name__ == "__main__":
    mcp.run()
