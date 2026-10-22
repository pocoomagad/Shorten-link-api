FROM python:alpine3.14

WORKDIR /url-shortener-app

RUN apk update -y \
    && apk upgrade \
    && apk add poetry 

RUN poetry config virtualenvs.create false

COPY pyproject.toml poerty.lock* ./

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "run", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]