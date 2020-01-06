FROM python:3.7.3-alpine3.9

RUN mkdir -p /opt/app
WORKDIR /opt/app

RUN apk --update add --no-cache bash curl-dev python3-dev libressl-dev gcc libgcc curl musl-dev make libpq postgresql-dev mariadb-dev
RUN pip3 install --upgrade pip 

COPY requirements.txt ./
COPY Makefile ./
RUN pip install -r ./requirements.txt

ADD . ./
RUN chmod +x ./entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["sh", "/opt/app/entrypoint.sh"]