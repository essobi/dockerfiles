FROM dorapro/official-image:php_5.5-apache  
  
RUN apt-get update \  
&& apt-get install -y \  
git \  
ssl-cert \  
libssl-dev \  
mysql-client \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install \  
gd \  
zip \  
iconv \  
mcrypt \  
mbstring \  
ftp \  
pdo_mysql \  
mysql \  
mysqli  
  
# Xdebug  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
  
# Xdebug CLIの設置  
ENV XDEBUG_CONFIG remote_host=10.254.254.254  
# composer command setup  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
ENV HOME /root  
ENV PATH $HOME/.composer/vendor/bin:$PATH  
  
# entrykit  
ADD
https://github.com/progrium/entrykit/releases/download/v0.4.0/entrykit_0.4.0_Linux_x86_64.tgz
/tmp/entrykit.tgz  
RUN tar -xzf /tmp/entrykit.tgz -C /bin entrykit \  
&& entrykit --symlink \  
&& true  
  
# 設定ファイルの設置  
ENV DOCUMENT_ROOT /var/www/html/public  
COPY conf.d/vhost.conf.tmpl /etc/apache2/sites-enabled/000-default.conf.tmpl  
COPY conf.d/ssl-default.conf.tmpl /etc/apache2/sites-enabled/ssl-
default.conf.tmpl  
COPY conf.d/php.ini /usr/local/etc/php/php.ini  
COPY conf.d/xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
  
# mod_rewrite enabled  
RUN a2enmod rewrite  
  
# mod_ssl enabled  
RUN a2enmod ssl  
  
EXPOSE 80  
EXPOSE 443  
# user id changed  
RUN usermod -u 1000 www-data  
  
ENTRYPOINT ["render", \  
"/etc/apache2/sites-enabled/000-default.conf", \  
"/etc/apache2/sites-enabled/ssl-default.conf", \  
"--", \  
"apache2-foreground" \  
]  

