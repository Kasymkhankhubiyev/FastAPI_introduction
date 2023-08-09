from fastapi import FastAPI

from todo import todo_router
from model import Todo

# to run a server run in cmd: (venv) uvicorn file_name:app --port 8000 --reload

# if __name__ == '__main__':
    
app = FastAPI()

# a '/' route only accepts "GET" requests and returns a message
@app.get('/')
async def welcome() -> dict:
    return {'message': 'Hello World'}

app.include_router(todo_router)
    
