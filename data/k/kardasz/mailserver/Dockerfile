FROM debian:jessie  
MAINTAINER Krzysztof Kardasz <krzysztof@kardasz.eu>  
  
# Update system and install required packages  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
ENV RUN_USER mailserver  
ENV RUN_USER_UID 6000  
ENV RUN_GROUP mailserver  
ENV RUN_GROUP_GID 6000  
ENV OPENDKIM_USER opendkim  
ENV OPENDKIM_USER_UID 6001  
ENV OPENDKIM_GROUP opendkim  
ENV OPENDKIM_GROUP_GID 6001  
ENV SPAMD_USER spamd  
ENV SPAMD_USER_UID 6002  
ENV SPAMD_GROUP spamd  
ENV SPAMD_GROUP_GID 6002  
ENV VERSION 1  
RUN \  
groupadd --gid ${OPENDKIM_GROUP_GID} -r ${OPENDKIM_GROUP} && \  
useradd -r -d /var/run/opendkim --uid ${OPENDKIM_USER_UID} -g
${OPENDKIM_GROUP} ${OPENDKIM_USER} && \  
mkdir -p /var/run/opendkim && chown ${OPENDKIM_USER}:${OPENDKIM_GROUP}
/var/run/opendkim  
  
RUN \  
groupadd --gid ${SPAMD_GROUP_GID} -r ${SPAMD_GROUP} && \  
useradd -r -d /home/spamd -m --uid ${SPAMD_USER_UID} -g ${SPAMD_GROUP}
${SPAMD_USER}  
  
RUN \  
groupadd --gid ${RUN_GROUP_GID} -r ${RUN_GROUP} && \  
useradd -r --uid ${RUN_USER_UID} -g ${RUN_GROUP} ${RUN_USER}  
  
# Install git, download and extract Stash and create the required directory
layout.  
# Try to limit the number of RUN instructions to minimise the number of layers
that will need to be created.  
RUN apt-get update -qq \  
&& apt-get install -y wget curl postfix postfix-mysql dovecot-core dovecot-
imapd dovecot-lmtpd dovecot-mysql dovecot-sieve dovecot-managesieved postfix-
policyd-spf-python clamsmtp clamav clamav-milter clamav-unofficial-sigs
milter-greylist spamass-milter opendkim opendkim-tools syslog-ng supervisor \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
RUN sed -i -E 's/^(\s*)system\\(\\);/\1unix-stream("\/dev\/log");/'
/etc/syslog-ng/syslog-ng.conf  
  
EXPOSE 143 993 110 995 25 465 587  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

