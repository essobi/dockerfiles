FROM ubuntu:16.04  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
dovecot-core dovecot-imapd dovecot-lmtpd \  
dovecot-sieve dovecot-managesieved dovecot-mysql dovecot-pgsql \  
dovecot-sqlite dovecot-antispam dovecot-ldap dovecot-solr \  
rsync mysql-client  
  
RUN groupadd -g 1000 mbuser  
RUN useradd -u 1000 -g 1000 mbuser  
  
RUN mkdir -p /var/vmail && \  
chown -R mbuser:mbuser /var/vmail/  
  
RUN cp -r /etc/dovecot /dovecot-template  
RUN rm -r /etc/dovecot/  
  
EXPOSE 24 143 993 12345 10026  
CMD ["dovecot", "-F"]  

