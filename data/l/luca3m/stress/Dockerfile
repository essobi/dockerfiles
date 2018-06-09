FROM alpine:edge  
MAINTAINER Luca Marturana <lucamarturana@gmail.com>  
RUN apk add stress --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && rm -fr
/var/cache/apk/*  
ENTRYPOINT [ "stress" ]  

