FROM ubuntu:14.04  
MAINTAINER tech@texastribune.org  
  
RUN apt-get update && \  
apt-get install -y postfix supervisor libsasl2-modules syslog-ng-core  
  
ENV SMTP_USER SMTP_USER  
ENV SMTP_PASSWORD SMTP_PASSWORD  
ENV SMTP_HOST SMTP_HOST  
  
# postfix  
ADD sasl_passwd /etc/postfix/  
ADD main.cf /etc/postfix/  
ADD postfix-supervisord.conf /etc/supervisor/conf.d/postfix.conf  
  
# syslog-ng  
ADD syslog-ng-supervisor.conf /etc/supervisor/conf.d/syslog-ng.conf  
ADD syslog-ng.conf /etc/syslog-ng/syslog-ng.conf  
  
ADD supervisord.conf /etc/supervisor/  
  
ADD run.sh /  
CMD /run.sh  
  
VOLUME /var/log  
  
EXPOSE 25  

