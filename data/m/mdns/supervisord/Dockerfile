FROM ubuntu:16.04  
MAINTAINER Alexis Ducastel <alexis@ducastel.net>  
  
# Install Supervisor.  
RUN apt-get update && \  
apt-get install -y supervisor && \  
apt-get clean && \  
sed -i.bkp '/\\[supervisord\\]/a nodaemon=true'
/etc/supervisor/supervisord.conf  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

