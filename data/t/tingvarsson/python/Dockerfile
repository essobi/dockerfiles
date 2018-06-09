# Python  
#  
# Version 3.1.0  
FROM alpine:3.4  
MAINTAINER Thomas Ingvarsson <ingvarsson.thomas@gmail.com>  
  
RUN apk add \--no-cache python3 python3-dev && \  
apk add \--no-cache \--virtual=build-dependencies wget ca-certificates && \  
wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python3 && \  
apk del build-dependencies

