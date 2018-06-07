FROM wordpress  
  
MAINTAINER seu <seu@panopticon.re>  
  
RUN apt-get update && \  
apt-get install -y libldap-dev && \  
rm -rf /var/lib/apt/lists/* && \  
ln -fs /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/ && \  
docker-php-ext-install ldap  
  
CMD ["apache2-foreground"]  

