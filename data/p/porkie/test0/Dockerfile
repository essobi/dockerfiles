FROM phusion/baseimage:0.9.19  
  
MAINTAINER Porkie  
  
  
# Install Nginx  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C \  
&& echo "deb http://ppa.launchpad.net/nginx/development/ubuntu xenial main" >>
/etc/apt/sources.list \  
&& echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >>
/etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
ca-certificates \  
wget \  
nginx \  
gettext-base \  
git \  
php-pear \  
php7.0 \  
php7.0-cli \  
php7.0-dev \  
php7.0-common \  
php7.0-curl \  
php7.0-json \  
php7.0-gd \  
php7.0-mysql \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-xml\  
php7.0-fpm \  
php7.0-opcache \  
php7.0-bz2 \  
php-imagick \  
unrar \  
time \  
tmux \  
p7zip-full \  
mediainfo \  
lame \  
ffmpeg \  
libav-tools \  
man \  
build-essential \  
curl \  
htop \  
software-properties-common \  
unzip \  
nano \  
ntp \  
ntpdate \  
vnstat \  
tcptrack \  
bwm-ng \  
mytop \  
&& rm -rf /etc/nginx/sites-enabled/default \  
&& mkdir -p /run/php \  
&& sed -i '/^;clear_env = no/s/^;//' /etc/php/7.0/fpm/pool.d/www.conf \  
&& wget -P /usr/local/bin
https://github.com/jwilder/forego/releases/download/v0.16.1/forego \  
&& chmod u+x /usr/local/bin/forego \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& sed -i 's/^http {/&\n server_names_hash_bucket_size 64;/g'
/etc/nginx/nginx.conf \  
&& mkdir -p /var/lib/php/sessions \  
&& chmod -R 777 /var/lib/php/sessions \  
&& mkdir /yenc \  
&& cd /yenc \  
&& wget
http://heanet.dl.sourceforge.net/project/yydecode/yydecode/0.2.10/yydecode-0.2.10.tar.gz
\  
&& tar xzf yydecode-0.2.10.tar.gz \  
&& cd yydecode-0.2.10 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /yenc \  
  
## Install composer  
RUN \  
cd /tmp && \  
chmod 775 /var/www && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'aa96f26c2b67226a324c27919f1eb05f21c248b987e6195cad9690d5c1ff713d53020a02ac8c217dbf90a7eacc9d141d')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar /usr/local/bin/composer  
  
RUN \  
mkdir /app && \  
cd /app && \  
composer create-project --no-dev --keep-vcs --prefer-source nzedb/nzedb nzedb
&& \  
chmod -R 755 /app/nzedb/app/libraries && \  
chmod -R 755 /app/nzedb/libraries && \  
chmod -R 777 /app/nzedb/resources && \  
chmod -R 777 /app/nzedb/www && \  
mv /app/nzedb/resources/covers /app/nzedb/resources/covers-sample && \  
mv /app/nzedb/nzedb/config /app/nzedb/nzedb/config-sample  
  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY Procfile /app/  
COPY 10-linkconfig.sh /app/prerun/  
WORKDIR /app/  
  
COPY default.conf /etc/nginx/conf.d/  
COPY php.ini /etc/php/7.0/fpm/conf.d/40-custom.ini  
  
EXPOSE 8810  
  
VOLUME ['/data', '/config']  
  
CMD ["/usr/local/bin/forego", "start", "-r"]  

