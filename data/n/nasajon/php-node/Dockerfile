FROM alpine:edge  
MAINTAINER Nasajon<devops@nasajon.com.br>  
  
ENV TZ "America/Sao_Paulo"  
  
RUN apk update \  
&& apk add --no-cache \  
tzdata \  
curl \  
vim \  
ca-certificates \  
autoconf file g++ gcc binutils isl libatomic libc-dev musl-dev make re2c
libstdc++ libgcc binutils-libs mpc1 mpfr3 gmp libgomp \  
coreutils \  
freetype-dev \  
libjpeg-turbo-dev \  
libltdl \  
libmcrypt-dev \  
libpng-dev \  
mysql-client \  
nodejs-npm \  
php7-bcmath \  
php7-cli \  
php7-common \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-gd \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-memcached \  
php7-mysqli \  
php7-opcache \  
php7-openssl \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pgsql \  
php7-phar \  
php7-redis \  
php7-simplexml \  
php7-tokenizer \  
php7-xml \  
php7-xmlreader \  
php7-xmlwriter \  
php7-xsl \  
php7-zip \  
php7-zlib && \  
apk add -u musl && \  
apk del autoconf file g++ gcc binutils isl libatomic libc-dev musl-dev make
re2c libstdc++ libgcc binutils-libs mpc1 mpfr3 gmp libgomp && \  
rm -rf /var/cache/apk/*  
  
RUN sed -i -e "s|error_reporting\s*=.*|error_reporting = E_ALL|" \  
-e "s|display_errors\s*=.*|display_errors = On|" \  
-e "s|display_startup_errors\s*=.*|display_startup_errors = On|" \  
-e "s|track_errors\s*=.*|track_errors = On|" \  
-e "s|upload_max_filesize\s*=.*|upload_max_filesize = 100M|" \  
-e "s|date\s*=.*|date = America/Sao_Paulo|" \  
-e "s|max_execution_time\s*=.*|max_execution_time = 90|" \  
-e "s|memory_limit\s*=.*|memory_limit = 256M|" \  
-e "s|;opcache.enable\s*=.*|opcache.enable = 0|" \  
-e "s|;opcache.enable_cli\s*=.*|opcache.enable_cli = 0|" \  
/etc/php7/php.ini  
  
RUN npm install -g yarn  
  
WORKDIR /build  

