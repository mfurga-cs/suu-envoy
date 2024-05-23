FROM envoyproxy/envoy:v1.30.1

# install python
RUN apt update && \
	apt install -y --no-install-recommends python3 python3-pip

# install service.py and requirements
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./info.proto ./service.py /code/
RUN python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. info.proto

# start envoy in background (&)
# replace shell with python3 (exec, forward SIGTERM to python)
CMD ["/bin/bash", "-c", "envoy -c /envoy.yaml & exec python3 service.py"]
#CMD ["python3", "service.py"]
