FROM alpine  
  
RUN apk update && apk add libffi-dev \  
openssl-dev \  
build-base \  
python \  
py-pip \  
python-dev  
  
RUN pip install ansible awscli  
  
RUN wget
https://releases.hashicorp.com/packer/1.2.1/packer_1.2.1_linux_amd64.zip &&
unzip packer_1.2.1_linux_amd64.zip  
RUN rm -rf packer_1.2.1_linux_amd64.zip && mv packer /usr/sbin/  
  
ENV USER root  
WORKDIR /packer

