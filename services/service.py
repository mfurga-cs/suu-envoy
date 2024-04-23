#!/usr/bin/env python3

import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

import os
from fastapi import FastAPI, Request

SERVICE_NAME = os.environ.get("SERVICE_NAME", "?")

app = FastAPI()

@app.get(f"/{SERVICE_NAME}/endpoint-1")
async def endpoint1(request: Request):
  print(request)
  return {
    "service": SERVICE_NAME,
    "url": str(request.url),
    "ip": ip
  }

@app.get(f"/{SERVICE_NAME}/endpoint-2")
async def endpoint2(request: Request):
  return {
    "service": SERVICE_NAME,
    "url": str(request.url),
    "ip": ip
  }
