# convenience gnuplot  
FROM alpine:3.3  
MAINTAINER Ivo Jimenez "ivo.jimenez@gmail.com"  
# Make sure we are up-to-date  
RUN apk add --update gnuplot --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing && rm -rf /var/cache/apk/*  
  
VOLUME /document  
WORKDIR /document  
ENTRYPOINT ["gnuplot"]  

