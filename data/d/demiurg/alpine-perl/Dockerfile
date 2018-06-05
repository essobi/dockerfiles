FROM alpine:edge  
MAINTAINER Demiurg (parserpro@gmail.com)  
  
RUN apk update && apk add perl perl-dev curl tar make gcc build-base ca-
certificates && update-ca-certificates && rm -fr /var/cache/apk/*  
  
RUN cd /bin && curl -L https://cpanmin.us/ -o cpanm && chmod +x cpanm  

