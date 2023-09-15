import asyncio
import aiohttp
import time

async def perform_concurrent_requests(api_endpoints, num_requests):
    async def make_request(session, endpoint):
        async with session.get(endpoint) as response:
            return response.status

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, endpoint) for endpoint in api_endpoints]
        responses = await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time

    return responses, total_time
