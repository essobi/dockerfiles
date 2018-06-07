FROM python:3.6-alpine3.6  
MAINTAINER Cybric, Inc.  
  
RUN apk add --update alpine-sdk curl-dev \  
openssl openssl-dev unzip  
  
RUN echo "http://mirror1.hs-esslingen.de/pub/Mirrors/alpine/edge/community" >>
/etc/apk/repositories  
RUN apk update && apk add docker  
  
RUN pip install awscli  
  
WORKDIR /app  
  
ADD Makefile /app  
ADD requirements.txt /app  
ADD setup.py /app  
  
RUN make docker_deps  
  
ADD . /app  
  
RUN make docker_install && apk del alpine-sdk \  
&& adduser -S cybric && chown -R cybric:nogroup /app  
  
RUN mkdir -p /code && mkdir -p /results && chown cybric:nogroup /results \  
&& chown cybric:nogroup /code  
  
# USER cybric  
VOLUME /code/  
VOLUME /results/  

