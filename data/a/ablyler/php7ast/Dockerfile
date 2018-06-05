FROM alpine:3.3  
  
ADD repositories /etc/apk  
  
RUN apk --update add bash \  
wget \  
curl \  
git \  
grep \  
php7 \  
php7-bcmath \  
php7-curl \  
php7-intl \  
php7-json \  
php7-gettext \  
php7-gd \  
php7-ldap \  
php7-mbstring \  
php7-mcrypt \  
php7-mysqlnd \  
php7-opcache \  
php7-openssl \  
php7-pgsql \  
php7-phar \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-session \  
php7-soap \  
php7-sockets \  
php7-sqlite3 \  
php7-tidy \  
php7-xsl \  
php7-xml \  
php7-xmlreader \  
php7-xmlrpc \  
php7-zip \  
php7-zlib  
  
RUN apk --update add bash \  
autoconf \  
make \  
build-base \  
php7-dev && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
wget -O v0.1.1.tar.gz https://github.com/nikic/php-ast/archive/v0.1.1.tar.gz
&& \  
tar -zxvf v0.1.1.tar.gz && \  
cd php-ast-0.1.1 && \  
phpize7 && \  
./configure --prefix=/usr --with-php-config=/usr/bin/php-config7 && \  
make -j3 && \  
make install && \  
cd .. && \  
rm -Rf php-ast-0.1.1 && \  
apk del php7-dev \  
autoconf \  
make \  
build-base  
  
ADD ast.ini /etc/php7/conf.d

