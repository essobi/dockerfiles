FROM alpine:3.4  
  
MAINTAINER Zoltan Burgermeiszter <zoltan@burgermeiszter.com>  
  
RUN addgroup -g 1000 user && \  
adduser -D -u 1000 -G user -s /bin/ash user  
  
USER user  
  
WORKDIR "/home/user"

