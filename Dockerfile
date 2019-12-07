FROM python:3-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk --update add python py-pip openssl ca-certificates py-openssl wget bash linux-headers
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip3 install --upgrade pip \
  && pip3 install --upgrade pipenv\
  && pip3 install --upgrade -r /app/requirements.txt\
  && apk del build-dependencies

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "hello.py" ]