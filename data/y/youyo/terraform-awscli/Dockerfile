FROM python:3-alpine  
MAINTAINER youyo  
  
ENV TERRAFORM_VERSION=0.9.11  
RUN apk add --no-cache --update ca-certificates openssl curl && \  
wget
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin/ && \  
rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
pip install awscli  

