FROM shaddock/seed:latest  
MAINTAINER Thibaut Lapierre <root@epheo.eu>  
  
#install ceilometer  
RUN apt-get -y update  
RUN apt-get install -y --force-yes mongodb-clients python-pymongo ceilometer-
api ceilometer-collector ceilometer-agent-central \  
ceilometer-agent-notification ceilometer-alarm-evaluator ceilometer-alarm-
notifier \  
python-ceilometerclient  
  
ADD supervisord.conf /etc/supervisord.conf  
  
VOLUME ["/var/log/ceilometer"]  
  
ADD ceilometer-start /usr/local/bin/  
ADD configparse.py /usr/local/bin/  
RUN chmod +x /usr/local/bin/ceilometer-start  
RUN chmod +x /usr/local/bin/configparse.py  
  
EXPOSE 8776  
CMD ["ceilometer-start"]  

