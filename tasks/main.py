import uvicorn
import json
from fastapi import FastAPI
from tasks.router import router as task_router

with open("config.json") as config_file:
    config = json.load(config_file)

app = FastAPI()

app.include_router(task_router)

if __name__ == '__main__':
    uvicorn.run(app, host=config['host'], port=config['port'])
