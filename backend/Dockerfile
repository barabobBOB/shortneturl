FROM --platform=linux/x86_64 python:3.8
#-> 여기도 두 주석의 위치
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend

WORKDIR /backend

ADD . /backend/

RUN pip3 install django