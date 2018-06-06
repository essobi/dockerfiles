FROM ubuntu:14.04.5  
MAINTAINER Josh Jaques "josh.jaques@telenium.ca"  
RUN apt-get update -qy  
RUN apt-get install -y build-essential cmake libffi-dev  
RUN apt-get install -y linux-headers-$(uname -r)  
RUN apt-get install -y wget  
RUN apt-get install -y git  
  
RUN apt-get install -y postgresql-9.3 postgresql-server-dev-9.3  
RUN apt-get install -y postgresql-contrib-9.3  
  
RUN apt-get install -y python3-dev  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python3 get-pip.py  
  
RUN wget https://cogentdatahub.com/assets/srr-2.0.11.tgz  
RUN tar xvzf srr-2.0.11.tgz  
RUN make -C srr-2.0.11  
RUN make -C srr-2.0.11 install  
  
RUN pip install tox  

