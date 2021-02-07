FROM python:3.9.1-buster

WORKDIR /app

COPY bot/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "bot.py"]
