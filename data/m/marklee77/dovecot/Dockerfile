FROM marklee77/supervisor:alpine  
LABEL maintainer="Mark Stillwell <mark@stillwell.me>"  
  
RUN apk add --update-cache --no-cache \  
curl \  
dovecot \  
dovecot-fts-solr \  
dovecot-ldap \  
dovecot-pigeonhole-plugin && \  
rm -rf \  
/etc/dovecot/* \  
/etc/ssl/dovecot/* \  
/var/cache/apk/* && \  
ln -s dovecot-ldap.conf.ext /etc/dovecot/dovecot-ldap-passdb.conf.ext && \  
ln -s dovecot-ldap.conf.ext /etc/dovecot/dovecot-ldap-userdb.conf.ext && \  
mkdir -m 0755 /var/lib/dovecot && \  
adduser -u 1000 -h /var/lib/vmail -s /bin/false -D vmail  
  
COPY root/etc/dovecot/default.sieve /etc/dovecot/  
RUN chmod 0644 /etc/dovecot/default.sieve  
  
COPY root/etc/periodic/daily/dovecot-tidy-mailboxes /etc/periodic/daily/  
RUN chmod 0755 /etc/periodic/daily/dovecot-tidy-mailboxes  
  
COPY root/etc/my_init.d/10-dovecot-setup /etc/my_init.d/  
RUN chmod 0755 /etc/my_init.d/10-dovecot-setup  
  
COPY root/etc/supervisor/conf.d/dovecot.conf /etc/supervisor/conf.d  
RUN chmod 0644 /etc/supervisor/conf.d/dovecot.conf  
  
EXPOSE 110 143 4190 8025 8100 9027  
VOLUME ["/var/lib/dovecot", "/var/lib/vmail"]  

