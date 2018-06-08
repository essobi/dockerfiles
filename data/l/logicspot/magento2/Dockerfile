FROM ubuntu:14.04  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
COPY config /  
  
# Update repositories  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >>
/etc/apt/sources.list \  
&& apt-key adv \--keyserver keyserver.ubuntu.com \--recv-keys E5267A6C \  
&& apt-get update  
  
# Install system apps  
RUN apt-get -o Dpkg::Options::=\--force-confdef -y install supervisor curl
wget telnet vim git \  
&& locale-gen en_GB.utf8 \  
&& chmod -R 755 /init /hooks \  
&& chmod 755 /etc/supervisor/exit_on_fatal.py  
# Install nginx  
RUN apt-get install \--no-install-recommends \--no-install-suggests -y \  
ca-certificates \  
nginx \  
gettext-base \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& sed -i -e 's/gzip on/#gzip on/' /etc/nginx/nginx.conf \  
&& sed -i -e 's/gzip_disable/#gzip_disable/' /etc/nginx/nginx.conf \  
&& rm /etc/nginx/sites-available/* /etc/nginx/sites-enabled/default \  
&& mkdir -p /var/www/html \  
&& chmod 777 /var/www/html /var/lib/nginx \  
&& chmod 755 /var/www \  
&& chmod 666 /etc/nginx/sites-enabled/site.conf  
# Install PHP 7.1  
RUN apt-get install -y php7.1-cli php7.1-fpm php7.1-common php7.1-curl
php7.1-gd php7.1-mysql php7.1-soap php7.1-xml php7.1-zip php7.1-gettext
php7.1-mbstring php7.1-mcrypt php7.1-intl php7.1-imap php7.1-bcmath php-
imagick php-xdebug \  
&& sed -i -e 's/max_execution_time = 30/max_execution_time = 300/g'
/etc/php/7.1/fpm/php.ini \  
&& sed -i -e 's/upload_max_filesize = 2M/upload_max_filesize = 50M/g'
/etc/php/7.1/fpm/php.ini \  
&& sed -i -e 's/post_max_size = 8M/post_max_size = 50M/g'
/etc/php/7.1/fpm/php.ini \  
&& sed -i -e '/sendfile on;/a\ fastcgi_read_timeout 300\;'
/etc/nginx/nginx.conf \  
&& sed -i -e 's/;php_admin_value\\[error_log\\]/php_admin_value[error_log]/'
/etc/php/7.1/fpm/pool.d/www.conf \  
&& sed -i -e 's/;php_admin_flag\\[log_errors\\]/php_admin_flag[log_errors]/'
/etc/php/7.1/fpm/pool.d/www.conf \  
&& sed -i -e 's/;php_admin_value\\[memory_limit\\] =
32M/php_admin_value[memory_limit] = 256M/' /etc/php/7.1/fpm/pool.d/www.conf \  
&& echo "xdebug.max_nesting_level = 200;" >> /etc/php/7.1/mods-
available/xdebug.ini \  
&& echo "xdebug.remote_enable = on;" >> /etc/php/7.1/mods-available/xdebug.ini
\  
&& echo "xdebug.remote_connect_back = on;" >> /etc/php/7.1/mods-
available/xdebug.ini \  
&& echo "xdebug.remote_port = 9000;" >> /etc/php/7.1/mods-available/xdebug.ini
\  
&& echo "xdebug.idekey = = PHP_STORM;" >> /etc/php/7.1/mods-
available/xdebug.ini \  
&& phpdismod -s cli xdebug \  
&& mkdir \--mode 777 /var/run/php  
# Install composer  
RUN mkdir /tmp/composer/ \  
&& cd /tmp/composer \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod a+x /usr/local/bin/composer \  
&& rm -rf /tmp/composer  
# Install ioncube  
RUN mkdir -p /usr/src/tmp/ioncube \  
&& curl -fSL
"http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz"
-o /usr/src/tmp/ioncube_loaders_lin_x86-64.tar.gz \  
&& tar xfz /usr/src/tmp/ioncube_loaders_lin_x86-64.tar.gz -C
/usr/src/tmp/ioncube \  
&& cp /usr/src/tmp/ioncube/ioncube/ioncube_loader_lin_7.1.so
/usr/lib/php/20151012/ \  
&& rm -rf /usr/src/tmp/  
# Install WP-CLI  
RUN mkdir /tmp/wpcli/ \  
&& cd /tmp/wpcli \  
&& curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp-cli \  
&& rm -rf /tmp/wpcli  
# Install npm and grunt  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs  
  
# Clean up  
RUN apt-get autoremove -y \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN chmod +x /usr/local/bin/*  
  
# forward request and error logs to docker log collector  
#RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
# && ln -sf /dev/stderr /var/log/nginx/error.log  
  
ENTRYPOINT ["/bin/bash", "-e", "/init/entrypoint"]  
CMD ["run"]  
  
EXPOSE 80 443 35729

