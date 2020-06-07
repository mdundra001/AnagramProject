FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY words .
COPY requirements.txt .
RUN pip install -qr requirements.txt
COPY backend  /usr/src/app/
CMD ["python3", "./application.py"]
