FROM synctree/mediawiki  
MAINTAINER seu <seu@panopticon.re>  
  
# Note that at the moment we maintain mediawiki by pulling the git repo  
# in a volume mounted to /var/www/html, so the smw and ldap extensions  
# are installed there.  
# ENV LDAPAUTH_DOWNLOAD_URL
"https://extdist.wmflabs.org/dist/extensions/LdapAuthentication-
REL1_24-24a399e.tar.gz"  
#  
# RUN set -x; \  
# curl -fSL "$LDAPAUTH_DOWNLOAD_URL" -o ldap.tar.gz && \  
# tar -xf ldap.tar.gz -C /usr/src/mediawiki/extensions/ --strip-components=0  
# git for composer.phar  
RUN apt-get update && \  
apt-get install -y libldap-dev git && \  
rm -rf /var/lib/apt/lists/* && \  
ln -fs /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/ && \  
docker-php-ext-install ldap && \  
docker-php-ext-install mbstring  
  
VOLUME /var/www/html  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

