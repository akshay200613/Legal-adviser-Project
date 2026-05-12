import asyncio
from fastapi import APIRouter, Depends, Query
from fastapi.responses import StreamingResponse
from fastapi_limiter.depends import RateLimiter
from app.core.deps import get_current_user, RoleChecker
from app.models.user import User

router = APIRouter()

# RBAC: Only 'user' or 'admin' can access legal advice
allow_legal_access = RoleChecker(["user", "admin", "legal_expert"])

async def mock_legal_advice_stream(query: str):
    """
    Simulates a streaming response from an LLM.
    """
    responses = [
        f"Analyzing your query: {query}\n",
        "Searching relevant legal statutes...\n",
        "Found match in Section 42 of the Civil Code.\n",
        "Legal Recommendation: Consult with a licensed attorney for specific advice.\n",
        "Done."
    ]
    for chunk in responses:
        yield chunk
        await asyncio.sleep(0.5)

@router.get("/advice/stream", dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def get_legal_advice_stream(
    query: str = Query(..., min_length=5),
    current_user: User = Depends(allow_legal_access)
):
    """
    Streaming AI legal advice endpoint with RBAC and Rate Limiting.
    """
    return StreamingResponse(
        mock_legal_advice_stream(query),
        media_type="text/event-stream"
    )
