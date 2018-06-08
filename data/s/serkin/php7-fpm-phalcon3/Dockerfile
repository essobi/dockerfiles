FROM serkin/php7-fpm  
  
MAINTAINER serkin.alexander@gmail.com  
  
RUN docker-php-ext-install pdo pdo_mysql  
  
# Install Phalcon 3  
RUN git clone \--depth=1 -b 3.0.x https://git@github.com/phalcon/cphalcon.git
\  
&& cd cphalcon/build \  
&& ./install  
RUN echo "extension=phalcon.so" > $PHP_INI_DIR/conf.d/phalcon.ini  
  
# Install Phalcon 3 dev tools  
RUN composer global require --dev 'phalcon/devtools:3.0.x-dev' && \  
ln -s ~/.composer/vendor/bin/phalcon.php /usr/bin/phalcon && \  
chmod ugo+x /usr/bin/phalcon  

