FROM shaddock/seed:latest  
MAINTAINER Thibaut Lapierre <root@epheo.eu>  
  
#install heat  
RUN apt-get -y update  
RUN apt-get install -y --force-yes heat-api heat-api-cfn heat-engine python-
heatclient  
  
ADD supervisord.conf /etc/supervisord.conf  
  
ADD heat-start /usr/local/bin/  
ADD configparse.py /usr/local/bin/  
RUN chmod +x /usr/local/bin/heat-start  
RUN chmod +x /usr/local/bin/configparse.py  
  
EXPOSE 8000  
EXPOSE 8004  
CMD ["heat-start"]  

