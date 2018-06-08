FROM alpine:latest  
MAINTAINER Jeremy Richard  
  
RUN apk --update add openssl wget \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir /output  
  
VOLUME /output  
  
WORKDIR /output  
  
ENTRYPOINT ["wget"]  

