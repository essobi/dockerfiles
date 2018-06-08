FROM php:5.6-apache  
MAINTAINER Mats Löfgren <mats.lofgren@matzor.eu>  
MAINTAINER Guy Pascarella <guy.pascarella@gmail.com>  
  
RUN a2enmod rewrite  
  
# Install ldap stuff via  
# https://github.com/docker-library/php/issues/75#issuecomment-82075678  
# Slightly modified for the new way debian-jessie works  
RUN apt-get update && apt-get install -y \  
git libfreetype6-dev libpng-dev libjpeg-dev zlib1g unzip wget patch dos2unix
vim \  
ldap-utils libldap-2.4-2 libldap-2.4-2-dbg libldap2-dev && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap && \  
docker-php-ext-install mysqli mbstring && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ &&\  
docker-php-ext-install gd calendar  
  
ENV Q2A_VERSION 1.7.5  
ENV Q2A_FILE_NAME question2answer-${Q2A_VERSION}.zip  
ENV Q2A_DOWNLOAD_URL
https://github.com/q2a/question2answer/releases/download/v${Q2A_VERSION}/${Q2A_FILE_NAME}  
  
RUN mkdir -p /var/www && \  
rm -rf /var/www/html && \  
cd /var/www && pwd && \  
wget ${Q2A_DOWNLOAD_URL} && \  
unzip /var/www/${Q2A_FILE_NAME} && \  
mv /var/www/question2answer-${Q2A_VERSION} /var/www/html && \  
rm -f /var/www/${Q2A_FILE_NAME}  
  
ADD q2a-install-plugin /usr/local/bin/q2a-install-plugin  
  
# Install some common plugins  
RUN /usr/local/bin/q2a-install-plugin NoahY/q2a-badges && \  
/usr/local/bin/q2a-install-plugin jhubert/qa-hipchat-notifications && \  
/usr/local/bin/q2a-install-plugin zakkak/qa-ldap-login && \  
/usr/local/bin/q2a-install-plugin arjunsuresh/q2a-xml-rpc && \  
/usr/local/bin/q2a-install-plugin nakov/q2a-plugin-open-questions && \  
/usr/local/bin/q2a-install-plugin q2a-projects/q2a-tag-descriptions && \  
/usr/local/bin/q2a-install-plugin arjunsuresh/categorydescription && \  
/usr/local/bin/q2a-install-plugin arjunsuresh/tag-search  
  
# Patch login per instructions of qa-ldap-login  
ADD login.php.patch /var/www/html/qa-include/pages/login.php.patch  
RUN find /var/www/html/ -iname "*.php" -exec dos2unix {} \; && \  
patch --backup /var/www/html/qa-include/pages/login.php < /var/www/html/qa-
include/pages/login.php.patch  
  
ADD php.ini /usr/local/etc/php/php.ini  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chown root:root /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

