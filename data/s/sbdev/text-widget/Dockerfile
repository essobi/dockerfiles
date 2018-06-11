FROM php:7.0.8-apache  
COPY config/apache2/apache2.conf /etc/apache2/  
COPY config/apache2/ports.conf /etc/apache2/  
COPY config/apache2/sites-available/000-default.conf /etc/apache2/sites-
available/  
COPY config/apache2/sites-enabled/000-default.conf /etc/apache2/sites-enabled/  
RUN apt-get update && apt-get install -y git zlib1g-dev  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae')
\  
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/local/bin/composer  
COPY config/php.ini /usr/local/etc/php/  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install pdo_mysql  
RUN composer global require "laravel/installer"  
RUN echo 'export PATH="$PATH:$HOME/.composer/vendor/bin"' >> ~/.bashrc  
RUN a2enmod rewrite  
RUN apt-get install -y wget  
RUN wget -c "http://xdebug.org/files/xdebug-2.4.0.tgz" \  
&& tar -xf xdebug-2.4.0.tgz \  
&& rm xdebug-2.4.0.tgz \  
&& ( \  
cd xdebug-2.4.0 \  
&& phpize \  
&& ./configure --enable-xdebug \  
&& make \  
&& make install \  
) \  
&& rm -r xdebug-2.4.0 \  
&& docker-php-ext-enable xdebug  
COPY config/docker-php-ext-xdebug.ini /usr/local/etc/php/conf.d/  

