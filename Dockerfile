FROM ubuntu:14.04

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install python-software-properties build-essential \
        python-dev wget git build-essential \
        libmysqlclient-dev libpq-dev libxml2-dev \
        libxslt1-dev swig libjpeg-dev libfreetype6-dev \
        zlib1g-dev libpng12-dev libmemcached-dev \
        libsqlite3-0 libsqlite3-dev wamerican \
        libffi-dev -yq && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/include/x86_64-linux-gnu/openssl/opensslconf.h /usr/include/openssl/opensslconf.h

RUN wget -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py && \
    python /tmp/get-pip.py && \
    rm /tmp/get-pip.py

ADD requirements.txt /temp-work/requirements.txt

RUN pip install -r //temp-work/requirements.txt && rm -rf /temp-work
