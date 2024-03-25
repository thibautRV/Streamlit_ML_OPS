FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . .

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Install Poetry and use Python 3.9
RUN pip install poetry && poetry env use python3.11 && poetry install

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Set STREAMLIT_SERVER_WATCH environment variable to 0
ENV STREAMLIT_SERVER_WATCH 0

CMD ["poetry", "run", "streamlit", "run", "--server.port=8501", "--server.address=0.0.0.0", "app.py"]
