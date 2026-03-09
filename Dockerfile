FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    --no-install-recommends build-essential ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir .

RUN mkdir -p /app/data/sessions /app/jobs
RUN printf '[]\n' > /app/data/clients.json

CMD ["telekit", "start-program"]
