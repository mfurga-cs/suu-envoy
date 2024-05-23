#!/usr/bin/env python3

import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

import os
from fastapi import FastAPI, Request

import psycopg2
conn = psycopg2.connect(
  database="envoy",
  host="127.0.0.1",
  user="envoy",
  password="envoy",
  port="5432")
cursor = conn.cursor()

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


@app.get(f"/{SERVICE_NAME}/dbquery")
async def endpoint2(request: Request):
  cursor.execute("SELECT * FROM cars;")
  return {
    "service": SERVICE_NAME,
    "url": str(request.url),
    "ip": ip,
    "db": cursor.fetchall()
  }
