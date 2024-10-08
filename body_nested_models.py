from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

offers = []

@app.post("/offers/")
async def create_offer(offer: Offer):
    offers.append(offer)
    return offer

@app.get("/offers/{offer_id}")
async def create_offer(offer_id: int):
    return offers[offer_id]