FROM python:2.7

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./app/requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY ./app/* /usr/src/app/
RUN chmod +x /usr/src/app/app.py
ENTRYPOINT ["/usr/src/app/app.py"]
