FROM alpine:latest  
MAINTAINER Mathieu Deous "mat.deous@gmail.com"  
# prepare environment  
ENV LANG=en_US LC_ALL=C  
EXPOSE 5000  
WORKDIR /opt/waikup  
RUN adduser -S uwsgi  
  
# install dependencies  
RUN apk --no-cache --update add \  
ca-certificates \  
python \  
py-pip \  
uwsgi \  
uwsgi-python \  
postgresql-client && \  
apk --no-cache --update add --virtual build-dependencies \  
build-base \  
libffi-dev \  
libressl-dev \  
postgresql-dev \  
python-dev \  
wget  
  
# install dockerize  
ENV DOCKERIZE_VERSION=v0.6.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-$DOCKERIZE_VERSION.tar.gz && \  
rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# copy application  
ADD . /opt/waikup  
  
# install application dependencies  
RUN pip install pipenv && \  
pipenv install  
  
# cleanup  
RUN rm -rf /opt/waikup/.git && \  
apk del build-dependencies && \  
rm -rf ~/.cache/pip  
  
# startup script  
CMD ["/bin/sh", "/opt/waikup/docker/entrypoint.sh"]  

