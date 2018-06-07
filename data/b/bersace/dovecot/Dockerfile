FROM debian:stretch  
  
ADD https://github.com/krallin/tini/releases/download/v0.17.0/tini /tini  
  
RUN set -ex ; \  
chmod +x /tini; \  
apt-get update -y ; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
gnupg1 ; \  
echo deb http://xi.dovecot.fi/debian/ stretch-auto/dovecot-2.2 main >
/etc/apt/sources.list.d/dovecot.list ; \  
apt-key adv --fetch-keys http://xi.dovecot.fi/debian/archive.key ; \  
apt-get update -y ; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
courier-authlib-userdb \  
dovecot-imapd \  
dovecot-gssapi \  
dovecot-mysql \  
dovecot-pgsql \  
dovecot-sieve \  
dovecot-ldap \  
maildrop \  
python3 \  
ssl-cert \  
; \  
apt-get clean ; \  
rm -rf /var/lib/apt/lists/* ; \  
:  
  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
  
VOLUME /docker-init.d  
ADD autoconf.sh /docker-init.d/autoconf  
ADD unsecure.conf /etc/dovecot/conf.d/00-unsecure.conf  
ADD docker.conf /etc/dovecot/conf.d/99-docker.conf  
ADD snakeoil.conf /etc/dovecot/conf.d/99-unsecure.conf  
  
EXPOSE 143  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["/usr/sbin/dovecot", "-F"]  

