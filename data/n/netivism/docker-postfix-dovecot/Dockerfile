FROM debian:jessie  
MAINTAINER Jimmy Huang <jimmy@netivism.com.tw>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update -y && \  
apt-get install -y -q pwgen postfix postfix-pcre dovecot-common dovecot-core
dovecot-imapd opendkim opendkim-tools rsyslog supervisor vim procps  
  
ADD dovecot/dovecot.conf /etc/dovecot/dovecot.conf  
ADD opendkim/opendkim.conf /etc/opendkim.conf  
ADD dovecot/dovecot /etc/init.d/dovecot  
ADD postfix/master.cf /etc/postfix/master.cf  
ADD postfix/transport /etc/postfix/transport  
ADD container/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD rsyslog/50-default.conf /etc/rsyslog.d/50-default.conf  
  
ADD container/init.sh /init.sh  
ADD container/regenpasswd.sh /usr/local/bin/regenpasswd.sh  
ADD container/regenpasswd.sh /usr/local/bin/removemail.sh  
RUN chmod +x /init.sh  
RUN chmod +x /usr/local/bin/regenpasswd.sh  
RUN chmod +x /usr/local/bin/removemail.sh  
  
CMD ["/usr/bin/supervisord"]  

