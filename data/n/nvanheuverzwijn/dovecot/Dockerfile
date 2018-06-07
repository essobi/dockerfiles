FROM debian:stretch-slim  
  
ENV ENTRYPOINT_ROOT="entrypoint" \  
DEBIAN_FRONTEND="noninteractive" \  
DOVECOT_DOVECOT_CONF="" \  
DOVECOT_DOVECOT_SQL_CONF_EXT="" \  
DOVECOT_LDAP_CONF_EXT="" \  
DOVECOT_10_AUTH="" \  
DOVECOT_10_MAIL="" \  
DOVECOT_10_MASTER="" \  
DOVECOT_10_SSL="" \  
DOVECOT_15_LDA="" \  
DOVECOT_15_MAILBOXES="" \  
DOVECOT_20_IMAP="" \  
DOVECOT_20_LMTP="" \  
DOVECOT_20_MANAGESIEVE="" \  
DOVECOT_90_FTS="" \  
DOVECOT_90_SIEVE=""  
  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
busybox-syslogd \  
ca-certificates \  
dovecot-imapd \  
dovecot-mysql \  
dovecot-lmtpd \  
dovecot-managesieved \  
dovecot-sieve \  
dovecot-solr \  
procps \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd -u 5000 -U -m -d /var/mail --groups mail vmail  
  
ADD https://github.com/kronostechnologies/docker-init-
entrypoint/releases/download/1.3.0/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
EXPOSE 110 143 993 995  
  
COPY docker/ /  

