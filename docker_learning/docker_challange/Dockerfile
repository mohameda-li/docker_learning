FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install flask redis && pip install -r requirements.txt

EXPOSE 5002

CMD ["python", "app.py"]
