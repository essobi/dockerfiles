FROM alpine  
  
MAINTAINER https://github.com/imasen  
  
RUN apk add --no-cache clamav clamav-libunrar  
  
RUN mkdir -p /run/clamav \  
&& chown clamav:clamav /run/clamav  
  
RUN freshclam  
  
RUN echo 'TCPSocket 3310' >> /etc/clamav/clamd.conf  
  
EXPOSE 3310  
CMD clamd; freshclam -d; tail -f /var/log/clamav/*.log  

