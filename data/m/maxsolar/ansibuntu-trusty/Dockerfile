FROM ubuntu:trusty  
LABEL MAINTAINER='Jim T. Tang<maxubuntu@gmail.com>'  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get dist-upgrade -y && \  
apt-get install python-pip python-dev libffi-dev libyaml-dev libssl-dev \  
aptitude wget curl -y  
  
## install Ansible 2.4.0.0  
RUN pip install ansible==2.4.0.0 && \  
mkdir /etc/ansible; echo '[local]' > /etc/ansible/hosts; \  
echo 127.0.0.1 >>/etc/ansible/hosts; \  
apt-get clean all && apt-get autoremove -y  
  
CMD ["/bin/bash"]  

