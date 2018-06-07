FROM ubuntu:trusty  
  
MAINTAINER aherrera@mgage.com  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y software-properties-common && \  
apt-get install -y git \  
libffi-dev \  
libssl-dev \  
libyaml-dev \  
python-pip \  
python-dev &&\  
pip install --upgrade pip &&\  
pip install --upgrade setuptools==33.1.1 ansible==2.1.4 boto boto3  
#https://github.com/ansible/ansible/issues/16015  
#https://github.com/pypa/setuptools/issues/942  
  
ENV PYTHONUNBUFFERED=1  
ENV ANSIBLE_FORCE_COLOR=true  

