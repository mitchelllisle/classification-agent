from fastapi import FastAPI, HTTPException

from classifyagent import __version__
from classifyagent.config import Settings
from classifyagent.models import RunRequest
from classifyagent.service import ClassificationService

# Validate required configuration during app import/startup.
settings = Settings()

app = FastAPI(title="Classification Agent", version=__version__)


@app.get("/health")
def health() -> dict[str, str]:
    """Return service health metadata.

    Returns:
        dict[str, str]: Health status and package version.
    """
    return {"status": "ok", "version": __version__}


@app.post("/run")
def run(request: RunRequest) -> dict:
    """Classify each payload item using the classification service.

    Args:
        request: Request body containing payload items to classify.

    Returns:
        dict: Serialized classification response.

    Raises:
        HTTPException: Raised with status 502 when upstream model calls fail.
    """
    service = ClassificationService()
    try:
        result = service.run(request.payload)
    except Exception as exc:
        # Surface upstream model failures to callers in a structured way.
        raise HTTPException(
            status_code=502,
            detail=f"{type(exc).__name__}: {exc}",
        ) from exc

    return result.model_dump(exclude_none=True)
