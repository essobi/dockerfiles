FROM ubuntu:14.04  
MAINTAINER oladayo, toye , samuel <devops@terragonltd.com>  
  
RUN apt-get update  
  
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential  
RUN apt-get install -y python python-dev python-distribute python-pip  
RUN cd /  
RUN mkdir production  
RUN cd production  
WORKDIR /production  
ADD msisdnservice/libraries /production/libraries  
ADD logs /production/logs  
ADD msisdnservice/msisdn_fetcher.py /production/msisdn_fetcher.py  
ADD msisdnservice/requirements.txt /production/requirements.txt  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8090  
#uodate  
RUN ls -larth  
CMD python msisdn_fetcher.py  
  

