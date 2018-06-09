FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
postfix \  
postfix-mysql \  
postfix-policyd-spf-python \  
openssl \  
dovecot-core \  
dovecot-imapd \  
dovecot-mysql \  
dovecot-sieve \  
dovecot-managesieved \  
dovecot-antispam \  
opendkim opendkim-tools  
  
RUN apt-get install -y lsb-release wget && \  
CODENAME=`lsb_release -c -s` && \  
wget -O- https://rspamd.com/apt-stable/gpg.key | apt-key add - && \  
echo "deb http://rspamd.com/apt-stable/ $CODENAME main" >
/etc/apt/sources.list.d/rspamd.list && \  
echo "deb-src http://rspamd.com/apt-stable/ $CODENAME main" >>
/etc/apt/sources.list.d/rspamd.list && \  
apt-get update && \  
apt-get install --no-install-recommends -y rspamd  
  
COPY etc /etc/  
  
RUN groupadd -g 5000 vmail && \  
useradd -g vmail -u 5000 vmail -d /home/vmail -m && \  
chgrp postfix /etc/postfix/mysql-*.cf && \  
chgrp vmail /etc/dovecot/dovecot.conf && \  
chmod g+r /etc/dovecot/dovecot.conf  
  
COPY policyd-spf.conf /etc/postfix-policyd-spf-python/policyd-spf.conf  
  
RUN postconf -e virtual_gid_maps=static:5000 && \  
postconf -e virtual_mailbox_domains=mysql:/etc/postfix/mysql-virtual-mailbox-
domains.cf && \  
postconf -e virtual_mailbox_maps=mysql:/etc/postfix/mysql-virtual-mailbox-
maps.cf && \  
postconf -e virtual_alias_maps=mysql:/etc/postfix/mysql-virtual-alias-
maps.cf,mysql:/etc/postfix/mysql-email2email.cf && \  
postconf -e virtual_transport=dovecot && \  
postconf -e dovecot_destination_recipient_limit=1 && \  
# TLS Configuration  
postconf -e smtpd_tls_cert_file=/etc/ssl/certs/postfix-cert.pem && \  
postconf -e smtpd_tls_key_file=/etc/ssl/private/postfix-cert.key && \  
postconf -e smtpd_tls_ciphers=high && \  
postconf -e smtpd_tls_loglevel=1 && \  
postconf -e smtpd_tls_received_header=yes && \  
postconf -e smtpd_tls_security_level=may && \  
postconf -e smtpd_tls_protocols=!SSLv2,!SSLv3,TLSv1,TLSv1.1,TLSv1.2 && \  
postconf -e smtpd_tls_mandatory_protocols=!SSLv2,!SSLv3,TLSv1,TLSv1.1,TLSv1.2
&& \  
postconf -e smtpd_tls_mandatory_exclude_ciphers=EXPORT,LOW,aNULL,MD5,RC4 && \  
postconf -e smtpd_tls_exclude_ciphers=EXPORT,LOW,aNULL,MD5,RC4 && \  
postconf -e smtpd_tls_mandatory_ciphers=high && \  
postconf -e smtp_tls_security_level=may && \  
postconf -e smtp_tls_loglevel=1 && \  
postconf -e smtp_tls_mandatory_protocols=!SSLv2,!SSLv3,TLSv1,TLSv1.1,TLSv1.2
&& \  
postconf -e smtp_tls_protocols=!SSLv2,!SSLv3,TLSv1,TLSv1.1,TLSv1.2 && \  
postconf -e smtp_tls_mandatory_ciphers=high && \  
postconf -e smtp_tls_mandatory_exclude_ciphers=LOW,EXPORT,aNULL,MD5,RC4 && \  
postconf -e tls_preempt_cipherlist=yes && \  
postconf -e smtpd_tls_eecdh_grade=strong && \  
# Auth  
postconf -e smtpd_sasl_type=dovecot && \  
postconf -e smtpd_sasl_path=private/auth && \  
# SPF  
postconf -e policy-spf_time_limit=3600s && \  
postconf -e smtpd_relay_restrictions="permit_mynetworks
permit_sasl_authenticated defer_unauth_destination check_policy_service
unix:private/policy-spf" && \  
  
# Rspamd  
postconf -e
smtpd_milters=inet:127.0.0.1:11332,local:/var/run/opendkim/opendkim.sock && \  
postconf -e milter_protocol=6,2 && \  
postconf -e milter_mail_macros="i {mail_addr} {client_addr} {client_name}
{auth_authen}" && \  
# skip mail without checks if something goes wrong  
postconf -e milter_default_action=accept && \  
  
# specially for docker  
postconf -F '*/*/chroot = n'  
RUN echo "dovecot unix - n n - - pipe" >> /etc/postfix/master.cf && \  
echo ' flags=DRhu user=vmail:vmail argv=/usr/lib/dovecot/deliver -f ${sender}
-d ${user}@${nexthop} -a ${recipient}' >> /etc/postfix/master.cf  
  
RUN echo "submission inet n - - - - smtpd" >> /etc/postfix/master.cf && \  
echo " -o smtpd_tls_security_level=encrypt" >> /etc/postfix/master.cf && \  
echo " -o smtpd_sasl_auth_enable=yes" >> /etc/postfix/master.cf && \  
echo " -o smtpd_client_restrictions=permit_sasl_authenticated,reject" >>
/etc/postfix/master.cf  
  
RUN echo "policy-spf unix - n n - - spawn" >> /etc/postfix/master.cf && \  
echo " user=nobody argv=/usr/bin/policyd-spf" >> /etc/postfix/master.cf  
  
COPY start.sh /start.sh  
  
# TODO: add VOLUME instructions for at least /etc/opendkim/keys/  
# default config  
ENV DB_HOST localhost  
ENV DB_USER root  
  
# SMTP ports  
EXPOSE 25  
EXPOSE 587  
# POP and IMAP ports  
EXPOSE 110  
EXPOSE 143  
EXPOSE 995  
EXPOSE 993  
# Manage Sieve  
EXPOSE 2093  
CMD ["sh", "start.sh"]  

