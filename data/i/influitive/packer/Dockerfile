FROM hashicorp/packer:1.0.0  
  
RUN apk add \--update py-pip libffi-dev python-dev openssl-dev openssh-client
alpine-sdk && \  
pip install ansible && \  
apk del alpine-sdk  

