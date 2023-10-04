FROM python:3.8-slim

WORKDIR /app

COPY word_count.py /app/
COPY text.txt /app/

RUN chmod +x word_count.py

CMD ["python", "/app/word_count.py"]
