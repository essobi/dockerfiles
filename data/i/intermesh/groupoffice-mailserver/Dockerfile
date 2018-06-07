FROM debian:stretch-slim  
  
  
  
ENV MYSQL_USER groupoffice  
ENV MYSQL_PASSWORD groupoffice  
ENV MYSQL_DATABASE groupoffice  
ENV MYSQL_HOST db  
ENV POSTMASTER_EMAIL postmaster@example.com  
  
RUN apt-get update  
RUN apt-get install -y postfix postfix-mysql dovecot-imapd dovecot-mysql
dovecot-lmtpd dovecot-sieve dovecot-managesieved supervisor bash rsyslog  
  
#Add user for mail handling  
RUN useradd -r -u 150 -g mail -d /var/mail/vhosts -m -s /sbin/nologin -c
"Virtual Mailbox" vmail  
  
# Dovecot config  
ADD ./etc/dovecot/conf.d/99-groupoffice.conf
/etc/dovecot/conf.d/99-groupoffice.conf  
RUN sed -i 's/{postmaster}/'$POSTMASTER_EMAIL'/'
/etc/dovecot/conf.d/99-groupoffice.conf  
  
ADD ./etc/dovecot/dovecot-sql.conf.ext /etc/dovecot/dovecot-sql.conf.ext  
RUN sed -i 's/{dbHost}/'$MYSQL_HOST'/' /etc/dovecot/dovecot-sql.conf.ext && \  
sed -i 's/{dbName}/'$MYSQL_DATABASE'/' /etc/dovecot/dovecot-sql.conf.ext && \  
sed -i 's/{dbUser}/'$MYSQL_PASSWORD'/' /etc/dovecot/dovecot-sql.conf.ext && \  
sed -i 's/{dbPass}/'$MYSQL_USER'/' /etc/dovecot/dovecot-sql.conf.ext  
  
#disable default system auth because it slows down the login  
RUN sed -i 's/!include auth-system.conf.ext/#!include auth-system.conf.ext/'
/etc/dovecot/conf.d/10-auth.conf  
  
# Postfix config  
RUN cp /etc/hostname /etc/mailname  
  
# SASL settings  
# This will make Postfix authenticate users via Dovecot. Users mail clients
will connect directly to Postfix for sending mail and we need them to
authenticate.  
RUN postconf -e 'smtpd_sasl_auth_enable = yes' && \  
postconf -e 'smtpd_sasl_type = dovecot' && \  
postconf -e 'smtpd_sasl_path = private/auth' && \  
postconf -e 'smtpd_sasl_authenticated_header = yes' && \  
postconf -e 'smtpd_recipient_restrictions = permit_mynetworks,
permit_sasl_authenticated, reject_non_fqdn_sender, reject_non_fqdn_recipient,
reject_unauth_destination, reject_unauth_pipelining, reject_invalid_hostname,
reject_unknown_sender_domain permit' && \  
postconf -e 'smtpd_data_restrictions = reject_unauth_pipelining,
reject_multi_recipient_bounce, permit' && \  
postconf -e 'smtpd_relay_restrictions = permit_mynetworks,
permit_sasl_authenticated, reject_unauth_destination' && \  
postconf -e 'smtpd_sasl_path = private/auth' && \  
postconf -e 'smtp_tls_security_level = may' && \  
postconf -e 'broken_sasl_auth_clients = yes' && \  
postconf -e 'virtual_minimum_uid = 150' && \  
postconf -e 'virtual_uid_maps = static:150' && \  
postconf -e 'virtual_gid_maps = static:8' && \  
postconf -e 'virtual_mailbox_base = /var/mail/vhosts' && \  
postconf -e 'virtual_alias_domains =' && \  
postconf -e 'virtual_alias_maps =
proxy:mysql:$config_directory/mysql_virtual_alias_maps.cf' && \  
postconf -e 'virtual_mailbox_domains =
proxy:mysql:$config_directory/mysql_virtual_mailbox_domains.cf' && \  
postconf -e 'virtual_mailbox_maps =
proxy:mysql:$config_directory/mysql_virtual_mailbox_maps.cf' && \  
postconf -e 'virtual_transport = lmtp:unix:private/dovecot-lmtp' && \  
postconf -e 'default_destination_concurrency_limit = 5' && \  
postconf -e 'relay_destination_concurrency_limit = 1' && \  
postconf -e 'message_size_limit = 20480000' && \  
postconf -M submission/inet="submission inet n - n - - smtpd" && \  
postconf -P "submission/inet/syslog_name=postfix/submission" && \  
postconf -P "submission/inet/smtpd_tls_security_level=encrypt" && \  
postconf -P "submission/inet/smtpd_etrn_restrictions=reject" && \  
postconf -P "submission/inet/smtpd_sasl_type=dovecot" && \  
postconf -P "submission/inet/smtpd_sasl_path=private/auth" && \  
postconf -P "submission/inet/smtpd_sasl_security_options=noanonymous" && \  
postconf -P "submission/inet/smtpd_sasl_local_domain=$myhostname" && \  
postconf -P "submission/inet/smtpd_sasl_auth_enable=yes" && \  
postconf -P "submission/inet/milter_macro_daemon_name=ORIGINATING" && \  
postconf -P
"submission/inet/smtpd_client_restrictions=permit_sasl_authenticated,reject"
&& \  
postconf -P
"submission/inet/smtpd_recipient_restrictions=permit_mynetworks,permit_sasl_authenticated,reject"
&& \  
echo "user = ${MYSQL_USER}\n\  
password = ${MYSQL_PASSWORD}\n\  
hosts = ${MYSQL_HOST}\n\  
dbname = ${MYSQL_DATABASE}\n\  
table = pa_aliases\n\  
select_field = goto\n\  
where_field = address\n\  
additional_conditions = and active = '1'" >
/etc/postfix/mysql_virtual_alias_maps.cf && \  
echo "user = ${MYSQL_USER}\n\  
password = ${MYSQL_PASSWORD}\n\  
hosts = ${MYSQL_HOST}\n\  
dbname = ${MYSQL_DATABASE}\n\  
table = pa_domains\n\  
select_field = domain\n\  
where_field = domain\n\  
additional_conditions = and backupmx = '0' and active = '1'" >
/etc/postfix/mysql_virtual_mailbox_domains.cf && \  
echo "user = ${MYSQL_USER}\n\  
password = ${MYSQL_PASSWORD}\n\  
hosts = ${MYSQL_HOST}\n\  
dbname = ${MYSQL_DATABASE}\n\  
table = pa_mailboxes\n\  
select_field = maildir\n\  
where_field = username\n\  
additional_conditions = and active = '1'" >
/etc/postfix/mysql_virtual_mailbox_maps.cf  
  
# Use supervisor to run multiple services in docker  
ADD ./etc/supervisor/conf.d/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 25  
EXPOSE 143  
EXPOSE 587  
EXPOSE 993  
EXPOSE 4190  
RUN mkdir -p /var/mail/vhosts && chown vmail:mail /var/mail/vhosts  
VOLUME /var/mail/vhosts  
  
ENTRYPOINT ["/usr/bin/supervisord"]  
#CMD /bin/bash  

