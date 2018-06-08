FROM 4devs/centos  
  
ENV REMI_REPO_VERSION 'remi-php71'  
ENV PHP_TIMEZONE 'Europe/Moscow'  
RUN yum-config-manager --enable ${REMI_REPO_VERSION} \  
&& yum -y install php php-intl php-mbstring php-cli php-xml php-gd \  
&& yum -y install unzip \  
&& yum clean all  
  
RUN sed -ri 's@;date.timezone =@date.timezone = '"$PHP_TIMEZONE"'@g'
/etc/php.ini  
  
# Add global binary directory to PATH and make sure to re-export it  
ENV PATH /composer/vendor/bin:$PATH  
  
# Allow Composer to be run as root  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_VERSION 1.2.0  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"  
  
# Install Composer  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer.phar --version=${COMPOSER_VERSION} \  
&& rm -rf /tmp/composer-setup.php \  
&& echo 'alias composer="php -dmemory_limit=-1 /usr/local/bin/composer.phar"'
>> ~/.bashrc  

