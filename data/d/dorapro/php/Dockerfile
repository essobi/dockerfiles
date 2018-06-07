FROM dorapro/ubuntu:14.04  
  
RUN apt-get update -q && apt-get install -yq --force-yes \--no-install-
recommends software-properties-common curl \  
&& apt-add-repository ppa:ondrej/php -y \  
&& apt-get update \  
&& apt-get install -yq --force-yes \--no-install-recommends \  
php7.0-cli \  
php7.0-dev \  
php-sqlite3 \  
php-gd \  
php-apcu \  
php-json \  
php-curl \  
php-gmp \  
php-imap \  
php-mbstring \  
php-mysql \  
php-memcached \  
php-readline \  
php-xml \  
php-zip \  
php-intl \  
&& apt-get autoremove -qq \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* >/dev/null 2>&1  
  
CMD ["php", "-a"]  

