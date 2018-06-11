FROM node:10.2.1  
  
MAINTAINER David Bauske <david.bauske@voltstorage.com>  
RUN cd  
  
RUN apt-get update  
RUN apt-get install -y python-dev  
  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN rm get-pip.py  
RUN pip install awscli  

