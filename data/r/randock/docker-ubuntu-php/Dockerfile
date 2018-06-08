FROM ubuntu:yakkety  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install base packages  
RUN locale-gen en_US.UTF-8 \  
&& export LANG=en_US.UTF-8 \  
&& export LC_ALL=en_US.UTF-8 \  
  
&& apt-get update && apt-get install -y software-properties-common \  
&& rm -rf /var/lib/apt/lists/* \  
  
&& add-apt-repository ppa:ondrej/php \  
  
&& apt-get update \  
&& apt-get -yq --allow-unauthenticated install \  
php7.1 \  
php7.1-fpm \  
php7.1-curl \  
php7.1-mysql \  
php7.1-sqlite3 \  
php7.1-intl \  
php7.1-memcached \  
php7.1-memcache \  
php7.1-gd \  
php7.1-apc \  
php7.1-intl \  
php7.1-ldap \  
php7.1-mcrypt \  
php7.1-readline \  
php7.1-xml \  
php7.1-mbstring \  
php7.1-zip \  
php7.1-bcmath \  
php7.1-opcache \  
php7.1-readline \  
php7.1-json \  
php-apcu \  
php-apcu-bc \  
libmaxminddb0 \  
libmaxminddb-dev \  
net-tools \  
mmdb-bin \  
curl \  
zip \  
unzip \  
zsh \  
g++ \  
gcc \  
make \  
libxml2 \  
&& rm -rf /var/lib/apt/lists/* \  
  
&& phpenmod -v 7.1 mcrypt  
  
COPY config/php/php.ini /etc/php7/conf.d/50-setting.ini  
COPY config/php/opcache.ini /etc/php7/cli/conf.d/opcache.ini  
COPY config/php/opcache.ini /etc/php7/fpm/conf.d/opcache.ini  
COPY config/php/php-fpm.conf /etc/php7/php-fpm.conf  
  
CMD ["/usr/sbin/php-fpm7.1", "-R", "--nodaemonize" "--fpm-config"
"/etc/php/7.1/fpm/php-fpm.conf"]

