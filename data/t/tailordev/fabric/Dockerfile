FROM tailordev/rsync:latest  
MAINTAINER TailorDev <hello@tailordev.fr>  
  
RUN apk update && \  
apk add openssh python2 git py-pip openssl && \  
apk --update add --virtual build-dependencies openssl-dev python-dev libffi-
dev build-base && \  
pip install --upgrade fabric && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk/*  

