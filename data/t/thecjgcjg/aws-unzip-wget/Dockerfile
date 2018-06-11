FROM ubuntu  
MAINTAINER Charles Gillham <charlie@fsmg.co.uk>  
RUN apt-get update  
RUN apt-get install -y python-dev wget unzip openssh-client git  
RUN apt-get install -y linux-headers-$(uname -r) build-essential  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
EXPOSE 6379  

