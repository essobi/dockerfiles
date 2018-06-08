FROM ubuntu:xenial  
MAINTAINER John Paul Alcala jp@jpalcala.com  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update && \  
apt-get -y install \  
rsyslog \  
mail-stack-delivery \  
ca-certificates \  
opendkim \  
opendkim-tools \  
dovecot-mysql \  
postfix-mysql \  
spamass-milter \  
pflogsumm \  
logwatch \  
pyzor \  
razor \  
libmail-dkim-perl \  
clamav-milter \  
arj \  
bzip2 \  
cabextract \  
cpio \  
file \  
gzip \  
lzop \  
nomarch \  
p7zip \  
pax \  
rpm \  
unzip \  
zip \  
zoo && \  
sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d && \  
rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/tmp/.[!.]* \  
/etc/cron.weekly/fstrim  
  
COPY etc/ /etc  
COPY var/ /var  
# User and directory setup  
RUN groupadd -g 5000 vmail && \  
useradd -g vmail -u 5000 vmail -d /var/mail/vmail -m && \  
usermod -G opendkim postfix && \  
usermod -a -G debian-spamd spamass-milter && \  
sa-compile && \  
spamassassin --lint && \  
mkdir -p \  
/etc/opendkim \  
/var/spool/postfix/opendkim \  
/var/spool/postfix/spamassassin \  
/var/lib/spamassassin/.spamassassin \  
/var/lib/spamassassin/.razor \  
/var/lib/spamassassin/.pyzor \  
/var/spool/postfix/clamav && \  
pyzor --homedir /var/lib/spamassassin/.pyzor discover && \  
razor-admin -home=/var/lib/spamassassin/.razor -register && \  
razor-admin -home=/var/lib/spamassassin/.razor -create && \  
razor-admin -home=/var/lib/spamassassin/.razor -discover && \  
echo "razorhome = /var/lib/spamassassin/.razor" >>
/var/lib/spamassassin/.razor/razor-agent.conf && \  
chown opendkim:opendkim /etc/opendkim && \  
chown opendkim:root /var/spool/postfix/opendkim && \  
chown debian-spamd:root /var/spool/postfix/spamassassin/ && \  
chown -R debian-spamd:debian-spamd /var/lib/spamassassin && \  
chown clamav:root /var/spool/postfix/clamav/ && \  
chown -R vmail:vmail /var/mail/vmail && \  
rm -rf /tmp/* /tmp/.[!.]*  
  
# Main postfix configuration  
RUN postconf -e 'mydestination = localhost' && \  
postconf -e 'smtpd_banner = $myhostname ESMTP' && \  
postconf -e 'smtpd_helo_required = yes' && \  
postconf -e 'smtpd_sender_restrictions = reject_unknown_sender_domain,
reject_sender_login_mismatch' && \  
postconf -e 'smtpd_sender_login_maps = $virtual_mailbox_maps' && \  
postconf -e 'unknown_address_reject_code = 550' && \  
postconf -e 'unknown_hostname_reject_code = 550' && \  
postconf -e 'unknown_client_reject_code = 550' && \  
postconf -e 'smtpd_tls_ask_ccert = yes' && \  
postconf -e 'smtpd_tls_CAfile = /etc/ssl/certs/ca-certificates.crt' && \  
postconf -e 'smtpd_tls_loglevel = 1' && \  
postconf -e 'smtpd_tls_session_cache_timeout = 3600s' && \  
postconf -e 'message_size_limit = 30720000' && \  
postconf -e 'virtual_transport = dovecot' && \  
postconf -e 'dovecot_destination_recipient_limit = 1' && \  
postconf -e 'default_destination_concurrency_limit = 5' && \  
postconf -e 'disable_vrfy_command = yes' && \  
postconf -e 'relay_destination_concurrency_limit = 1' && \  
postconf -e 'smtp_tls_note_starttls_offer = yes' && \  
postconf -e 'virtual_mailbox_domains = mysql:/etc/postfix/mysql-virtual-
mailbox-domains.cf' && \  
postconf -e 'virtual_mailbox_maps = mysql:/etc/postfix/mysql-virtual-mailbox-
maps.cf' && \  
postconf -e 'virtual_alias_maps = mysql:/etc/postfix/mysql-virtual-alias-
maps.cf' && \  
postconf -e 'milter_default_action = accept' && \  
postconf -e 'milter_connect_macros = j {daemon_name} v {if_name} _' && \  
postconf -e 'non_smtpd_milters = $smtpd_milters' && \  
postconf -e 'smtpd_milters = unix:/spamass/spamass.sock unix:/clamav/clamav-
milter.ctl unix:/opendkim/opendkim.sock' && \  
postconf -e 'postscreen_greet_action = enforce' && \  
postconf -e 'postscreen_dnsbl_action = enforce' && \  
postconf -e 'postscreen_access_list = permit_mynetworks' && \  
postconf -e 'postscreen_dnsbl_sites = zen.spamhaus.org,
b.barracudacentral.org, bl.spamcop.net'  
# Run script  
COPY postfix.sh /  
COPY learnspam.sh /  
COPY postfix_report.sh /  
  
VOLUME ["/etc/opendkim", "/etc/ssl/private", "/var/mail",
"/var/lib/spamassassin", "/var/lib/dovecot", "/var/lib/clamav",
"/var/lib/logrotate", "/var/log"]  
  
EXPOSE 25 143 993 587  
  
WORKDIR /  
CMD ["/postfix.sh"]  

