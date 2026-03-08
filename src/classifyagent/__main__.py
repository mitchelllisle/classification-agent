"""CLI entrypoint for running the classification FastAPI app."""

import os

import uvicorn


def main() -> None:
    """Start the ASGI server for the classification agent."""
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run("classifyagent.app:app", host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
