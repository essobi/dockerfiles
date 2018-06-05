FROM debian:jessie  
MAINTAINER Christian Simon <mail@christiansimon.eu>  
  
ENV DOMAIN_PRIMARY=christiansimon.eu  
ENV TLS_PRIVKEY=/etc/ssl/mailserver/privkey.pem  
ENV TLS_CERTFILE=/etc/ssl/mailserver/cert.pem  
ENV TLS_CAFILE=/etc/ssl/mailserver/chain.pem  
ENV TLS_FULLCHAINFILE=/etc/ssl/mailserver/fullchain.pem  
  
# Postfix/Courier non-interactive setup  
RUN echo "postfix postfix/mailname string ${DOMAIN_PRIMARY}" | debconf-set-
selections  
RUN echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-
set-selections  
RUN echo "courier-base courier-base/webadmin-configmode boolean true" |
debconf-set-selections  
  
RUN groupadd -r --gid 5000 vmail \  
&& useradd -r --uid 5000 -g vmail -d /var/vmail -s /bin/false -m vmail  
  
RUN apt-get update \  
&& mkdir -p /var/run/courier/authdaemon \  
&& touch /var/run/courier/authdaemon/pid.lock \  
&& apt-get install -y apt-utils \  
&& apt-get install --no-install-recommends -y \  
postfix postfix-mysql spamassassin spamc maildrop sqlgrey gamin \  
courier-authdaemon courier-authlib-mysql courier-pop courier-pop-ssl courier-
imap courier-imap-ssl \  
libsasl2-2 libsasl2-modules libsasl2-modules-sql sasl2-bin libpam-mysql
rsyslog mysql-client less  
  
COPY maildroprc /etc/maildroprc  
  
COPY spamassassin/local.cf /etc/spamassassin/  
  
COPY sqlgrey/clients_fqdn_whitelist.local /etc/sqlgrey/  
COPY sqlgrey/sqlgrey.conf.example /etc/sqlgrey/  
  
COPY postfix/sasl/smtpd.conf /etc/postfix/sasl/smtpd.conf  
COPY postfix/*.cf /etc/postfix/  
COPY postfix/*.template /etc/postfix/  
COPY postfix/postfix.conf.example /etc/postfix/  
  
COPY courier/authdaemonrc /etc/courier/  
COPY courier/authmysqlrc.template /etc/courier/  
COPY courier/imapd-ssl /etc/courier/  
COPY courier/pop3d-ssl /etc/courier/  
  
COPY defaults/* /etc/default/  
  
COPY init-service.sh /usr/local/bin/  
RUN chmod a+x /usr/local/bin/init-service.sh  
  
VOLUME /home/postfix  
VOLUME /etc/mailserver  
  
# SMTP  
EXPOSE 25  
# IMAP (SSL)  
EXPOSE 993  
CMD ["/usr/local/bin/init-service.sh"]

