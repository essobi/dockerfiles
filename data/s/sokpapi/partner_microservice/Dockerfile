FROM ubuntu:14.04  
MAINTAINER oladayo, toye , samuel <devops@terragonltd.com>  
  
RUN apt-get update  
  
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential  
RUN apt-get install -y python python-dev python-distribute python-pip  
RUN cd /  
RUN mkdir production  
RUN cd production  
WORKDIR /production  
ADD partner_microservice/libraries /production/libraries  
ADD logs /production/logs  
ADD partner_microservice/partner.py /production/partner.py  
ADD partner_microservice/requirements.txt /production/requirements.txt  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8081  
RUN ls -larth  
CMD python partner.py  
  

