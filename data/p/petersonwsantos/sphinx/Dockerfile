FROM alpine:3.5  
MAINTAINER Peterson W. Santos <opeterson@hotmail.com>  
  
WORKDIR /doc  
  
COPY ./requiriments.txt /doc/requiriments.txt  
  
RUN apk add --no-cache --virtual --update py-pip make wget ca-certificates
ttf-dejavu openjdk8-jre graphviz && \  
pip install --upgrade pip && \  
pip install -r requiriments.txt  

