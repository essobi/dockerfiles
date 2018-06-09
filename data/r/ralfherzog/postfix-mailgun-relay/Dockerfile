FROM debian:jessie  
MAINTAINER Ralf Herzog "ralf@rherzog.de"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq && \  
#>> Postfix setup  
apt-get -q -y install \  
postfix \  
postfix-ldap \  
mailutils \  
libsasl2-2 \  
ca-certificates \  
libsasl2-modules \  
sasl2-bin \  
supervisor \  
syslog-ng \  
syslog-ng-core  
  
#>> Cleanup  
RUN rm -rf /var/lib/apt/lists/* /tmp/* && \  
apt-get autoremove -y && \  
apt-get autoclean  
  
#>> Setup syslog-ng to echo postfix log data to the screen  
# system() can't be used since Docker doesn't allow access to /proc/kmsg.  
# https://groups.google.com/forum/#!topic/docker-user/446yoB0Vx6w  
RUN sed -i -E 's/^(\s*)system\\(\\);/\1unix-stream("\/dev\/log");/'
/etc/syslog-ng/syslog-ng.conf && \  
# https://github.com/LyleScott/docker-postfix-gmail-relay/issues/1  
sed -i '/^smtp_tls_CAfile =/d' /etc/postfix/main.cf  
  
# main.cf  
RUN postconf -e smtpd_banner="\$myhostname ESMTP" && \  
postconf -e smtpd_sasl_auth_enable=yes && \  
postconf -e smtpd_sasl_type=cyrus && \  
postconf -e smtpd_sasl_path=smtpd && \  
#postconf -e
smtpd_recipient_restrictions="reject_sender_login_mismatch,reject_non_fqdn_recipient,reject_non_fqdn_sender,reject_unlisted_recipient,permit_mynetworks,permit_sasl_authenticated,reject_unauth_destination,reject_invalid_hostname,reject_unknown_sender_domain,reject_unknown_recipient_domain,reject_rbl_client
sbl-xbl.spamhaus.org,reject_rbl_client bl.spamcop.net,reject_rbl_client
list.dsbl.org,reject_rbl_client rbl.mail-abuse.org,reject_rbl_client
spamsources.fabel.dk" && \  
#postconf -e
smtpd_relay_restrictions="reject_sender_login_mismatch,reject_non_fqdn_recipient,reject_non_fqdn_sender,reject_unlisted_recipient,permit_mynetworks,permit_sasl_authenticated,reject_unauth_destination,reject_invalid_hostname,reject_unknown_sender_domain,reject_unknown_recipient_domain,reject_rbl_client
sbl-xbl.spamhaus.org,reject_rbl_client bl.spamcop.net,reject_rbl_client
list.dsbl.org,reject_rbl_client rbl.mail-abuse.org,reject_rbl_client
spamsources.fabel.dk" && \  
postconf -e smtpd_reject_unlisted_sender=yes && \  
postconf -e relayhost=[smtp.mailgun.org]:587 && \  
postconf -e smtp_sasl_auth_enable=yes && \  
postconf -e smtp_sasl_password_maps=hash:/etc/postfix/sasl_passwd && \  
postconf -e smtp_sasl_security_options=noanonymous && \  
postconf -e smtpd_sasl_tls_security_options=noanonymous && \  
postconf -e smtp_tls_CAfile=/etc/postfix/cacert.pem && \  
postconf -e smtp_use_tls=yes  
  
RUN usermod -aG sasl postfix  
  
# saslauthd  
# Symlink fix https://wiki.debian.org/PostfixAndSASL  
RUN mkdir -p /var/spool/postfix/var/run/saslauthd && \  
chown postfix /var/spool/postfix/var/ -R && \  
rm -rf /run/saslauthd && ln -s /var/spool/postfix/var/run/saslauthd
/run/saslauthd && \  
echo "pwcheck_method: saslauthd\nmech_list: PLAIN LOGIN\n" >
/etc/postfix/sasl/smtpd.conf && \  
sed -i "s/START=no/START=yes/" /etc/default/saslauthd && \  
sed -i "s/MECHANISMS=\"pam\"/MECHANISMS=\"ldap\"/" /etc/default/saslauthd  
  
EXPOSE 25  
  
COPY supervisord.conf /etc/supervisor/  
COPY init.sh /opt/init.sh  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

