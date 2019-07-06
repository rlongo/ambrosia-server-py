FROM python:3.7-slim AS builder

COPY . /srv/flask_app
WORKDIR /srv/flask_app

RUN apt clean && \
    apt update && \
    apt install -y --no-install-recommends nginx python3-dev build-essential libpq-dev  && \
    pip install -r requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx

CMD ["./production.sh"]

