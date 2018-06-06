FROM golang:alpine  
  
# Configure the Terraform version here  
ENV TERRAFORM_VERSION=0.11.2  
RUN apk add --update git bash openssh  
  
# install azure cli (bash and python tooling essential for build - removed
after completion)  
RUN apk update && \  
apk add bash py-pip make && \  
apk add --virtual=build gcc libffi-dev musl-dev openssl-dev python-dev && \  
pip install azure-cli && \  
apk del --purge build  
  
ENV TF_DEV=true  
ENV TF_RELEASE=true  
  
WORKDIR $GOPATH/src/github.com/hashicorp/terraform  
RUN git clone https://github.com/hashicorp/terraform.git ./ && \  
git checkout v${TERRAFORM_VERSION} && \  
/bin/bash scripts/build.sh  
  
# Start in root's home  
WORKDIR /root

