FROM ubuntu:14.04  
MAINTAINER oladayo, toye , samuel <devops@terragonltd.com>  
  
RUN apt-get update  
  
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential  
RUN apt-get install -y python python-dev python-distribute python-pip  
RUN cd /  
RUN mkdir production  
RUN mkdir /var/log/tmoni/  
RUN cd production  
WORKDIR /production  
ADD subscription-cron/libraries /production/libraries  
ADD logs /production/logs  
ADD subscription-cron/renewal.py /production/renewal.py  
ADD subscription-cron/reattempt.py /production/reattempt.py  
ADD subscription-cron/billing_consumer.py /production/billing_consumer.py  
ADD subscription-cron/update_consumer.py /production/update_consumer.py  
ADD subscription-cron/new_subscriber.py /production/new_subscriber.py  
  
ADD subscription-cron/requirements.txt /production/requirements.txt  
ADD subscription-cron/startup.sh /production/startup.sh  
  
ADD subscription-cron/cronjob /etc/cron.d/tmoni_jobs  
RUN chmod 0644 /etc/cron.d/tmoni_jobs  
RUN crontab /etc/cron.d/tmoni_jobs  
RUN touch /var/log/tmoni/cron.log  
  
RUN pip install -r requirements.txt  
  
RUN ls -larth  
  
CMD sh /production/startup.sh && tail -f /dev/null  
  

