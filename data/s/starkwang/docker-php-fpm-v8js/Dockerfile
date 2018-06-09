FROM ubuntu:14.04.1  
MAINTAINER devdocker <www.devdocker.com>  
  
ENV PATH $PATH:/root/.composer/vendor/bin  
  
# Install PHP7  
RUN apt-get install -y language-pack-en-base && \  
export LC_ALL=en_US.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --force-yes supervisor git python \  
gcc make g++ wget vim nginx curl chrpath \  
libicu-dev \  
libmcrypt-dev \  
zlib1g-dev \  
\--no-install-recommends \  
php7.0 \  
php7.0-cli \  
php7.0-fpm \  
php7.0-mysql \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-json \  
php7.0-dev \  
php7.0-odbc \  
php7.0-opcache \  
php7.0-xml \  
php7.0-xsl \  
php7.0-gd \  
php7.0-zip \  
php7.0-curl \  
  
# Don't clear our valuable environment vars in PHP  
&& echo "\nclear_env = no" >> /usr/local/etc/php-fpm.conf \  
  
# Fix write permissions with shared folders  
&& usermod -u 1000 www-data  
  
  
  
  
# install dependencies  
RUN apt-get clean  
  
# depot tools  
RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
/usr/local/depot_tools  
ENV PATH $PATH:/usr/local/depot_tools  
  
# install v8  
RUN cd /usr/local/src && fetch v8 && \  
cd /usr/local/src/v8 && git checkout 4.9.111 && gclient sync && make
x64.release library=shared snapshot=off -j4 && \  
mkdir -p /usr/local/lib && \  
cp /usr/local/src/v8/out/x64.release/lib.target/lib*.so /usr/local/lib && \  
echo "create /usr/local/lib/libv8_libplatform.a\naddlib
/usr/local/src/v8/out/x64.release/obj.target/tools/gyp/libv8_libplatform.a\nsave\nend"
| ar -M && \  
cp -R /usr/local/src/v8/include /usr/local && \  
chrpath -r '$ORIGIN' /usr/local/lib/libv8.so && \  
rm -fR /usr/local/src/v8  
  
# get v8js, compile and install  
ENV NO_INTERACTION 1  
RUN git clone https://github.com/preillyme/v8js.git /usr/local/src/v8js && \  
cd /usr/local/src/v8js && phpize && ./configure --with-v8js=/usr/local && \  
make all test install && \  
echo extension=v8js.so > /etc/php/7.0/cli/conf.d/99-v8js.ini && \  
echo extension=v8js.so > /etc/php/7.0/fpm/conf.d/99-v8js.ini && \  
chmod 0777 /etc/php/7.0/fpm/conf.d/99-v8js.ini && \  
chmod 0777 /etc/php/7.0/cli/conf.d/99-v8js.ini && \  
rm -fR /usr/local/src/v8js  
# service nginx reload  
# Next composer and global composer package, as their versions may change from
time to time  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer.phar \  
&& composer.phar global require --no-progress "fxp/composer-asset-
plugin:~1.2.0" \  
&& composer.phar global require --no-progress "codeception/codeception=2.0.*"
\  
&& composer.phar global require --no-progress "codeception/specify=*" \  
&& composer.phar global require --no-progress "codeception/verify=*"  
  
# Nginx example config and composer wrapper  
COPY nginx /opt/nginx  
COPY composer /usr/local/bin/composer  
  
WORKDIR /var/www/html  
  
# Composer packages are installed outside the app directory /var/www/html.  
# This way developers can mount the source code from their host directory  
# into /var/www/html and won't end up with an empty vendors/ directory.  
COPY composer.json /var/www/html/  
COPY composer.lock /var/www/html/  
RUN composer install --prefer-dist --no-progress \  
&& rm composer.*  
  
EXPOSE 9000  
CMD ["php-fpm"]

