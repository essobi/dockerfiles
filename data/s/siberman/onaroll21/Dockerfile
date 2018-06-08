FROM alpine:3.2  
MAINTAINER Simon Berman <spb@siberman.com>  
RUN apk --update add git && mkdir -p /data/http && rm -rf /var/cache/apk/*  
COPY . /data/http  
VOLUME ["/data/http"]  
CMD ["true"]  

