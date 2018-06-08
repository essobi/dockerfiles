FROM nginx:latest  
  
MAINTAINER Mustafa Salim <mustafalim225@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Core  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
git-core \  
openssh-client \  
unzip \  
vim \  
wget  
  
# PHP 7.0  
RUN wget --quiet -O - https://www.dotdeb.org/dotdeb.gpg | apt-key add - \  
&& echo "deb http://packages.dotdeb.org jessie all" | tee
/etc/apt/sources.list.d/php7.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
php7.0-apcu \  
php7.0-bcmath \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-dev \  
php7.0-fpm \  
php7.0-gd \  
php7.0-imagick \  
php7.0-intl \  
php7.0-json \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mongodb \  
php7.0-mysql \  
php7.0-opcache \  
php7.0-pgsql \  
php7.0-redis \  
php7.0-sqlite3 \  
php7.0-xdebug \  
php7.0-xml \  
php7.0-zip  
  
# Config PHP and NGINX  
RUN sed -i "s/pm.max_children = 5/pm.max_children = 50/g"
/etc/php/7.0/fpm/pool.d/www.conf \  
&& sed -i "s/pm.start_servers = 2/pm.start_servers = 10/g"
/etc/php/7.0/fpm/pool.d/www.conf \  
&& sed -i "s/pm.max_spare_servers = 3/pm.max_spare_servers = 15/g"
/etc/php/7.0/fpm/pool.d/www.conf \  
&& mkdir -p /run/php \  
&& chown root:root /run/php \  
&& echo "Asia/Jakarta" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata \  
&& sed -i "s/;date.timezone =.*/date.timezone = Asia\/Jakarta/g"
/etc/php/7.0/fpm/php.ini \  
&& sed -i "s/;date.timezone =.*/date.timezone = Asia\/Jakarta/g"
/etc/php/7.0/cli/php.ini \  
&& sed -i "s/upload_max_filesize =.*/upload_max_filesize = 250M/g"
/etc/php/7.0/fpm/php.ini \  
&& sed -i "s/memory_limit = 128M/memory_limit = 385M/g"
/etc/php/7.0/fpm/php.ini \  
&& sed -i "s/post_max_size =.*/post_max_size = 250M/g"
/etc/php/7.0/fpm/php.ini \  
&& sed -i "s/user = www-data/user = root/g" /etc/php/7.0/fpm/pool.d/www.conf \  
&& sed -i "s/group = www-data/group = root/g" /etc/php/7.0/fpm/pool.d/www.conf
\  
&& sed -i "s/listen.owner = www-data/listen.owner = root/g"
/etc/php/7.0/fpm/pool.d/www.conf \  
&& sed -i "s/listen.group = www-data/listen.group = root/g"
/etc/php/7.0/fpm/pool.d/www.conf  
  
# NodeJS and NPM  
RUN \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs jpegoptim \  
&& npm install -g npm \  
&& npm install -g bower \  
&& npm install -g gulp \  
&& npm install -g webpack \  
&& echo '{ "allow_root": true }' > ~/.bowerrc  
  
# Clear Cache  
RUN apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Working Directory  
RUN mkdir -p /home/projects  
VOLUME /home/projects  
WORKDIR /home/projects  
  
# Docker Container  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

