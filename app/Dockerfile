FROM python:3.9-slim-buster
COPY . /app
ARG SHORT_HASH
ENV GIT_COMMIT_HASH=$SHORT_HASH
WORKDIR /app
RUN pip install flask redis
RUN echo git commit hash: ${GIT_COMMIT_HASH}
EXPOSE 5000
CMD ["python", "/app/app.py"]
