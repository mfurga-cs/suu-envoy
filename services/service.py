#!/usr/bin/env python3

import os
from fastapi import FastAPI, Request

SERVICE_NAME = os.environ.get("SERVICE_NAME", "?")

app = FastAPI()

@app.get("/endpoint1")
async def endpoint1(request: Request):
  print(request)
  return {
    "service": SERVICE_NAME,
    "url": str(request.url)
  }

@app.get("/endpoint2")
async def endpoint2(request: Request):
  return {
    "service": SERVICE_NAME,
    "url": str(request.url)
  }
