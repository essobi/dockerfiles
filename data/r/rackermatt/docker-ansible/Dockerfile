FROM alpine:3.4  
MAINTAINER Matt George  
  
RUN apk --update add python py-pip openssl ca-certificates  
RUN apk --update add --virtual build-dependencies build-base python-dev
libffi-dev openssl-dev  
RUN pip install --upgrade pip && \  
pip install ansible==2.3.1.0  
RUN apk del build-dependencies && rm -rf /var/cache/apk/*  
CMD [ "ansible-playbook", "--version" ]  

