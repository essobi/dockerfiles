FROM alpine:edge  
  
COPY fabfile.py /  
  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
RUN apk add --no-cache openssh-client curl fabric  
  

