FROM owncloud:9  
MAINTAINER Ando Roots <ando@sqroot.eu>  
  
RUN apt-get update && \  
apt-get install -y libldap2-dev && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap  

