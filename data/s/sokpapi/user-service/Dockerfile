FROM ubuntu:14.04  
MAINTAINER oladayo, toye , samuel <devops@terragonltd.com>  
  
RUN apt-get update  
  
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential  
RUN apt-get install -y python python-dev python-distribute python-pip  
RUN cd /  
RUN mkdir production  
RUN cd production  
WORKDIR /production  
ADD user-service/libraries /production/libraries  
ADD logs /production/logs  
ADD user-service/user_service.py /production/user_service.py  
ADD user-service/requirements.txt /production/requirements.txt  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8080  
RUN ls -larth  
CMD python user_service.py  
  

