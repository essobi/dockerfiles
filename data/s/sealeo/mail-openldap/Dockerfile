FROM debian:8.2  
LABEL maintainer="Pierre GUINAULT <speed@infinity.ovh>, Alexis Pereda
<alexis@pereda.fr>"  
  
RUN apt-get update && apt-get upgrade -y && \  
LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apt-utils \  
dovecot-imapd \  
dovecot-ldap \  
dovecot-pop3d \  
incron \  
ldap-utils \  
libodbc1 \  
libsasl2-modules-ldap \  
libslp1 \  
libwrap0 \  
postfix \  
postfix-ldap \  
rsyslog \  
sasl2-bin \  
supervisor \  
vim \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LDAP_PASSWORD password  
ENV LDAP_DOMAIN_BASE example.com  
ENV SSL_SMTP_CERT smtp.cert  
ENV SSL_SMTP_KEY smtp.key  
ENV SSL_IMAP_CERT imap.cert  
ENV SSL_IMAP_KEY imap.key  
ENV MAIL_DOMAIN exemple.com  
  
RUN mkdir /root/vmail  
RUN groupadd -g 2000 vmail  
RUN useradd -u 2000 -g 2000 -d /vmail -s /bin/false -m vmail  
  
ADD ./supervisord.conf /etc/supervisord.conf  
  
ADD postfix.main.cf /root/vmail  
ADD init.sh /root/vmail  
ADD script /root/vmail  
  
ADD ./slapd /  
  
RUN chmod +x /root/vmail/script  
RUN ln -s /root/vmail/script /usr/local/bin/add_domain  
RUN ln -s /root/vmail/script /usr/local/bin/add_alias  
RUN ln -s /root/vmail/script /usr/local/bin/add_email  
  
RUN LC_CTYPE=C.UTF-8  
  
EXPOSE 25  
EXPOSE 587  
EXPOSE 993  
VOLUME ["/vmail"]  
VOLUME ["/ssl"]  
  
CMD ["/usr/bin/supervisord", "-c/etc/supervisord.conf"]  

