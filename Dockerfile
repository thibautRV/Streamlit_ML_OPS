FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*


COPY . .

RUN pip install --upgrade pip setuptools

RUN pip install poetry && poetry install

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD ["poetry", "run", "streamlit", "run", "--server.port=8501", "--server.address=0.0.0.0", "app.py"]
