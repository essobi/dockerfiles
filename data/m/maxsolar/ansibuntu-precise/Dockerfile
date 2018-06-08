FROM ubuntu:precise  
LABEL MAINTAINER='Jim T. Tang<maxubuntu@gmail.com>'  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get dist-upgrade -y && \  
apt-get install aptitude build-essential python python-pip python-dev python-
sphinx python-software-properties wget curl libyaml-dev libffi-dev libssl-dev
-y && \  
wget -qO - https://bootstrap.pypa.io/get-pip.py| python - && \  
/usr/local/bin/pip install -U six requests[security] setuptools simplejson
pyparsing appdirs  
  
## install Ansible 2.4.0.0  
RUN mkdir /etc/ansible; echo '[local]' > /etc/ansible/hosts; \  
echo '127.0.0.1' >> /etc/ansible/hosts; \  
/usr/local/bin/pip install ansible==2.4.0.0 && \  
apt-get clean all && apt-get autoremove -y  
  
CMD ["/bin/bash"]  

