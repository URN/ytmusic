FROM python:3.8-alpine
WORKDIR /app
RUN apk add --no-cache ffmpeg; mkdir -p /out

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8888
CMD ["python", "main.py"]