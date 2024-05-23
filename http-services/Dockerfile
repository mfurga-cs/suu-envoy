FROM envoyproxy/envoy:v1.30.1

# install python
RUN apt update && \
	apt install -y --no-install-recommends python3 python3-pip

# install service.py and requirements
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./service.py /code/

# start envoy in background (&)
# replace shell with uvicorn (exec, forward SIGTERM to uvicorn)
# listen both on v4 and v6
CMD ["/bin/bash", "-c", "envoy -c /envoy.yaml & exec uvicorn service:app --host 127.0.0.1 --host ::1 --port 20000"]
