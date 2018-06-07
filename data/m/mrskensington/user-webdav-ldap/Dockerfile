FROM php:7-apache  
MAINTAINER docker@mikeditum.co.uk  
  
RUN apt-get update && \  
apt-get install -y ldap-utils && \  
apt-get clean  
  
RUN a2enmod dav && \  
a2enmod dav_fs && \  
a2enmod ldap && \  
a2enmod authnz_ldap && \  
a2enmod userdir  
  
ENV LDAP_SCHEME=ldap \  
LDAP_SERVER=openldap \  
LDAP_BASE_DN="" \  
LDAP_SEARCH_ATTRIBUTE=uid \  
LDAP_FILTER=objectClass=* \  
LDAP_SEARCH_DN="" \  
LDAP_SEARCH_PASSWORD="" \  
AUTH_REQUIRE=valid-user  
  
COPY index.php /var/www/html/  
  
COPY init_container.sh /usr/bin/  
RUN chmod +x /usr/bin/init_container.sh  
  
COPY webdav.conf.php /etc/apache2/sites-available/  
  
ENTRYPOINT [ "/usr/bin/init_container.sh" ]  

