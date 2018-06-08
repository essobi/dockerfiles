FROM phusion/baseimage  
MAINTAINER Ragnar Hongset <ragnar.hongset@raghon.no>  
  
# Based on the fine work of Guilhem Berna <guilhem.berna@gmail.com>  
RUN apt-get update && apt-get install -yq \  
nginx \  
python-flup  
  
ENV autostart true  
  
#Adding all our scripts  
COPY crontab /etc/cron.d/monitor_nginx  
COPY restart_nginx /etc/my_init.d/z_restart_nginx  
  
#Nginx daemon  
RUN mkdir /etc/service/nginx  
COPY run_nginx.sh /etc/service/nginx/run  
  
VOLUME ["/etc/nginx/", "/var/log/nginx"]  
  
EXPOSE 80 443  
# Baseimage init process  
ENTRYPOINT ["/sbin/my_init"]  

