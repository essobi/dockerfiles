FROM ubuntu:artful  
  
LABEL Author="Bruno Honda <bruno.honda@live.com>"  
  
ENV COMPOSER_FINGERPRINT
544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061  
ENV COMPOSER_INSTALLDIR /usr/local/bin  
ENV COMPOSER_FILENAME composer  
  
# Install requires package  
RUN apt-get update \  
&& apt-get install -y \  
git \  
php-cli \  
php-gd \  
php-intl \  
php-mbstring \  
php-pdo \  
php-pdo-pgsql \  
php-xdebug \  
php-xml \  
php-zip  
  
# Install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'${COMPOSER_FINGERPRINT}') { echo 'Installer verified'; } else { echo
'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php --install-dir=${COMPOSER_INSTALLDIR}
\--filename=${COMPOSER_FILENAME} \  
&& php -r "unlink('composer-setup.php');"  
  
CMD ["php", "-a"]  

