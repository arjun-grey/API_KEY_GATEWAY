import time 
import uuid


async def logging_middle(request , call_next):

    request_id = str(uuid.uuid4)

    start = time.perf_counter()
    
    request.state.request_id = request_id

    response = await request(call_next)

    processing_time = (
        time.perf_counter() - start
    )
    
    print(
        f"{request.method}"
        f" {request.url.path}"
        f" {response.status_code}"
        f" {processing_time:.4f}s"
    )

    request.headers[
        "X-Process-Time"
    ] = processing_time

    request.headers[
         "X-Request-ID"
    ] = request_id

