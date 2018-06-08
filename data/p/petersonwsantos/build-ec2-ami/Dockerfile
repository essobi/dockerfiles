FROM ubuntu:16.04  
LABEL maintainer="peterson W Santos <opeterson@hotmail.com>"  
LABEL terraform.version="0.9.5"  
LABEL packer.version="0.10.2"  
LABEL tag="1.0"  
  
ENV TERRAFORM_VERSION="0.9.5"  
ENV PACKER_VERSION="0.10.2"  
RUN apt-get update -qqy && \  
apt-get install -qqy curl git unzip openssh-client wget python python-pip && \  
pip install -U awscli && \  
pip install -U awsebcli && \  
wget -q
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip -o terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin && \  
rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
wget -q
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
&& \  
unzip -o packer_${PACKER_VERSION}_linux_amd64.zip -d /usr/local/bin && \  
rm packer_${PACKER_VERSION}_linux_amd64.zip && \  
apt-get install -f && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /code  

