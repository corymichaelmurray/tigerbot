FROM python:3.9.1-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "bot.py"]
