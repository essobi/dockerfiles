FROM easysys/ubuntu-base:xenial  
MAINTAINER bexio ag <ops@bexio.com>  
  
# Install Apache  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
apache2 \  
&& sed -ri \  
-e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \  
-e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2\nErrorLogFormat "%l: [pid %P] %F: %E: [client %a] %M"!g' \  
-e 's!^(\s*LogFormat).* combined$!\1 "[%{%Y-%m-%dT%H:%M:%S%z}t] httpd.INFO: \\\"%m %U\\\" %>s %I %O %h %u %D" combined!g' \  
"/etc/apache2/apache2.conf" \  
&& { \  
echo '<VirtualHost *:80>'; \  
echo ' DocumentRoot "/var/www/app/web"'; \  
echo; \  
echo ' <Directory "/var/www/app/web">'; \  
echo ' Options FollowSymLinks'; \  
echo ' AllowOverride All'; \  
echo ' Require all granted'; \  
echo ' </Directory>'; \  
echo; \  
echo ' DirectoryIndex /index.php index.php /index.html index.html'; \  
echo; \  
echo '# Write to the log output of the docker container.'; \  
echo 'CustomLog /proc/self/fd/1 combined'; \  
echo 'ErrorLog /proc/self/fd/2'; \  
echo '</VirtualHost>'; \  
} | tee /etc/apache2/sites-available/000-default.conf \  
&& { \  
echo '#!/bin/bash'; \  
echo 'set -e'; \  
echo; \  
echo '# Apache gets grumpy about PID files pre-existing'; \  
echo 'rm -f /var/run/apache2/apache2.pid'; \  
echo; \  
echo 'exec apache2ctl -DFOREGROUND'; \  
echo; \  
} | tee /usr/local/bin/httpd-foreground \  
&& chmod +x /usr/local/bin/httpd-foreground \  
&& a2enmod rewrite \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install php  
ENV php_version=7.0  
ENV php_config_dir=/etc/php/7.0/  
RUN set -ex \  
&& LANG=C.UTF-8 add-apt-repository -y ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
libapache2-mod-php${php_version} \  
php${php_version}-cli \  
&& a2enmod php${php_version} \  
&& sed -ri \  
-e 's!^;?(\s*log_errors).*!\1 = On!g' \  
-e 's!^;?(\s*error_reporting).*!\1 = E_ALL!g' \  
"${php_config_dir}/apache2/php.ini" "${php_config_dir}/cli/php.ini" \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup the Composer installer  
RUN set -ex \  
&& curl -so /tmp/composer-setup.php http://getcomposer.org/installer \  
&& curl -so /tmp/composer-setup.sig http://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) { echo 'Invalid
installer' . PHP_EOL; exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer \  
&& rm -rf /tmp/composer-setup.*  
  
RUN set -ex \  
&& mkdir -p /var/www/app/web \  
&& echo "<?php phpinfo();" > /var/www/app/web/index.php \  
&& chown www-data:www-data /var/www/app/web/index.php  
  
WORKDIR /var/www/app  
EXPOSE 80  
CMD ["httpd-foreground"]  

