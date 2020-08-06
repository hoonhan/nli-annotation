FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir -p /backend
WORKDIR /backend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
