FROM maxwellewxam/php-fpm  
  
RUN apt-get install -y openssh-server nano  
  
RUN useradd www -d /var/www/ -p null -s /bin/bash \  
&& echo "www:www" | chpasswd  
ADD https://raw.githubusercontent.com/Maxwellewxam/dotfiles/master/.dir_colors
/var/www/.dir_colors  
RUN chown -R www /var/www && chmod 777 -R /var/www  
  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
RUN pecl install xdebug \  
&& touch $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20160303/xdebug.so' >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo 'xdebug.remote_enable=1' >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo 'xdebug.remote_connect_back=1' >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo 'xdebug.remote_port=9999' >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo 'xdebug.var_display_max_depth=10' >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo 'xdebug.cli_color=1' >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo 'xdebug.show_local_vars=1' >> $PHP_INI_DIR/conf.d/xdebug.ini  
  
RUN echo 'Port 2222' >> /etc/ssh/sshd_config  
  
EXPOSE 2222  
EXPOSE 9999  
CMD /etc/init.d/ssh start && php-fpm  

