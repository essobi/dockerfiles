FROM python:2-alpine  
  
RUN apk update \  
&& apk add ffmpeg \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY . /usr/src/app  

