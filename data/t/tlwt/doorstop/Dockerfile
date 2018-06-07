#Download base image ubuntu 16.10  
FROM ubuntu:16.10  
# update Ubuntu Software repository  
RUN apt-get update  
  
# installing command line tools  
RUN apt-get -y install nano less git python3 python3-pip  
  
WORKDIR /app  
RUN git clone https://github.com/jacebrowning/doorstop.git  
  
WORKDIR /app/doorstop  
RUN python3 setup.py install  
  
WORKDIR /data  
  
ENTRYPOINT /bin/bash  

