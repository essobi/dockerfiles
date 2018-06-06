FROM phpplatform/php-apache:7.0  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
RUN apt-get update -yqq \  
&& apt-get install git -yqq \  
&& apt-get install wget -yqq \  
&& apt-get install zip -yqq \  
&& apt-get install unzip -yqq  
  
RUN wget https://composer.github.io/installer.sig -O - -q | tr -d '\n' >
installer.sig \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
file_get_contents('installer.sig')) { echo 'Installer verified'; } else { echo
'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php'); unlink('installer.sig');" \  
&& mv composer.phar /usr/local/bin/composer  

