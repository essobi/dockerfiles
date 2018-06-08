FROM python:2.7-alpine  
MAINTAINER Dmitry Malinovsky <dmitry@malinovsky.me>  
  
RUN apk update \  
&& apk add build-base libffi-dev openssl-dev sshpass \  
&& rm -rf /var/cache/apk/*  
  
ENV ANSIBLE_VERSION=2.2.1.0  
RUN pip install -U --no-cache-dir pip \  
&& pip install --no-cache-dir ansible==$ANSIBLE_VERSION  
  
CMD ["/bin/sh"]  

