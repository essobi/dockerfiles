FROM debian:wheezy  
MAINTAINER Dario Andrei <wouldgo84@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y rsyslog mysql-client
postfix postfix-mysql dovecot-core dovecot-imapd dovecot-lmtpd dovecot-mysql
spamassassin spamc opendkim opendkim-tools  
  
RUN cp /etc/postfix/main.cf /etc/postfix/main.cf.orig  
  
RUN ln -s /etc/ssl/certs/ssl-cert-snakeoil.pem /etc/ssl/certs/dovecot.pem  
RUN ln -s /etc/ssl/private/ssl-cert-snakeoil.key /etc/ssl/private/dovecot.pem  
  
RUN sed -i -re"s/smtpd_tls_cert_file=\/etc\/ssl\/certs\/ssl-cert-
snakeoil.pem/#smtpd_tls_cert_file=\/etc\/ssl\/certs\/ssl-cert-snakeoil.pem/g"
/etc/postfix/main.cf  
RUN sed -i -re"s/smtpd_tls_key_file=\/etc\/ssl\/private\/ssl-cert-
snakeoil.key/#smtpd_tls_key_file=\/etc\/ssl\/private\/ssl-cert-snakeoil.key/g"
/etc/postfix/main.cf  
RUN sed -i -re"s/smtpd_use_tls=yes/#smtpd_use_tls=yes/g" /etc/postfix/main.cf  
RUN sed -i
-re"s/smtpd_tls_session_cache_database.*/#smtpd_tls_session_cache_database =
btree:$\\{data_directory\\}\/smtpd_scache/g" /etc/postfix/main.cf  
RUN sed -i
-re"s/smtp_tls_session_cache_database.*/#smtp_tls_session_cache_database =
btree:$\\{data_directory\\}\/smtp_scache/g" /etc/postfix/main.cf  
  
RUN echo "" >> /etc/postfix/main.cf  
RUN echo "#Container configurations" >> /etc/postfix/main.cf  
RUN echo "smtpd_tls_cert_file=/etc/ssl/certs/dovecot.pem" >>
/etc/postfix/main.cf  
RUN echo "smtpd_tls_key_file=/etc/ssl/private/dovecot.pem" >>
/etc/postfix/main.cf  
RUN echo "smtpd_use_tls=yes" >> /etc/postfix/main.cf  
RUN echo "smtpd_tls_auth_only = yes" >> /etc/postfix/main.cf  
  
RUN echo "smtpd_sasl_type = dovecot" >> /etc/postfix/main.cf  
RUN echo "smtpd_sasl_path = private/auth" >> /etc/postfix/main.cf  
RUN echo "smtpd_sasl_auth_enable = yes" >> /etc/postfix/main.cf  
RUN echo "smtpd_recipient_restrictions = permit_sasl_authenticated,
permit_mynetworks, reject_unauth_destination" >> /etc/postfix/main.cf  
  
RUN sed -i -re"s/mydestination.*/mydestination = localhost/g"
/etc/postfix/main.cf  
  
RUN echo "virtual_transport = lmtp:unix:private/dovecot-lmtp" >>
/etc/postfix/main.cf  
RUN echo "virtual_mailbox_domains = mysql:/etc/postfix/mysql-virtual-mailbox-
domains.cf" >> /etc/postfix/main.cf  
RUN echo "virtual_mailbox_maps = mysql:/etc/postfix/mysql-virtual-mailbox-
maps.cf" >> /etc/postfix/main.cf  
RUN echo "virtual_alias_maps = mysql:/etc/postfix/mysql-virtual-alias-maps.cf"
>> /etc/postfix/main.cf  
  
RUN sed -i -re"s/#submission inet n(\ )+-(\ )+-(\ )+-(\ )+-(\
)+smtpd/submission inet n - - - - smtpd/g" /etc/postfix/master.cf  
RUN sed -i -re"s/#(\ )*-o\ syslog_name=postfix\/submission/ -o
syslog_name=postfix\/submission/g" /etc/postfix/master.cf  
RUN sed -i -re"s/#(\ )*-o\ smtpd_tls_security_level=encrypt/ -o
smtpd_tls_security_level=encrypt/g" /etc/postfix/master.cf  
RUN sed -i -re"s/#(\ )*-o\ smtpd_sasl_auth_enable=yes/ -o\
smtpd_sasl_auth_enable=yes/ ; ta ; b ; :a ; N ; ba" /etc/postfix/master.cf  
RUN sed -i -re"s/#(\ )*-o\
smtpd_client_restrictions=permit_sasl_authenticated,reject/ -o
smtpd_client_restrictions=permit_sasl_authenticated,reject/ ; ta ; b ; :a ; N
; ba" /etc/postfix/master.cf  
  
RUN cp /etc/dovecot/dovecot.conf /etc/dovecot/dovecot.conf.orig  
RUN cp /etc/dovecot/conf.d/10-mail.conf /etc/dovecot/conf.d/10-mail.conf.orig  
RUN cp /etc/dovecot/conf.d/10-auth.conf /etc/dovecot/conf.d/10-auth.conf.orig  
RUN cp /etc/dovecot/dovecot-sql.conf.ext /etc/dovecot/dovecot-
sql.conf.ext.orig  
RUN cp /etc/dovecot/conf.d/10-master.conf
/etc/dovecot/conf.d/10-master.conf.orig  
RUN cp /etc/dovecot/conf.d/10-ssl.conf /etc/dovecot/conf.d/10-ssl.conf.orig  
  
RUN echo "#Container configurations" >> /etc/dovecot/dovecot.conf  
RUN echo "protocols = imap lmtp" >> /etc/dovecot/dovecot.conf  
  
RUN sed -i -re"s/mail_location.*/mail_location =
maildir:\/var\/mail\/vhosts\/%d\/%n/g" /etc/dovecot/conf.d/10-mail.conf  
RUN sed -i -re"s/#mail_privileged_group.*/mail_privileged_group = mail/g"
/etc/dovecot/conf.d/10-mail.conf  
  
RUN mkdir -p /var/mail/vhosts  
RUN groupadd -g 5000 vmail  
RUN useradd -g vmail -u 5000 vmail -d /var/mail  
RUN chown -Rv vmail:vmail /var/mail  
RUN chmod -Rv g+rwx /var/mail  
  
RUN sed -i -re"s/#disable_plaintext_auth\ =\ yes/disable_plaintext_auth =
yes/g" /etc/dovecot/conf.d/10-auth.conf  
RUN sed -i -re"s/auth_mechanisms.*/auth_mechanisms = plain login/g"
/etc/dovecot/conf.d/10-auth.conf  
RUN sed -i -re"s/\\!include auth-system.conf.ext/#\\!include auth-
system.conf.ext/g" /etc/dovecot/conf.d/10-auth.conf  
RUN sed -i -re"s/#\\!include auth-sql.conf.ext/\\!include auth-sql.conf.ext/g"
/etc/dovecot/conf.d/10-auth.conf  
  
ADD ./confs/connect-line-dovecot-sql.conf.ext /tmp/connect-line-dovecot-
sql.conf.ext  
RUN printf "passdb {\n driver = sql\n args = /etc/dovecot/dovecot-
sql.conf.ext\n}\n\nuserdb {\n driver = static\n " > /etc/dovecot/conf.d/auth-
sql.conf.ext && echo "args = uid=vmail gid=vmail home=/var/mail/vhosts/%d/%n"
>> /etc/dovecot/conf.d/auth-sql.conf.ext && echo "}" >>
/etc/dovecot/conf.d/auth-sql.conf.ext  
RUN sed -i -re"s/#driver.*/driver = mysql/g" /etc/dovecot/dovecot-sql.conf.ext
&& cat /tmp/connect-line-dovecot-sql.conf.ext >> /etc/dovecot/dovecot-
sql.conf.ext && echo "" >> /etc/dovecot/dovecot-sql.conf.ext && echo
"default_pass_scheme = SHA512-CRYPT" >> /etc/dovecot/dovecot-sql.conf.ext &&
echo "" >> /etc/dovecot/dovecot-sql.conf.ext && echo "password_query = SELECT
email as user, password FROM virtual_users WHERE email='%u';" >>
/etc/dovecot/dovecot-sql.conf.ext  
  
RUN chown -R vmail:dovecot /etc/dovecot  
RUN chmod -R o-rwx /etc/dovecot  
  
RUN sed -i -re"s/#ssl.*/ssl = required/g" /etc/dovecot/conf.d/10-ssl.conf &&
sed -i -re"s/ssl_cert.*/ssl_cert = <\/etc\/ssl\/certs\/dovecot.pem/g"
/etc/dovecot/conf.d/10-ssl.conf && sed -i -re"s/ssl_key.*/ssl_key =
<\/etc\/ssl\/private\/dovecot.pem/g" /etc/dovecot/conf.d/10-ssl.conf  
  
RUN adduser spamd --disabled-login  
RUN sed -i -re"s/ENABLED=0/ENABLED=1/g" /etc/default/spamassassin  
RUN sed -i -re"s/OPTIONS=.*/OPTIONS=\"--create-prefs --max-children 5
--username spamd --helper-home-dir \/home\/spamd\/ -s
\/home\/spamd\/spamd.log\"/g" /etc/default/spamassassin  
RUN sed -i -re"s/PIDFILE=.*/PIDFILE=\"\/home\/spamd\/spamd.pid\"/g"
/etc/default/spamassassin  
RUN sed -i -re"s/CRON=0/CRON=1/g" /etc/default/spamassassin  
  
ADD ./confs/mysql-virtual-mailbox-domains.cf /etc/postfix/mysql-virtual-
mailbox-domains.cf  
ADD ./confs/mysql-virtual-mailbox-maps.cf /etc/postfix/mysql-virtual-mailbox-
maps.cf  
ADD ./confs/mysql-virtual-alias-maps.cf /etc/postfix/mysql-virtual-alias-
maps.cf  
  
ADD ./confs/etc.dovecot.conf.d.10-master.conf
/etc/dovecot/conf.d/10-master.conf  
  
ADD ./confs/spamassassin-rules.conf /etc/spamassassin/local.cf  
RUN sed -i -re"s/smtp inet n - - - - smtpd/smtp inet n - - - - smtpd\r\n -o
content_filter=spamassassin/g" /etc/postfix/master.cf  
RUN echo "spamassassin unix - n n - - pipe" >> /etc/postfix/master.cf && echo
" user=spamd argv=/usr/bin/spamc -f -e" >> /etc/postfix/master.cf && echo "
/usr/sbin/sendmail -oi -f \${sender} \${recipient}" >> /etc/postfix/master.cf  
  
ADD ./confs/opendkim.conf /tmp/opendkim.conf  
RUN cat /tmp/opendkim.conf >> /etc/opendkim.conf  
RUN echo 'SOCKET="inet:12301@localhost"' >> /etc/default/opendkim  
RUN echo 'milter_protocol = 2' >> /etc/postfix/main.cf  
RUN echo 'milter_default_action = accept' >> /etc/postfix/main.cf  
RUN echo 'smtpd_milters = inet:localhost:12301' >> /etc/postfix/main.cf  
RUN echo 'non_smtpd_milters = inet:localhost:12301' >> /etc/postfix/main.cf  
RUN mkdir -p /etc/opendkim/keys  
  
ADD ./run/bootstrap.sh /opt/bootstrap.sh  
ADD ./run/opendkim.sh /opt/opendkim.sh  
ADD ./confs/create_mysql_db.sql /tmp/create_mysql_db.sql  
RUN mkdir -p /opt/dkim-pub && chmod a+x /opt/opendkim.sh  
  
VOLUME ["/var/mail", "/var/log", "/opt/dkim-pub"]  
EXPOSE 25 587 993  
CMD ["/bin/bash", "/opt/bootstrap.sh" ]  

