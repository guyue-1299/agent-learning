import asyncio
import logging

import httpx

from .models import FetchResult

logger = logging.getLogger(__name__)


async def fetch(client: httpx.AsyncClient, url: str) -> FetchResult:
    loop = asyncio.get_running_loop()
    start = loop.time()
    logger.info("start fetch url=%s", url)
    try:
        resp = await client.get(url)
        result = FetchResult(
            url=url,
            status=resp.status_code,
            length=len(resp.content),
            elapsed=loop.time() - start,
        )
        logger.info(
            "done url=%s status=%s elapsed=%.3f",
            url,
            result.status,
            result.elapsed,
        )
        return result
    except httpx.HTTPError as exc:
        result = FetchResult(
            url=url,
            status=None,
            length=0,
            elapsed=loop.time() - start,
            error=str(exc),
        )
        logger.warning("failed url=%s error=%s", url, exc)
        return result


async def fetch_all(urls: list[str], timeout: float) -> list[FetchResult]:
    async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
        return await asyncio.gather(*(fetch(client, u) for u in urls))
