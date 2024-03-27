# get the base image
FROM python:3.11-slim
RUN pip install pipenv

ENV PROJECT_DIR /app
COPY . /${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}

RUN pipenv install --system --deploy

EXPOSE 8080
CMD ["python", "app.py"]
