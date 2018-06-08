FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get -y install clamav-daemon  
RUN freshclam  
  
ADD ./clamd.conf /etc/clamav/clamd.conf  
  
VOLUME /var/run/clamav/clamd.ctl  
ENTRYPOINT ["clamd", "--config-file=/etc/clamav/clamd.conf"]  
  

