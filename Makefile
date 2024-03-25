prepare:
    poetry config virtualenvs.prefer-active-python true
    poetry config virtualenvs.in-project true
    poetry install --no-root
run:
    poetry run streamlit run app.py
check:
    vulture . && isort . && black . && mypy .
build:
    docker build -t myapp .
push:
    docker push myapp
deploy:
    