FROM moonscale/runner-drupal:php7.1  
  
RUN docker-php-pecl-install \  
xdebug  
  
# Install phpcs, phpcbf, phpmd, phpcpd  
# Install coder module through drush  
RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
&& chmod +x phpcs.phar \  
&& mv phpcs.phar /usr/local/bin/phpcs \  
&& curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar \  
&& chmod +x phpcbf.phar \  
&& mv phpcbf.phar /usr/local/bin/phpcbf \  
&& wget -c http://static.phpmd.org/php/latest/phpmd.phar \  
&& chmod +x phpmd.phar \  
&& mv phpmd.phar /usr/local/bin/phpmd \  
&& wget https://phar.phpunit.de/phpcpd.phar \  
&& chmod +x phpcpd.phar \  
&& mv phpcpd.phar /usr/local/bin/phpcpd \  
&& drush dl coder --destination=/usr/local \  
&& mkdir -p /usr/local/lib/php/PHP/CodeSniffer/Standards \  
&& ln -s /usr/local/coder/coder_sniffer/Drupal
/usr/local/lib/php/PHP/CodeSniffer/Standards/  
  
RUN rm -rf /var/www/html && ln -s /project/www /var/www/html  
  
COPY xdebug.ini /usr/local/etc/php/conf.d/conf-xdebug.ini  
  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Moon" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& echo "extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707"
> $PHP_INI_DIR/conf.d/blackfire.ini  

