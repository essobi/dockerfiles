FROM alpine:3.7  
MAINTAINER KASKO Ltd, sysarch@kasko.io  
  
RUN apk --no-cache --update add bash curl less groff jq python py-pip && \  
pip install --no-cache-dir --upgrade pip && \  
pip install --no-cache-dir awscli==1.14.34 && \  
mkdir /root/.aws && \  
aws --version  
  
ENTRYPOINT []  

