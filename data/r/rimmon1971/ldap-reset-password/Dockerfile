FROM php:5.6-apache  
  
# Install needed php extensions: ldap  
RUN \  
apt-get update && \  
apt-get install libldap2-dev libmcrypt-dev unzip -y && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-configure mcrypt --with-mcrypt=usr/lib/ && \  
docker-php-ext-install ldap mcrypt  
COPY ltb-project-self-service-password-1.2.zip /ltb-project-self-service-
password-1.2.zip  
  
RUN \  
mkdir /var/www/html/resetpassword && \  
cd /var/www/html/resetpassword && \  
unzip /ltb-project-self-service-password-1.2.zip && \  
rm -f /ltb-project-self-service-password-1.2.zip  
COPY config.inc.php /var/www/html/resetpassword/conf/config.inc.php  
COPY start.bash /ldap-start  
  
# Define default command.  
CMD ["bash", "/ldap-start"]  
  
# Expose ports.  
EXPOSE 80  

