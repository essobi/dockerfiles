FROM debian:stable-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
ENV EDITOR vim  
ENV TERRAFORM_VERSION 0.11.7  
RUN apt-get -y update && \  
apt-get -y install \  
jq \  
openssh-client \  
python \  
python-pip \  
unzip \  
vim \  
&& \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/*  
  
WORKDIR /azure-orchestration  
  
COPY requirements.txt requirements.txt  
  
RUN pip install -r requirements.txt  
  
ADD
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
/tmp/  
  
RUN unzip /tmp/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d
/usr/local/bin/ && \  
rm /tmp/terraform_${TERRAFORM_VERSION}_linux_amd64.zip  

