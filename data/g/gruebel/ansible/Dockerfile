FROM python:2.7.14-alpine3.7  
  
ARG ANSIBLE_VERSION=2.4.3.0  
ARG BUILD_DATE  
  
LABEL org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.schema-version="1.0"  
# default region  
ENV AWS_DEFAULT_REGION=us-east-1  
  
RUN set -ex \  
&& apk add \--no-cache --virtual .run-deps \  
git \  
libffi \  
openssh-client \  
rsync \  
&& apk add \--no-cache --virtual .build-deps \  
gcc \  
libffi-dev \  
libressl-dev \  
make \  
musl-dev \  
&& pip install \  
ansible==${ANSIBLE_VERSION} \  
&& apk del .build-deps  
  
WORKDIR /root/ansible  

