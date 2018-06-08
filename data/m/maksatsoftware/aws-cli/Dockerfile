FROM alpine:latest  
  
MAINTAINER Maksat Annageldyev <maksat.annageldyev@maksat.software>  
  
RUN apk --update add python py-pip jq && pip install awscli && apk del py-pip
&& rm -rf /var/cache/apk/*  

