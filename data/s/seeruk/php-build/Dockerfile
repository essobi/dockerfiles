FROM ubuntu:xenial  
MAINTAINER Elliot Wright <hello@elliotdwright.com>  
  
COPY provisioning/docker-entrypoint.sh /opt/php-setup/docker-entrypoint.sh  
  
ENV COMPOSER_CACHE_DIR=/tmp/.composer  
ENV GOSU_VERSION 1.10  
ENV PHP_UID 1000  
ENV PHP_GID 1000  
ENV PHP_HOME /home/php  
ENV PHP_WORKDIR /app  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
git-core \  
language-pack-en-base \  
openssh-client \  
software-properties-common \  
wget \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& LC_ALL=en_US.UTF-8 apt-add-repository ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
php5.6 \  
php5.6-cli \  
php5.6-common \  
php5.6-curl \  
php5.6-dev \  
php5.6-fpm \  
php5.6-gd \  
php5.6-imagick \  
php5.6-intl \  
php5.6-json \  
php5.6-mbstring \  
php5.6-mcrypt \  
php5.6-memcached \  
php5.6-mysql \  
php5.6-xml \  
php5.6-zip \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/app/lists/* \  
&& chmod +x /opt/php-setup/docker-entrypoint.sh  
  
WORKDIR /opt/php-setup  
  
ENTRYPOINT ["/opt/php-setup/docker-entrypoint.sh"]  
  
CMD ["php", "-v"]  

