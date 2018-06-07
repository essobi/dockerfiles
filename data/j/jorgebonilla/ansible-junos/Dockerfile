FROM ubuntu:14.04  
MAINTAINER jorge.luis.bonilla@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# 1 - Update apt-get  
RUN apt-get update  
  
#2 Install junos-eznc  
RUN apt-get install -y python-pip python-dev python-lxml libxml2-dev
libxslt1-dev openssl ca-certificates ssh  
  
#Required for cryptography (which is required by ncclient)  
RUN apt-get install -y build-essential libssl-dev libffi-dev  
RUN pip install cryptography==1.2.1  
RUN pip install ncclient  
RUN pip install junos-eznc  
  
#3 install netconify (latest version, 1.0.3 as of compilation, which supports
--ssh)  
RUN apt-get install -y git  
RUN pip install git+https://github.com/Juniper/py-junos-netconify.git  
  
#2 Install Ansible  
RUN pip install ansible && mkdir /etc/ansible  
  
#3 - Install Junos Galaxy on ansible  
RUN ansible-galaxy install Juniper.junos  
  
#4 - Clean up  
RUN apt-get clean &&\  
apt-get purge  
  
#Optional - Copy example files  
ADD ./example /tmp/example  

