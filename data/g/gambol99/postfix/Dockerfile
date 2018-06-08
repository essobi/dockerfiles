#  
# Author: Rohith  
# Date: 2015-07-17 12:49:15 +0100 (Fri, 17 Jul 2015)  
#  
# vim:ts=2:sw=2:et  
#  
FROM gambol99/supervisord  
MAINTAINER Rohith <gambol99@gmail.com>  
  
RUN yum install -y postfix mailx cyrus-sasl cyrus-sasl-plain cyrus-sasl-md5
rsyslog  
ADD config/rsyslog/rsyslog.conf /etc/rsyslog.conf  
ADD config/postfix/main.cf /etc/postfix/main.cf  
ADD config/supervisord/postfix.ini /etc/supervisord.d/postfix.ini  
ADD config/supervisord/rsyslog.ini /etc/supervisord.d/rsyslog.ini  
ADD config/bin/startup.sh /startup.sh  
RUN chmod +x /startup.sh  
  
EXPOSE 25 465 587  
ENTRYPOINT [ "/startup.sh" ]  

