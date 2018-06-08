# Docker-VPSr  
#  
# VERSION 0.5  
FROM ubuntu:14.04  
MAINTAINER zauberertz <zieglerz@gmx.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# create file to see if this is the firstrun when started  
RUN touch /firstrun  
  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get install -y wget  
  
# Set postfix to local mail delivery only for the moment. Actual config will
take place at first run  
RUN echo "postfix postfix/main_mailer_type select Local only" | debconf-set-
selections  
  
RUN apt-get update && apt-get install -yq\  
postfix postfix-mysql \  
fetchmail \  
dovecot-imapd dovecot-mysql dovecot-sieve dovecot-managesieved \  
spamassassin razor \  
pwgen \  
postgrey \  
supervisor  
  
COPY startup.sh /startup.sh  
COPY mail-setup.sh /  
RUN chmod +x /startup.sh  
COPY configs/postfix /etc/postfix  
COPY configs/dovecot /etc/dovecot  
COPY configs/spamassassin /etc/spamassassin  
COPY configs/apache2 /etc/apache2/sites-available  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY postfix.sh /postfix.sh  
  
# Cleanup  
RUN apt-get clean  
  
EXPOSE 25 143 993 465 80 443  
ENTRYPOINT [ "/startup.sh" ]  

