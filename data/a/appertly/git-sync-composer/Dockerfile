FROM appertly/git-sync  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends apt-transport-https lsb-release
ca-certificates wget git \  
&& wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends \  
php7.1-cli php7.1-opcache php7.1-gd php7.1-gmp php7.1-mcrypt php-imagick
php7.1-mbstring php7.1-intl \  
php-memcached php7.1-mysql php7.1-pgsql php7.1-sqlite3 php7.1-curl php7.1-xml
php7.1-zip \  
&& wget https://getcomposer.org/composer.phar -O /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/log/apt/* \  
&& rm -rf /var/log/dpkg.log \  
&& rm -rf /var/log/bootstrap.log \  
&& rm -rf /var/log/alternatives.log \  
&& chmod +x /start.sh  
  
ENV GIT_SYNC_POST_PULL composer install --no-dev --ignore-platform-reqs -o -n  

