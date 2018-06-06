FROM ubuntu:latest  
MAINTAINER cazza/Caroline  
  
RUN apt-get update  
RUN apt-get install -y python python-dev python-distribute python-pip python-
pymongo  
ADD . /project  
WORKDIR /project  
RUN pip install -r requirements.txt  
EXPOSE 8000  
CMD python cpyserver.py  

