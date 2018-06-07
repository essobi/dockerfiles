FROM ubuntu:14.04  
MAINTAINER Pierig Le Saux <lesaux@pythian.com>  
  
# Install InfluxDB  
RUN apt-get update -y && \  
apt-get upgrade -y  
  
RUN apt-get install keepalived -y  
  
ADD entrypoint.sh /  
ADD keepalived/ /etc/keepalived/  
ADD config_keepalived.sh /  
  
RUN chmod +x /config_keepalived.sh  
RUN chmod +x /entrypoint.sh  
  
#startup script  
  
ENTRYPOINT ["/entrypoint.sh"]  

