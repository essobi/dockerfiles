FROM openjdk:8-jdk-alpine  
  
LABEL VERSION=1.0.0  
  
RUN apk --update add make bash jq python py-pip openssl ca-certificates && \  
apk --update add \--virtual build-dependencies \  
python-dev libffi-dev openssl-dev build-base && \  
pip install --upgrade pip cffi virtualenv setuptools awscli && \  
pip install ansible && \  
pip install --upgrade pywinrm && \  
apk --update add sshpass openssh-client rsync && \  
rm -rf /var/cache/apk/*  

