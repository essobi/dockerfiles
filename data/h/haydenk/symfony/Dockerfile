FROM haydenk/animated-waddle:apache  
  
ENV XDEBUG_VERSION 2.5.0  
RUN yum install -y \  
vim \  
zlib1g-devel \  
libicu-devel \  
zip \  
gcc-c++ \  
htop \  
mariadb-client \  
freetype-devel \  
libjpeg-devel \  
libmcrypt-devel \  
libpng-devel \  
make \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mbstring exif zip opcache
pdo_mysql pcntl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install intl \  
&& rm -fv /etc/httpd/conf.d/welcome.conf && rm -rfv /usr/share/httpd/noindex \  
&& mkdir -p /usr/src/php/ext/xdebug && cd $_ \  
&& curl https://xdebug.org/files/xdebug-$XDEBUG_VERSION.tgz | tar --strip-
components=1 -xzv \  
&& docker-php-ext-configure xdebug && docker-php-ext-install xdebug \  
&& { \  
echo 'xdebug.default_enable=1'; \  
echo 'xdebug.remote_enable=1'; \  
echo 'xdebug.remote_handler=dbgp'; \  
echo 'xdebug.remote_autostart=0'; \  
echo 'xdebug.remote_connect_back=1'; \  
echo 'xdebug.remote_port=9000'; \  
echo "xdebug.remote_host=127.0.0.1"; \  
echo 'xdebug.profiler_enable=0'; \  
echo 'xdebug.profiler_enable_trigger=1'; \  
echo 'xdebug.profiler_output_dir="/tmp"'; \  
echo 'xdebug.max_nesting_level=1200'; \  
} >> /etc/php/conf.d/docker-php-ext-xdebug.ini \  
&& export VERSION=`php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;"` \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/${VERSION} \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so `php -r "echo
ini_get('extension_dir');"`/blackfire.so \  
&& echo "extension=blackfire.so" > /etc/php/conf.d/blackfire.ini \  
&& echo "blackfire.agent_socket=tcp://blackfire:8707" >>
/etc/php/conf.d/blackfire.ini \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& mkdir -p /var/www/html/web && cd $_ && mv ../index.php .  
  
COPY symfony.conf.dist /etc/httpd/conf.d/symfony.conf  
COPY httpd.conf.dist /etc/httpd/conf/httpd.conf  

