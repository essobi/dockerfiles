FROM alpine:3.4  
MAINTAINER Steeve Morin "steeve@zen.ly"  
RUN apk add \--update build-base python python-dev openssl openssl-dev libffi
libffi-dev curl zip unzip && \  
curl https://bootstrap.pypa.io/get-pip.py | python \- && \  
pip install isign && \  
pip uninstall -y pip setuptools wheel && \  
apk del build-base python-dev openssl-dev libffi-dev curl && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/isign"]  

