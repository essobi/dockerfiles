FROM kristophjunge/mediawiki:1.28  
MAINTAINER Steffen Sperling <steffen.sperling@ventum.com>  
  
RUN set -x; \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
libldap2-dev libpq-dev && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap && \  
docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql && \  
docker-php-ext-install pdo pdo_pgsql pgsql && \  
cd extensions && \  
git clone
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/LdapAuthentication && \  
git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/ExternalData  
  

