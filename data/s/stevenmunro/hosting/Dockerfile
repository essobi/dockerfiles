# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to `latest`! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
FROM phusion/baseimage:0.10.0  
  
MAINTAINER Medieval <support@medievalwp.co.nz>  
  
# http://phusion.github.io/baseimage-docker/  
# https://hub.docker.com/r/wodby/nginx-php-5.6-alpine/~/dockerfile/  
  
  
RUN \  
  
apt-get update && apt-get -y install \  
htop \  
nano \  
pwgen \  
wget \  
git \  
sed \  
rsync \  
ca-certificates \  
libpcre3 \  
libpcre3-dev \  
libssl-dev \  
dialog \  
imagemagick \  
libmagickwand-dev \  
iputils-ping \  
build-essential \  
autoconf \  
automake \  
g++ \  
libtool \  
make \  
tar \  
libssl-dev \  
pkg-config \  
mysql-client \  
libhyphen-dev \  
memcached \  
libmemcached-tools \  
mysecureshell \  
sudo  
  
RUN apt-get install -y --no-install-recommends expect  
  
  
  
  
RUN apt-get -y purge curl  
  
#setup secureshell  
RUN rm -f /etc/service/sshd/down  
RUN chmod 4755 /usr/bin/mysecureshell && \  
wget -O /etc/ssh/sftp_config
https://gist.githubusercontent.com/stevenmunro/9c9fcaddfad441f2822e1dd5f4aeab0a/raw/  
# Build nghttp2 libraries from source  
ARG NGHTTP2_RELEASE  
ENV NGHTTP2_RELEASE ${NGHTTP2_RELEASE:-v1.26.0}  
  
RUN mkdir -p /usr/local/src/nghttp2 && cd /usr/local/src/nghttp2 && \  
wget -qO- https://github.com/nghttp2/nghttp2/archive/${NGHTTP2_RELEASE}.tar.gz
| \  
tar -xzf - --directory=/usr/local/src/nghttp2 --strip-components=1 && \  
autoreconf -i -I /usr/share/aclocal/ && automake && autoconf && \  
./configure && \  
make && make install  
  
# Build curl from source  
ARG CURL_RELEASE  
ENV CURL_RELEASE ${CURL_RELEASE:-curl-7.56.1}  
  
RUN mkdir -p /usr/local/src/curl && cd /usr/local/src/curl && \  
wget -qO- https://curl.haxx.se/download/${CURL_RELEASE}.tar.gz | \  
tar -xzf - --directory=/usr/local/src/curl --strip-components=1 && \  
./buildconf && \  
./configure --enable-ipv6 --enable-threaded-resolver \  
\--with-nghttp2=/usr/local --with-ssl && \  
make && make install  
  
  
  
ARG NGINX_VER=1.13.6  
ARG NGINX_GPG="B0F4253373F8F6F510D42178520A9993A1C052F8"  
ARG BUILD_CORES  
ARG NGINX_CONF="--prefix=/etc/nginx \  
\--sbin-path=/usr/local/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--http-log-path=/nginx/log/nginx_access.log \  
\--error-log-path=/nginx/log/nginx_error.log \  
\--pid-path=/nginx/run/nginx.pid \  
\--lock-path=/nginx/run/nginx.lock \  
\--user=www-data --group=www-data \  
\--with-http_realip_module \  
\--with-http_gunzip_module \  
\--with-http_slice_module \  
\--with-http_gzip_static_module \  
\--with-http_random_index_module \  
\--with-http_secure_link_module \  
\--with-http_stub_status_module \  
\--with-http_auth_request_module \  
\--with-http_addition_module \  
\--with-http_sub_module \  
\--with-http_ssl_module \  
\--with-http_v2_module \  
\--with-http_stub_status_module \  
\--with-http_mp4_module \  
\--with-threads \  
\--with-file-aio \  
\--with-pcre-jit \  
\--with-ipv6 \  
\--without-http_scgi_module \  
\--without-http_uwsgi_module \  
\--without-http_autoindex_module \  
\--without-http_split_clients_module \  
\--without-http_empty_gif_module \  
\--without-http_browser_module \  
\--add-module=/tmp/ngx_cache_purge \  
\--add-module=/tmp/ngx_brotli \  
\--add-module=/tmp/headers-more-nginx-module"  
### Build nginx from source  
RUN NB_CORES=${BUILD_CORES-$(grep -c "processor" /proc/cpuinfo)} \  
&& cd /tmp \  
&& git clone https://github.com/FRiCKLE/ngx_cache_purge --depth=1 \  
&& git clone https://github.com/openresty/headers-more-nginx-module \--depth=1
\  
&& wget http://nginx.org/download/nginx-${NGINX_VER}.tar.gz \  
&& git clone https://github.com/google/ngx_brotli.git --depth=1 \  
&& cd ngx_brotli \  
&& git submodule update --init --recursive \  
&& cd /tmp \  
&& tar xzf nginx-${NGINX_VER}.tar.gz \  
&& cd /tmp/nginx-${NGINX_VER} \  
&& sed -i -e 's/"Server: nginx"/"Server: nginx-medieval"/g'
src/http/ngx_http_header_filter_module.c \  
&& sed -i -e 's/"nginx"/"nginx-medieval"/g'
src/http/v2/ngx_http_v2_filter_module.c \  
&& sed -i -e 's/"nginx\/"/"nginx-medieval \/ "/g' src/core/nginx.h \  
&& sed -i -e "s/\"Server: \" NGINX_VER CRLF/\"Server: Medieval \/
${NGX_VERSION}\" CRLF/g" src/http/ngx_http_header_filter_module.c \  
&& ./configure ${NGINX_CONF} \  
&& make -j ${NB_CORES} \  
&& make install  
  
  
### Add PHP repo  
RUN add-apt-repository -y ppa:ondrej/php \  
&& apt-get update  
  
  
RUN apt-get install -y \  
  
php-pear \  
php-memcached \  
php-redis \  
php-mailparse \  
#php-xdebug \  
php-imagick \  
php-apcu \  
  
php5.6 \  
php5.6-cli \  
php5.6-dev \  
php5.6-gmp \  
php5.6-json \  
php5.6-mysql \  
#php5.6-phpdbg \  
php5.6-snmp \  
php5.6-tidy \  
php5.6-zip \  
php5.6-bcmath \  
php5.6-common \  
php5.6-enchant \  
php5.6-imap \  
php5.6-ldap \  
php5.6-odbc \  
php5.6-pspell \  
php5.6-soap \  
php5.6-xml \  
php5.6-bz2 \  
php5.6-curl \  
php5.6-fpm \  
php5.6-interbase \  
php5.6-mbstring \  
php5.6-opcache \  
php5.6-readline \  
php5.6-sqlite3 \  
php5.6-xmlrpc \  
php5.6-cgi \  
php5.6-dba \  
php5.6-gd \  
php5.6-intl \  
php5.6-mcrypt \  
php5.6-pgsql \  
php5.6-recode \  
php5.6-sybase \  
php5.6-xsl \  
  
php7.0 \  
php7.0-cli \  
php7.0-dev \  
php7.0-gmp \  
php7.0-json \  
php7.0-mysql \  
#php7.0-phpdbg \  
php7.0-snmp \  
php7.0-tidy \  
php7.0-zip \  
php7.0-bcmath \  
php7.0-common \  
php7.0-enchant \  
php7.0-imap \  
php7.0-ldap \  
php7.0-odbc \  
php7.0-pspell \  
php7.0-soap \  
php7.0-xml \  
php7.0-bz2 \  
php7.0-curl \  
php7.0-fpm \  
php7.0-interbase \  
php7.0-mbstring \  
php7.0-opcache \  
php7.0-readline \  
php7.0-sqlite3 \  
php7.0-xmlrpc \  
php7.0-cgi \  
php7.0-dba \  
php7.0-gd \  
php7.0-intl \  
php7.0-mcrypt \  
php7.0-pgsql \  
php7.0-recode \  
php7.0-sybase \  
php7.0-xsl \  
  
php7.1 \  
php7.1-cli \  
php7.1-dev \  
php7.1-gmp \  
php7.1-json \  
php7.1-mysql \  
#php7.1-phpdbg \  
php7.1-snmp \  
php7.1-tidy \  
php7.1-zip \  
php7.1-bcmath \  
php7.1-common \  
php7.1-enchant \  
php7.1-imap \  
php7.1-ldap \  
php7.1-odbc \  
php7.1-pspell \  
php7.1-soap \  
php7.1-xml \  
php7.1-bz2 \  
php7.1-curl \  
php7.1-fpm \  
php7.1-interbase \  
php7.1-mbstring \  
php7.1-opcache \  
php7.1-readline \  
php7.1-sqlite3 \  
php7.1-xmlrpc \  
php7.1-cgi \  
php7.1-dba \  
php7.1-gd \  
php7.1-intl \  
php7.1-mcrypt \  
php7.1-pgsql \  
php7.1-recode \  
php7.1-sybase \  
php7.1-xsl \  
  
php7.2 \  
php7.2-cli \  
php7.2-dev \  
php7.2-gmp \  
php7.2-json \  
php7.2-mysql \  
#php7.2-phpdbg \  
php7.2-snmp \  
php7.2-tidy \  
php7.2-zip \  
php7.2-bcmath \  
php7.2-common \  
php7.2-enchant \  
php7.2-imap \  
php7.2-ldap \  
php7.2-odbc \  
php7.2-pspell \  
php7.2-soap \  
php7.2-xml \  
php7.2-bz2 \  
php7.2-curl \  
php7.2-fpm \  
php7.2-interbase \  
php7.2-mbstring \  
php7.2-opcache \  
php7.2-readline \  
php7.2-sqlite3 \  
php7.2-xmlrpc \  
php7.2-cgi \  
php7.2-dba \  
php7.2-gd \  
php7.2-intl \  
#php7.2-sodium \  
php7.2-pgsql \  
php7.2-recode \  
php7.2-sybase \  
php7.2-xsl  
  
  
### Place files  
ADD install /  
  
### Install composer global bin  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer && chmod +x
/usr/local/bin/composer  
  
### Install wp-cli global bin  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp && chmod +x /usr/local/bin/wp  
  
RUN echo 'www-data ALL=NOPASSWD:/DATA/bin/sftp.sh' | sudo EDITOR='tee -a'
visudo  
  
RUN chmod +x /etc/service/10-nginx/run \  
&& chmod +x /etc/service/20-php-fpm/run \  
&& chmod +x /etc/my_init.d/00-folders.sh \  
&& chmod +x /etc/my_init.d/10-nginx.sh \  
&& chmod +x /etc/my_init.d/20-php-fpm.sh \  
&& chmod +x /etc/my_init.d/30-cron.sh \  
&& chmod +x /etc/my_init.d/40-wordpress.sh \  
&& chmod +x /checksum.sh \  
&& chmod +x /verifycron.sh \  
&& chmod +x /backup-db.sh \  
&& chmod +x /create-user.exp \  
&& chown -R root:root /DATA/bin && chmod +x /DATA/bin/sftp.sh  
  
### Networking Configuration  
EXPOSE 80 22  
### Volume  
VOLUME ["/DATA"]  
  
#RUN apt-get -y purge --auto-remove git *-dev autoconf libtool  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/man /usr/local/src/nghttp2 /usr/local/src/curl  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

