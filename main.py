from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()
stack = []  # Ceci est la pile utilisée pour la calculatrice RPN

@app.get("/stack", response_model=List[float])
def get_stack():
    """Récupère l'état actuel de la pile."""
    return stack

@app.post("/push/{value}")
def push_value(value: float):
    """Ajoute un élément à la pile."""
    stack.append(value)
    return {"message": "Value added", "stack": stack}

@app.post("/pop")
def pop_value():
    """Retire le dernier élément de la pile."""
    if not stack:
        raise HTTPException(status_code=404, detail="Stack is empty")
    return stack.pop()

@app.post("/clear")
def clear_stack():
    """Nettoie la pile."""
    stack.clear()
    return {"message": "Stack cleared"}

@app.post("/add")
def add():
    """Effectue l'opération d'addition."""
    if len(stack) < 2:
        raise HTTPException(status_code=400, detail="Not enough elements in stack")
    a, b = stack.pop(), stack.pop()
    result = a + b
    stack.append(result)
    return {"result": result, "stack": stack}

@app.post("/subtract")
def subtract():
    """Effectue l'opération de soustraction."""
    if len(stack) < 2:
        raise HTTPException(status_code=400, detail="Not enough elements in stack")
    a, b = stack.pop(), stack.pop()
    result = a - b
    stack.append(result)
    return {"result": result, "stack": stack}

@app.post("/multiply")
def multiply():
    """Effectue l'opération de multiplication."""
    if len(stack) < 2:
        raise HTTPException(status_code=400, detail="Not enough elements in stack")
    a, b = stack.pop(), stack.pop()
    result = a * b
    stack.append(result)
    return {"result": result, "stack": stack}

@app.post("/divide")
def divide():
    """Effectue l'opération de division."""
    if len(stack) < 2:
        raise HTTPException(status_code=400, detail="Not enough elements in stack")
    a, b = stack.pop(), stack.pop()
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    result = a / b
    stack.append(result)
    return {"result": result, "stack": stack}
