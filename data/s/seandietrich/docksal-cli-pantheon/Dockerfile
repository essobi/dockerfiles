FROM docksal/cli:1.2-php7  
  
LABEL maintainer "Sean Dietrich <sean.dietrich@inresonance.com>"  
# Install the PHP extensions we need  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes \--no-install-recommends
install \  
php7.0-dev \  
bzip2 \  
libbz2-dev \  
libc-client2007e-dev \  
libjpeg-dev \  
libkrb5-dev \  
libldap2-dev \  
libmagickwand-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
xfonts-base \  
xfonts-75dpi \  
wkhtmltopdf \  
&& pecl install imagick \  
&& pecl install oauth-2.0.2 \  
&& pecl install redis-3.0.0 \  
&& mkdir -p /srv/bin \  
&& cd /srv/bin \  
&& curl -fsSL
"https://github.com/Medium/phantomjs/releases/download/v2.1.1/phantomjs-2.1.1-linux-x86_64.tar.bz2"
| tar -xjv \  
&& mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /srv/bin/phantomjs \  
&& rm -rf phantomjs-2.1.1-linux-x86_64 && rm -f
phantomjs-2.1.1-linux-x86_64.tar.bz2 \  
&& chmod +x /srv/bin/phantomjs \  
&& apt-get -y clean \  
&& apt-get -y autoclean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/lists/* && rm -rf && rm -rf /var/lib/cache/* && rm -rf
/var/lib/log/* && rm -rf /tmp/*  
  
COPY config/php/php.ini /etc/php/7.0/fpm/php.ini  
COPY config/php/php-cli.ini /etc/php/7.0/cli/php.ini  
  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN mkdir -p /opt/php  
COPY config/php/prepend.php /opt/php/prepend.php  
  
COPY auth_terminus.sh /opt/auth_terminus.sh  
  
RUN chmod 777 /opt  
  
USER docker  
  
# Install Terminus  
RUN composer create-project -d /opt --prefer-dist --no-dev pantheon-
systems/terminus:^1  
  
RUN mkdir -p ~/.terminus/plugins  
  
# Install Terminus Rsync  
RUN composer create-project --no-dev -d ~/.terminus/plugins pantheon-
systems/terminus-rsync-plugin:~1  
  
ENV PATH="/opt/terminus/bin:${PATH}" \  
FRAMEWORK=drupal8 \  
PANTHEON_SITE=docksal \  
PANTHEON_ENVIRONMENT=docksal \  
PANTHEON_BINDING=docksal \  
PANTHEON_DATABASE_HOST=db \  
PANTHEON_DATABASE_PORT=3306 \  
PANTHEON_DATABASE_USERNAME=user \  
PANTHEON_DATABASE_PASSWORD=user \  
PANTHEON_DATABASE_DATABASE=default \  
DRUPAL_HASH_SALT="some random salt"  

