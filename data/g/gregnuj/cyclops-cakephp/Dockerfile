FROM gregnuj/cyclops-composer:stretch  
  
LABEL MAINTAINER="Greg Junge <gregnuj@gmail.com>"  
  
## Install project requirements  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y \  
libmcrypt-dev \  
libicu-dev \  
libxml2-dev \  
libpq-dev \  
unixodbc-dev \  
libssh2-1-dev \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
## Prepare odbc  
RUN set -ex \  
&& docker-php-source extract \  
&& cd /usr/src/php/ext/odbc \  
&& phpize \  
&& sed -ri 's@^ *test +"\$PHP_.*" *= *"no" *&& *PHP_.*=yes *$@#&@g' configure
\  
&& ./configure --with-unixODBC=shared,/usr \  
&& docker-php-ext-install odbc \  
&& docker-php-source delete  
  
## Install project php extensions  
RUN set -ex \  
&& docker-php-ext-install \  
mcrypt \  
mbstring \  
pdo_mysql \  
pdo_pgsql \  
pdo_odbc \  
intl \  
soap \  
sockets \  
odbc \  
zip  
  
## Install/enable ssh2 extenssion  
RUN pecl install ssh2-1.1.2 \  
&& docker-php-ext-enable ssh2  
  
## cake.php uses /usr/bin/php  
RUN ln -s /usr/local/bin/php /usr/bin/php  

