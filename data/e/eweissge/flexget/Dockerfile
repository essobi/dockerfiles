FROM python:2.7  
LABEL MAINTAINER "Eric Weissgerber <eweissge@gmail.com>"  
  
RUN pip install -I flexget transmissionrpc  
RUN mkdir -p /root/.flexget && touch /root/.flexget/config.yml  
  
#COPY crontab /etc/crontab  
COPY config.yml /root/.flexget  
COPY db-config.sqlite /root/.flexget  
  
VOLUME ["/root/.flexget"]  
  
CMD ["/usr/local/bin/flexget", "--loglevel", "verbose", "daemon", "start"]  
  

