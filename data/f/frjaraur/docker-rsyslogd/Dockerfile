FROM alpine:latest  
  
MAINTAINER frjaraur@gmail.com  
  
RUN apk --update --no-cache add bash rsyslog  
  
# Required for loggin  
VOLUME /dev  
  
# Required for forwarding  
VOLUME /var/spool/rsyslog  
  
COPY rsyslog.conf /etc/rsyslog.conf  
  
COPY entrypoint.sh /entrypoint.sh  
  
COPY logrotate /usr/bin/logrotate  
  
EXPOSE 514  
ENTRYPOINT [ "/entrypoint.sh" ]  
  
CMD ["help"]  

