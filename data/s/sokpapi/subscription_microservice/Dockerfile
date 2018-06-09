FROM ubuntu:14.04  
MAINTAINER oladayo, toye , samuel <devops@terragonltd.com>  
  
RUN apt-get update  
  
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential  
RUN apt-get install -y python python-dev python-distribute python-pip  
RUN cd /  
RUN mkdir production  
RUN cd production  
WORKDIR /production  
ADD subscription-service/libraries /production/libraries  
ADD logs /production/logs  
ADD subscription-service/subscription_service.py
/production/subscription_service.py  
ADD subscription-service/renewal.py /production/renewal.py  
ADD subscription-service/reattempt.py /production/reattempt.py  
ADD subscription-service/billing_consumer.py /production/billing_consumer.py  
ADD subscription-service/update_consumer.py /production/update_consumer.py  
ADD subscription-service/requirements.txt /production/requirements.txt  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8086  
RUN ls -larth  
  
CMD python subscription_service.py  

