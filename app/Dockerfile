FROM python:3.9-slim-buster
COPY . /app
WORKDIR /app
RUN pip install flask redis
EXPOSE 5000
CMD ["python", "/app/app.py"]
