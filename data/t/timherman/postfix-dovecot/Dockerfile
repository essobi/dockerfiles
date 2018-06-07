FROM debian:latest  
  
MAINTAINER Tim Herman <tim@belg.be>  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get install -y mysql-client python-setuptools debconf-utils openssl
rsyslog  
  
RUN echo "postfix postfix/root_address string" | debconf-set-selections  
RUN echo "postfix postfix/procmail boolean false" | debconf-set-selections  
RUN echo "postfix postfix/rfc1035_violation boolean false" | debconf-set-
selections  
RUN echo "postfix postfix/bad_recipient_delimiter error" | debconf-set-
selections  
RUN echo "postfix postfix/protocols select all" | debconf-set-selections  
RUN echo "postfix postfix/retry_upgrade_warning boolean" | debconf-set-
selections  
RUN echo "postfix postfix/kernel_version_warning boolean" | debconf-set-
selections  
RUN echo "postfix postfix/mailname string diva.vimm.be" | debconf-set-
selections  
RUN echo "postfix postfix/tlsmgr_upgrade_warning boolean" | debconf-set-
selections  
RUN echo "postfix postfix/mydomain_warning boolean" | debconf-set-selections  
RUN echo "postfix postfix/recipient_delim string +" | debconf-set-selections  
RUN echo "postfix postfix/mynetworks string 127.0.0.0/8 [::ffff:127.0.0.0]/104
[::1]/128 172.17.0.0/16 " | debconf-set-selections  
RUN echo "postfix postfix/not_configured error" | debconf-set-selections  
RUN echo "postfix postfix/main_mailer_type select Internet Site" | debconf-
set-selections  
RUN echo "postfix postfix/sqlite_warning boolean" | debconf-set-selections  
RUN echo "postfix postfix/destinations string diva.vimm.be,
localhost.localdomain, localhost" | debconf-set-selections  
RUN echo "postfix postfix/chattr boolean false" | debconf-set-selections  
RUN echo "postfix postfix/mailbox_limit string 0" | debconf-set-selections  
RUN echo "postfix postfix/relayhost string" | debconf-set-selections  
  
RUN apt-get install -y postfix postfix-mysql dovecot-common dovecot-imapd
dovecot-pop3d dovecot-lmtpd dovecot-mysql  
  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD ./supervisord.conf /etc/supervisord.conf  
  
RUN mkdir -p /etc/ssl/certs/  
VOLUME /etc/ssl/certs/  
  
RUN mkdir -p /etc/ssl/private/  
VOLUME /etc/ssl/private/  
  
RUN mkdir -p /var/mail/vhosts/  
VOLUME /var/mail/vhosts  
RUN groupadd -g 5000 vmail  
RUN useradd -g vmail -u 5000 vmail -d /var/mail  
  
ADD postfix/main.cf /etc/postfix/main.cf  
ADD postfix/master.cf /etc/postfix/master.cf  
ADD postfix/mysql-virtual-mailbox-domains.cf /etc/postfix/mysql-virtual-
mailbox-domains.cf  
ADD postfix/mysql-virtual-mailbox-maps.cf /etc/postfix/mysql-virtual-mailbox-
maps.cf  
ADD postfix/mysql-virtual-alias-maps.cf /etc/postfix/mysql-virtual-alias-
maps.cf  
  
ADD dovecot/dovecot.conf /etc/dovecot/dovecot.conf  
ADD dovecot/10-mail.conf /etc/dovecot/conf.d/10-mail.conf  
ADD dovecot/10-auth.conf /etc/dovecot/conf.d/10-auth.conf  
ADD dovecot/dovecot-sql.conf.ext /etc/dovecot/dovecot-sql.conf.ext  
ADD dovecot/10-master.conf /etc/dovecot/conf.d/10-master.conf  
ADD dovecot/10-ssl.conf /etc/dovecot/conf.d/10-ssl.conf  
ADD dovecot/auth-sql.conf.ext /etc/dovecot/conf.d/auth-sql.conf.ext  
RUN chown -R vmail:dovecot /etc/dovecot  
RUN chmod -R o-rwx /etc/dovecot  
  
ADD initdb.sql /tmp/initdb.sql  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 25  
EXPOSE 465  
EXPOSE 143  
EXPOSE 993  
EXPOSE 587  
EXPOSE 110  
EXPOSE 995  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  
  

