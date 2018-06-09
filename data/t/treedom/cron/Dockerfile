FROM ubuntu:trusty  
  
MAINTAINER Giacomo Triggiano <gtriggiano@treedom.net>  
  
RUN apt-get update && \  
apt-get -yq install \  
rsyslog && \  
rm -rf /var/lib/apt/lists/*  
  
COPY /scripts /cron  
  
RUN chmod 755 /cron/*  
  
CMD ["/cron/start"]  

