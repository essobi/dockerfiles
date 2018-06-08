FROM moonscale/runner-magento  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - \  
&& sudo apt-get install -y bzip2 nodejs \  
&& apt-get clean \  
&& npm install -g grunt-cli  
  
RUN docker-php-pecl-install \  
xdebug  
  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Moon" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& echo "extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707"
> $PHP_INI_DIR/conf.d/blackfire.ini  
  
COPY xdebug.ini /usr/local/etc/php/conf.d/conf-xdebug.ini  

