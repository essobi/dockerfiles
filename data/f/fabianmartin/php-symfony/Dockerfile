FROM php:7.1  
  
ENV GOSU_VERSION 1.10  
ENV DOCKERIZE_VERSION v0.6.0  
  
RUN set -ex \  
&& fetchDeps='ca-certificates wget' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $fetchDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove $fetchDeps  
  
RUN deps='autoconf make g++ curl libcurl4-gnutls-dev libicu-dev libsqlite3-dev
zlib1g-dev' \  
&& apt-get update \  
&& apt-get install -y $deps \  
&& apt-get install -y git openssh-client \  
&& rm -rf /var/lib/apt/lists/* \  
&& pecl install apcu \  
&& docker-php-ext-enable apcu \  
&& docker-php-ext-install -j$(nproc) curl iconv intl json mbstring opcache
pdo_mysql pdo_sqlite zip \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& apt-get purge -y --auto-remove $deps  
  
ADD conf.d /usr/local/etc/php/conf.d/  
  
RUN groupadd -g 500 symfony \  
&& useradd -u 500 -g symfony -m -d /home/symfony -s /bin/sh symfony \  
&& mkdir /srv/symfony \  
&& chown symfony:symfony /srv/symfony \  
&& mkdir -p /home/symfony/.ssh \  
&& ssh-keyscan github.com >> /home/symfony/.ssh/known_hosts \  
&& chmod 700 /home/symfony/.ssh \  
&& chmod 600 /home/symfony/.ssh/* \  
&& chown symfony:symfony -R /home/symfony  
  
WORKDIR /srv/symfony  
CMD ["/bin/sh"]  

