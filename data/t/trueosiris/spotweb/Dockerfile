# Hive Docker manager using shared, synced volume  
FROM trueosiris/webserver:latest  
MAINTAINER Tim Chaubet "tim@chaubet.be"  
RUN mkdir -p /etc/my_init.d  
COPY startup.sh /etc/my_init.d/1.spotweb.startup.sh  
RUN chmod +x /etc/my_init.d/1.spotweb.startup.sh  
  
RUN mkdir -p /etc/service/cycle /var/log/cycle ; sync  
COPY cycle.sh /etc/service/cycle/run  
RUN chmod +x /etc/service/cycle/run \  
&& cp /var/log/cron/config /var/log/cycle/  
  
VOLUME ["/config", "/www"]  
  
EXPOSE 80  
CMD ["/sbin/my_init"]  

