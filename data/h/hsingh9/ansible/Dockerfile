# Dockerfile for building Ansible image for Ubuntu 16.04 (Xenial), with as few
additional software as possible.  
#  
# @see https://launchpad.net/~ansible/+archive/ubuntu/ansible  
#  
# Version 1.0  
#  
# pull base image  
FROM python:2.7-alpine  
  
MAINTAINER Harpreet Singh <hs@hsingh.com>  
  
RUN echo "===> Adding handy tools..." && \  
apk add --no-cache --virtual build-dependencies python-dev libffi-dev openssl-
dev build-base && \  
apk add --no-cache groff curl zip git bash openssh-client && \  
echo "===> Installing Ansible & Boto..." && \  
pip --disable-pip-version-check --no-cache-dir install boto boto3
ansible==2.2.0.0 awscli && \  
\  
\  
apk del build-dependencies && \  
mkdir -p /etc/ansible && \  
echo "localhost ansible_connection=local ansible_python_interpreter=python" >
/etc/ansible/hosts  
  
  
  
# default command: display Ansible version  
CMD [ "ansible-playbook", "--version" ]  

