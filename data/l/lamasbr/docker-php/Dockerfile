FROM chialab/php:7.1-fpm  
MAINTAINER llamas.jf@gmail.com  
  
# Install PHP IMAP and LDAP extensions  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends libc-client-dev libkrb5-dev && \  
docker-php-ext-configure imap --with-imap --with-imap-ssl --with-kerberos && \  
docker-php-ext-install imap && \  
apt-get install -y --no-install-recommends libldap2-dev && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

