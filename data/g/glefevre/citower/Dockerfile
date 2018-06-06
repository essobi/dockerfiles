FROM jenkins:alpine  
  
MAINTAINER Guillaume Lefevre <gelefevre@octo.com>  
  
USER root  
  
RUN apk -Uuv add python py-pip gcc python-dev musl-dev libffi libffi-dev
openssl-dev groff py-boto && \  
pip install awscli ansible && \  
apk --purge -v del py-pip gcc && \  
rm -rf /var/cache/apk/*  
  
USER jenkins  

