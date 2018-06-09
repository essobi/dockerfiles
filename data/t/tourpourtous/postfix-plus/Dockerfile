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
postfix supervisor rsyslog postfix-pcre postgrey ca-certificates spamassassin
spampd opendkim opendmarc && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
COPY etc/postfix /etc/postfix  
COPY etc/opendkim /etc/opendkim  
COPY etc/opendkim.conf /etc/opendkim.conf  
COPY etc/opendmarc.conf /etc/opendmarc.conf  
COPY etc/spamassassin /etc/spamassassin  
COPY etc/spampd.conf /etc/spampd.conf  
COPY etc/postgrey /etc/postgrey  
COPY etc/supervisor.conf /etc/supervisor/conf.d/postfix.conf  
  
COPY entrypoint.sh /  
  
EXPOSE 587  
EXPOSE 25  
ENTRYPOINT ["/entrypoint.sh"]  

