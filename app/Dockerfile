FROM python:3.10-slim

EXPOSE 80

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD python app.py