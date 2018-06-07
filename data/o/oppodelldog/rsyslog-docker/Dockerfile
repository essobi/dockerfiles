FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get -y install rsyslog  
  
EXPOSE 514  
ENTRYPOINT ["rsyslogd", "-n", "-f", "/etc/rsyslogd.conf"]  

