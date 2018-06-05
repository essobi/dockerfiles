# ltb-self-service-password image.  
FROM blowb/php:5.6-fpm  
  
MAINTAINER Hong Xu <hong@topbug.net>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libldap2-dev \  
libmcrypt-dev \  
ssmtp  
  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu  
RUN docker-php-ext-install \  
iconv \  
ldap \  
mbstring \  
mcrypt \  
opcache  
  
RUN curl -L -s http://tools.ltb-project.org/attachments/download/497/ltb-
project-self-service-password-0.8.tar.gz | tar zxvf - -C /var/www/ && \  
mv /var/www/ltb-project-self-service-password-0.8 /var/www/ltb-self-service-
password  
  
# link the configuration file to the "standard" location  
RUN mv -fv /var/www/ltb-self-service-password/conf/config.inc.php /etc/ && \  
ln -fvs /etc/config.inc.php /var/www/ltb-self-service-password/conf/  
  
COPY ltb_self_service_password.ini
/usr/local/etc/php/conf.d/ltb_self_service_password.ini  
  
# modify ssmtp settings  
RUN sed -ri -e 's/^(mailhub=).*/\1smtp-server/' \  
-e 's/^#(FromLineOverride)/\1/' /etc/ssmtp/ssmtp.conf  
  
VOLUME /var/www/ltb-self-service-password  
  
WORKDIR /var/www/ltb-self-service-password

