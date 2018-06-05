# Dockerfile for building Ansible image for Ubuntu 12.04 (Precise LTS), with
as few additional software as possible.  
FROM ubuntu:12.04  
  
MAINTAINER Valeriy Solovyov <weldpua2008@gmail.com>  
RUN echo "===> Updating cache..." && \  
apt-get update && \  
\  
\  
echo "===> Installing sudo..." && \  
apt-get install -y sudo && \  
\  
\  
apt-get install python-pip python-dev libssl-dev libffi-dev -y && \  
apt-get install python-apt -y -q && \  
apt-get install python-setuptools -y && \  
apt-get install build-essential -y && \  
apt-get install python-dev python2.7-dev python-pip -y && \  
apt-get install --reinstall python-pkg-resources -y && \  
easy_install --upgrade pip && \  
\  
\  
echo "===> Installing Ansible 2.1.1.0..." && \  
pip install --upgrade ansible==2.1.1.0 && \  
\  
\  
echo "===> Adding hosts for convenience..." && \  
mkdir -p /etc/ansible && \  
echo '[local]\nlocalhost\n' > /etc/ansible/hosts && \  
apt-get clean  
  
# apt-get install ansible -y && \  
# apt-get remove ansible --purge -y && \  
  
  
CMD ["/bin/bash"]

