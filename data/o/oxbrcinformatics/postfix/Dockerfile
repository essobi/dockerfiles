# Credit to juanluisbaptiste/docker-postfix this is the dockerfile but using  
# linux-alpine rather than centos  
#Dockerfile for a Postfix email relay service  
FROM alpine:3.3  
MAINTAINER James Welch <james.welch@ndm.ox.ac.uk>  
  
ENV VERSION 1.0.0  
RUN apk add --update supervisor perl cyrus-sasl mailx postfix bash openrc icu-
dev rsyslog && \  
mkdir -p /var/log/supervisor /var/spool/mail && \  
postconf inet_interfaces=all \  
smtputf8_enable=no \  
'myorigin=$mydomain' \  
mail_spool_directory=/var/spool/mail \  
mynetworks_style=class \  
smtp_tls_security_level=may && \  
sed -i -e 's:-/var/log/messages:-/var/log/messages.log:' \  
-e 's:-/var/log/maillog:-/var/log/mail.log:' \  
-e 's_\\*.emerg.*\\*_*.emerg :omusrmsg:*_' /etc/rsyslog.conf && \  
newaliases  
  
COPY postfix.sh /usr/local/bin  
COPY etc/supervisord.d /etc/supervisor.d  
  
RUN chmod +x /usr/local/bin/*  
  
VOLUME /var/log  
  
EXPOSE 25  
ENTRYPOINT ["supervisord"]  
CMD ["-c", "/etc/supervisord.conf"]  
  

