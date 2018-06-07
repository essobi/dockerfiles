FROM debian:jessie  
  
MAINTAINER Ernesto Baez <ernesto@tourpourtous.com>  
  
# Update system and install required packages  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
#ENV XDEBUG_ENABLED 0  
RUN \  
apt-get update && \  
apt-get -y install \  
dovecot-core dovecot-imapd dovecot-pop3d dovecot-lmtpd \  
dovecot-sqlite sqlite3 dovecot-sieve dovecot-managesieved \  
dovecot-lucene dovecot-antispam supervisor && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
COPY etc/dovecot /etc/dovecot  
COPY etc/supervisor.conf /etc/supervisor/conf.d/dovecot.conf  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

