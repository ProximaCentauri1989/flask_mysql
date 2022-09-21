FROM python:alpine3.11

ADD . /app
WORKDIR /app

RUN apk update && apk add build-base busybox-initscripts gcc python3-dev musl-dev mariadb-dev
RUN pip install -r ./requirements.txt && pip install waitress mysql-connector-python mysqlclient

CMD waitress-serve --port=5000 --call 'app:run_app'
