FROM ubuntu:14.04  
MAINTAINER Terragon DCB Team <tech@terragonltd.com>  
  
RUN apt-get update  
  
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential  
RUN apt-get install -y python python-dev python-distribute python-pip  
RUN cd /  
RUN mkdir production  
RUN mkdir /var/log/tmoni/  
RUN cd production  
WORKDIR /production  
ADD subscription-service/libraries /production/libraries  
ADD logs /production/logs  
ADD subscription-service/update_consumer.py /production/update_consumer.py  
  
ADD subscription-service/requirements.txt /production/requirements.txt  
ADD subscription-service/startup.sh /production/startup.sh  
  
ADD subscription-service/cronjob /etc/cron.d/dcb_jobs  
RUN chmod 0644 /etc/cron.d/dcb_jobs  
RUN crontab /etc/cron.d/dcb_jobs  
RUN touch /var/log/tmoni/cron.log  
  
RUN pip install -r requirements.txt  
  
RUN ls -larth  
  
CMD sh /production/startup.sh && tail -f /dev/null  
  

