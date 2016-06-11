FROM python:2.7-alpine
MAINTAINER Manuel Sierra & Juan Carlos Pazos

EXPOSE 80

COPY requirements.txt requirements.txt
RUN apk --update add python py-pip openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies

ADD cyclone_server.py /root/server.py
RUN chmod +x /root/server.py

CMD python /root/server.py
