  
#FROM ubuntu:17.04  
FROM python  
  
MAINTAINER john barnes <jbarnes7952@gmail.com>  
  
LABEL Name=husk  
LABEL Version=0.0.1a  
  
RUN apt update && apt-get install vim -y  
#RUN apt install software-properties-common python-software-properties -y  
#RUN add-apt-repository "ppa:jonathonf/python-3.6"  
#apt-get update && \  
#apt-get install python3.6 -y  
RUN mkdir /app  
COPY . /app/  
WORKDIR /app  
RUN pip3 install -r requirements.txt  
RUN echo "KexAlgorithms diffie-hellman-group1-sha1" >> /etc/ssh/ssh_config  
  
ENTRYPOINT ["python", "/app/husk.py"]  
  

