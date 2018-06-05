FROM alpine:latest  
  
MAINTAINER Thomas Sarboni <max-k@post.com>  
  
RUN apk --update-cache --no-cache add opensmtpd  
  
COPY smtpd.conf /etc/smtpd/smtpd.conf  
  
VOLUME /etc/smtpd /var/spool/mail  
  
EXPOSE 25 587  
ENTRYPOINT ["/usr/sbin/smtpd", "-d"]  

