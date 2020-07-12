FROM ubuntu:latest
EXPOSE 80
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip \
    libpq-dev
ADD requirements.txt /app/
RUN pip3 install -r /app/requirements.txt
ADD . /app
WORKDIR /app
