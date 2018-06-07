# Dovecot (IMAP)  
FROM debian:jessie  
  
MAINTAINER Wim Vandersmissen <wim.vandersmissen@nascom.be>  
  
# Install most recent version  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl \  
rsyslog \  
dovecot-imapd \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Environment variables  
ENV POSTFIX_HOSTNAME="mail.nascomdev.be"  
# Add scripts  
COPY scripts /opt/bin  
  
# Add group and user for virtual mail  
RUN groupadd -g 3001 vmail \  
&& useradd -m -d /vmail -u 3001 -g 3001 -s /sbin/nologin vmail \  
&& chmod 755 /vmail \  
&& usermod -G vmail dovecot  
  
# Add secure directory  
RUN mkdir -p /secure/dovecot \  
&& touch /secure/dovecot/users /secure/dovecot/passwd  
  
# Configure dovecot  
COPY config/dovecot /etc/dovecot  
  
# Set timezone  
RUN ln -fs /usr/share/zoneinfo/Europe/Brussels /etc/localtime && dpkg-
reconfigure -f noninteractive tzdata  
  
# Expose IMAP and IMAPS  
EXPOSE 143  
EXPOSE 993  
# Expose SASL auth  
EXPOSE 12345  
COPY run.sh /run.sh  
  
CMD ["/bin/bash", "/run.sh"]  

