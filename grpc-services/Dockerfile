FROM python:3.11
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./info.proto ./service.py /code/
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. info.proto

CMD ["python", "service.py"]
