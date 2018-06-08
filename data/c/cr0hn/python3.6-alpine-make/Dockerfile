FROM python:3-alpine  
  
RUN apk update && apk upgrade && pip install -U pip  
RUN apk add --update alpine-sdk make gcc python3-dev python-dev libxslt-dev
libxml2-dev libc-dev openssl-dev libffi-dev zlib-dev py-pip \  
&& rm -rf /var/cache/apk/*  
  
RUN set -x \  
&& VER="17.03.0-ce" \  
&& curl -L -o /tmp/docker-$VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz \  
&& tar -xz -C /tmp -f /tmp/docker-$VER.tgz \  
&& mv /tmp/docker/* /usr/bin  

