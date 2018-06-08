FROM ubuntu:17.10  
RUN mkdir /ansible2  
WORKDIR /ansible2  
RUN apt update -y && \  
apt install -y \  
libssl-dev python-dev sshpass apt-transport-https \  
ca-certificates curl gnupg2 software-properties-common python-pip wget curl
vim  
RUN /usr/bin/python -m pip install pip -U  
RUN pip install pbr>=1.6 ansible>=2.4.0 netaddr jinja2>=2.9.6  
RUN pip install yamllint apache-libcloud==2.2.1 boto==2.9.0 tox dopy PyCrypto  
  

