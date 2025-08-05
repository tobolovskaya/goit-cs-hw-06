FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask pymongo

CMD ["python", "socket_server.py"]
