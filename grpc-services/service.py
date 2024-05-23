#!/usr/bin/env python3

import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

import os
SERVICE_NAME = os.environ.get("SERVICE_NAME", "?")
PATH = "localhost:20000"

import sys # for stdout flush
import signal

# faster shutdown
def sigterm():
    sys.exit(0)
signal.signal(signal.SIGTERM, sigterm)

import grpc
import info_pb2_grpc
import info_pb2
from concurrent import futures

class Test1Servicer(info_pb2_grpc.Test1Servicer):
    def Info1(self, request, context):
        return info_pb2.InfoResult(
            name=SERVICE_NAME,
            ip=ip)

class Test2Servicer(info_pb2_grpc.Test2Servicer):
    def Info2(self, request, context):
        return info_pb2.InfoResult(
            name=SERVICE_NAME,
            ip=ip)

class Test3Servicer(info_pb2_grpc.Test3Servicer):
    def Info3(self, request, context):
        return info_pb2.InfoResult(
            name=SERVICE_NAME,
            ip=ip)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    if SERVICE_NAME == "Test1":
        info_pb2_grpc.add_Test1Servicer_to_server(Test1Servicer(), server)

    elif SERVICE_NAME == "Test2":
        info_pb2_grpc.add_Test2Servicer_to_server(Test2Servicer(), server)

    elif SERVICE_NAME == "Test3":
        info_pb2_grpc.add_Test3Servicer_to_server(Test3Servicer(), server)
        
    else:
        raise KeyError("no such service")
    
    print(f"Starting service {SERVICE_NAME} at {PATH}")
    sys.stdout.flush()
    
    server.add_insecure_port(PATH)
    server.start()
    server.wait_for_termination()


serve()
