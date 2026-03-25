from fastapi import APIRouter, HTTPException
from LinkedListClasses.Node import Node
from LinkedListClasses.LinkedList import LinkedList
from schemas import NodeSchema, LinkedListResponse
from storage import lists

router = APIRouter()

def ll_to_response(name: str) -> LinkedListResponse:
    ll = lists[name]
    elements = []
    current = ll.first
    while current is not None:
        elements.append(current.getData())
        current = current.getNext()
    return LinkedListResponse(name=name, size=ll.size(), elements=elements)


@router.post("/lists/{name}", status_code=201)
def create_list(name: str):
    if name in lists:
        raise HTTPException(status_code=409, detail=f"'{name}' already exists")
    lists[name] = LinkedList()
    return {"message": f"LinkedList '{name}' created"}


@router.get("/lists/{name}", response_model=LinkedListResponse)
def get_list(name: str):
    if name not in lists:
        raise HTTPException(status_code=404, detail="List not found")
    return ll_to_response(name)


@router.post("/lists/{name}/insert")
def insert_node(name: str, node: NodeSchema):
    if name not in lists:
        raise HTTPException(status_code=404, detail="List not found")
    lists[name].insert(Node(node.data))
    return ll_to_response(name)


@router.delete("/lists/{name}/delete")
def delete_node(name: str, node: NodeSchema):
    if name not in lists:
        raise HTTPException(status_code=404, detail="List not found")
    deleted = lists[name].delete(node.data)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Node '{node.data}' not found")
    return ll_to_response(name)


@router.post("/lists/{name}/search")
def search_node(name: str, node: NodeSchema):
    if name not in lists:
        raise HTTPException(status_code=404, detail="List not found")
    found = lists[name].search(node.data)
    if found is None:
        raise HTTPException(status_code=404, detail=f"Node '{node.data}' not found")
    return {"found": True, "data": found.getData()}


@router.delete("/lists/{name}")
def delete_list(name: str):
    if name not in lists:
        raise HTTPException(status_code=404, detail="List not found")
    del lists[name]
    return {"message": f"LinkedList '{name}' deleted"}