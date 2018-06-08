FROM texastribune/base  
MAINTAINER tech@texastribune.org  
  
RUN apt-get update  
RUN apt-get install -y postfix supervisor libsasl2-modules syslog-ng-core  
  
# http://help.mandrill.com/entries/23060367-Can-I-configure-Postfix-to-send-
through-Mandrill-  
ENV MANDRILL_USERNAME MANDRILL_USERNAME  
ENV MANDRILL_KEY MANDRILL_KEY  
  
# postfix  
ADD sasl_passwd /etc/postfix/  
ADD main.cf /etc/postfix/  
ADD postfix-supervisord.conf /etc/supervisor/conf.d/postfix.conf  
  
# syslog-ng  
ADD syslog-ng-supervisor.conf /etc/supervisor/conf.d/syslog-ng.conf  
ADD syslog-ng.conf /etc/syslog-ng/syslog-ng.conf  
#RUN touch /var/log/mail.log  
ADD supervisord.conf /etc/supervisor/  
  
ADD run.sh /  
CMD /run.sh  
  
VOLUME /var/log  
  
EXPOSE 25  

