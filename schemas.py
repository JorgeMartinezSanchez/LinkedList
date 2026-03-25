from pydantic import BaseModel
from typing import Any

class NodeSchema(BaseModel):
    data: Any

class LinkedListResponse(BaseModel):
    name: str
    size: int
    elements: list