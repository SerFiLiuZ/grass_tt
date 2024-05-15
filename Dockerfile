FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "tasks.main:app", "--host", "0.0.0.0", "--port", "8000"]
