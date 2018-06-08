FROM debian:jessie  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install postfix  
  
COPY syslog-stdout.py /usr/local/bin/syslog-stdout.py  
COPY start.sh /start.sh  
  
ENTRYPOINT ["/start.sh"]  
EXPOSE 25/tcp  

