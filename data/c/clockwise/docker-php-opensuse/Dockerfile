FROM opensuse:42.2  
RUN zypper install -y openssl-devel \  
gcc gcc-c++ libxml2-devel pkgconfig libbz2-devel curl-devel libwebp-devel \  
libpng12-devel libpng16-devel libjpeg62-devel libxmp-devel freetype-devel \  
gmp-devel gd-devel libmcrypt-devel freetype2-devel imap-devel \  
aspell-devel recode-devel autoconf bison re2c libicu-devel \  
libbz2-devel libedit-devel libevent-devel db-devel gmp-devel krb5-devel \  
libicu-devel libjpeg-devel libmcrypt-devel libopenssl-devel libpng-devel \  
libtidy-devel libtiff-devel libtool libxslt-devel  
  
RUN zypper install -y zlib-devel zip git unzip p7zip unrar wget make  
  
RUN mkdir -p /opt/php-7.1  
RUN mkdir /usr/local/src/php7-build  
RUN wget http://php.net/get/php-7.1.14.tar.bz2/from/this/mirror -O
/usr/local/src/php7-build/php-7.1.14.tar.bz2  
RUN cd /usr/local/src/php7-build && tar jxf
/usr/local/src/php7-build/php-7.1.14.tar.bz2  
  
RUN cd /usr/local/src/php7-build/php-7.1.14 && \  
./configure --prefix=/opt/php-7.1 --with-zlib-dir --with-freetype-dir
--enable-mbstring \  
\--with-libxml-dir=/usr --enable-soap --enable-intl --enable-calendar --with-
curl --with-mcrypt --with-zlib \  
\--with-gd --disable-rpath --enable-inline-optimization --with-bz2 --with-zlib
--enable-sockets \  
\--enable-sysvsem --enable-sysvshm --enable-pcntl --enable-mbregex --enable-
exif --enable-bcmath --with-mhash \  
\--enable-zip --with-pcre-regex --with-pdo-mysql --with-mysqli --with-mysql-
sock=/var/run/mysql/mysql.sock \  
\--with-webp-dir=/usr --with-jpeg-dir=/usr --with-png-dir=/usr --enable-gd-
native-ttf \  
\--with-openssl --with-fpm-user=www --with-fpm-group=www --with-libdir=lib64
--enable-ftp --with-imap \  
\--with-imap-ssl --with-kerberos --with-gettext --with-xmlrpc --with-xsl
--enable-opcache --enable-fpm \  
\--enable-debug && \  
make && \  
make install  
  
RUN cp /usr/local/src/php7-build/php-7.1.14/php.ini-production
/opt/php-7.1/lib/php.ini  
RUN cp /opt/php-7.1/etc/php-fpm.conf.default /opt/php-7.1/etc/php-fpm.conf  
RUN cp /opt/php-7.1/etc/php-fpm.d/www.conf.default /opt/php-7.1/etc/php-
fpm.d/www.conf  
  
RUN cd /usr/bin && ln -s /opt/php-7.1/bin/php php  
  
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');"  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer && \  
rm -rf /tmp/composer-setup.php  
  
RUN php -r "copy('https://phar.phpunit.de/phpunit.phar','/tmp/phpunit.phar');"  
RUN chmod +x /tmp/phpunit.phar  
RUN mv /tmp/phpunit.phar /usr/local/bin/phpunit  
  
ENV TIMEZONE UTC  
RUN echo "${TIMEZONE}" > /etc/timezone  
  
RUN wget http://pear.php.net/go-pear.phar  
RUN php go-pear.phar  
  
RUN cd /usr/bin && ln -s /opt/php-7.1/bin/pear pear  
  
ENV PATH=$PATH:/opt/php-7.1/bin  
ENV PATH=$PATH:/opt/php-7.1/sbin/  
  
RUN pear config-set php_ini `php --ini | grep "Loaded Configuration" | sed -e
"s|.*:\s*||"` system  
  
RUN useradd -g www www  
  
# set locale to utf-8  
RUN zypper install -y glibc-locale  
ENV LC_ALL en_US.utf8  
ENV LANG en_US.utf8  
ENV LANGUAGE en_US.utf8  
  
RUN touch /opt/php-7.1/etc/php-fpm.d/docker.conf  
RUN touch /opt/php-7.1/etc/php-fpm.d/zz-docker.conf  
  
RUN { \  
echo '[global]'; \  
echo 'error_log = /proc/self/fd/2'; \  
echo; \  
echo '[www]'; \  
echo '; if we send this to /proc/self/fd/1, it never appears'; \  
echo 'access.log = /proc/self/fd/2'; \  
echo; \  
echo 'clear_env = no'; \  
echo; \  
echo '; Ensure worker stdout and stderr are sent to the main error log.'; \  
echo 'catch_workers_output = yes'; \  
} | tee /opt/php-7.1/etc/php-fpm.d/docker.conf \  
&& { \  
echo '[global]'; \  
echo 'daemonize = no'; \  
echo; \  
echo '[www]'; \  
echo 'listen = 9000'; \  
} | tee /opt/php-7.1/etc/php-fpm.d/zz-docker.conf  
  
WORKDIR /var/www  
  
EXPOSE 9000  
CMD ["php-fpm"]

