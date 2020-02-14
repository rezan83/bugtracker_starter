"""Module to setup fastapi API to expose API to the outside world."""
import logging
import random
from typing import Any, Dict

from fastapi import Body, FastAPI
from starlette.middleware.cors import CORSMiddleware

import uvicorn


app = FastAPI(debug=True)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ERROR_CODES = [error_code for error_code in range(50)]
LOGGER = logging.getLogger("API")


def _generate_lists() -> Dict[str, Any]:
    """Generate resolved, unresolved and backlog lists."""
    return {
        'resolved': [{
            'id': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error ABC occured, that is `resolved`'
        } for error_idx in range(50)],
        'unresolved': [{
            'id': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error DEF occured, that is `unresolved`'
        } for error_idx in range(50, 100)],
        'backlog': [{
            'id': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error XYZ occured, that is in the `backlog`'
        } for error_idx in range(100, 150)]
    }


request_count = {}


@app.get("/get_lists/")
def get_lists(operator_name: str = "Rezan") -> Dict[str, Any]:
    """Return resolved, unresolved and backlog lists."""
    LOGGER.info('Generating resolved, unresolved and backlog lists.')
    global request_count
    if operator_name not in request_count:
        request_count[operator_name] = 0

    request_count[operator_name] += 1
    message = f"user: {operator_name}, has requested: {request_count[operator_name]} times"
    LOGGER.info(message)
    return _generate_lists()


@app.put("/put_resolved")
async def put_lists(resolved: Any = Body({"resolved": []})) -> Dict[str, Any]:
    resolved_codes = list(map(lambda x: x["code"], resolved["resolved"]))
    resolved_set = set(resolved_codes)
    for code in resolved_set:
        message = f"error code:{code} resolved {resolved_codes.count(code)} times"
        LOGGER.info(message)

    return resolved


@app.get("/get_list_intersection_counts")
def get_list_intersection_counts() -> Dict[str, int]:
    """Return the error intersection counts between a set of resolved, unresolved and backlog lists.
    """
    LOGGER.info(
        'Generating the intersection counts between a set of resolved, unresolved and backlog lists.')

    error_lists = _generate_lists()
    resolved, unresolved, backlog = error_lists['resolved'], error_lists['unresolved'], error_lists['backlog']

    # find intersections
    def list_intersection(list1, list2):
        set1 = set([x["code"] for x in list1])
        set2 = set([x["code"] for x in list2])
        return len(set1.intersection(set2))

    resolved_unresolved = list_intersection(resolved, unresolved)
    resolved_backlog = list_intersection(resolved, backlog)
    unresolved_backlog = list_intersection(unresolved, backlog)

    return {
        'resolved_unresolved': resolved_unresolved,
        'resolved_backlog': resolved_backlog,
        'unresolved_backlog': unresolved_backlog
    }


def run(host: str, port: int) -> None:
    """Run the code challenge API."""
    uvicorn.run(app, host=host, port=port)
