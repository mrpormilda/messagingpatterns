from fastapi import FastAPI
from pydantic import BaseModel
from rabbitmq import publish_message

app = FastAPI()

class PublishRequest(BaseModel):
    routing_key: str
    message: str

@app.post("/publish")
def publish(req: PublishRequest):
    publish_message(req.routing_key, req.message)
    return {"status": "Message published", "routing_key": req.routing_key, "message": req.message}

