FROM tecposter/ubuntu:latest  
  
MAINTAINER "zhanjh@126.com"  
# ref. https://hub.docker.com/_/php/  
  
RUN set -ex \  
  
&& apt-get update \  
&& apt-get upgrade --no-install-recommends --no-install-suggests -y \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
curl pkg-config \  
libmcrypt-dev libxml2-dev libcurl4-openssl-dev libssl-dev libjpeg-dev libpng-
dev libmcrypt-dev libreadline-dev \  
&& build_deps="gcc make build-essential" \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
$build_deps \  
  
&& cd /usr/local/src/ \  
&& curl -SL "http://php.net/distributions/php-7.1.6.tar.gz" -o php7.tar.gz \  
&& tar -zxf php7.tar.gz \  
&& cd php-7.1.6 \  
  
&& ./configure \  
\--prefix=/usr/local \  
\--with-readline \  
\--with-jpeg-dir \  
\--with-png-dir \  
\--enable-fpm \  
\--enable-opcache \  
\--enable-mbstring \  
\--enable-zip \  
\--enable-mysqlnd \  
\--enable-bcmath \  
\--with-gd \  
\--with-openssl \  
\--with-curl \  
\--with-mcrypt \  
\--with-pdo-mysql \  
\--with-fpm-user=www-data \  
\--with-fpm-group=www-data \  
\--with-zlib \  
&& make \  
&& make install \  
  
&& rm -rf /usr/local/src/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove $build_deps  

