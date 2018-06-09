FROM python:2.7.14-alpine3.6  
ENV ANSIBLE_VERSION 2.4.0.0  
RUN apk --no-cache update && \  
apk --no-cache add build-base python-dev openssl-dev libffi-dev && \  
pip install ansible==${ANSIBLE_VERSION}  
  
CMD [ "ansible --version" ]

