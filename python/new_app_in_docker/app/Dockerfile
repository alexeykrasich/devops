FROM python:3.9

WORKDIR /app

COPY REQUIREMENTS ./

RUN pip install -r REQUIREMENTS

COPY app.py ./

ENTRYPOINT ["python3", "app.py"]