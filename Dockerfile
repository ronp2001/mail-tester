FROM python:3.9.20-alpine3.19


WORKDIR /app


COPY . /app


CMD ["python", "send_emails.py"]
