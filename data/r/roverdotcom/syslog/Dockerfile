FROM ubuntu:14.04  
RUN apt-get update -q  
RUN apt-get install rsyslog  
COPY run.sh /run.sh  
CMD /run.sh  
VOLUME /dev  
VOLUME /var/log  

