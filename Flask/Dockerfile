FROM python:3.8-slim

WORKDIR /app

COPY word_count_flask.py text.txt /app/

RUN apt-get update && apt-get install -y vim && rm -rf /var/lib/apt/lists/* && chmod +x word_count_flask.py
RUN pip install gunicorn flask

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "word_count_flask:app"]
