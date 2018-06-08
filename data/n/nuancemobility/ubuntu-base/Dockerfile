FROM ubuntu:16.10  
MAINTAINER sspcm <mobility-sspcm@nuance.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y python-setuptools openssl ca-certificates cron curl git
unzip && \  
apt-get clean && \  
easy_install supervisor && \  
mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d  
  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
ADD process_failed_to_restart_listener.py
/etc/supervisor/process_failed_to_restart_listener.py  
  
RUN chmod +x /etc/supervisor/process_failed_to_restart_listener.py  
  
CMD supervisord -c /etc/supervisor/supervisord.conf  

