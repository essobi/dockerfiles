FROM node  
  
MAINTAINER "Jacco Meijer" <jacco@thinkbright.nl>  
  
# Install packages needed to get https://www.dotdeb.org/dotdeb.gpg  
RUN \  
apt-get update && \  
apt-get -y install apt-utils wget  
  
# Add PHP  
RUN \  
echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list && \  
echo 'deb-src http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list
&& \  
wget https://www.dotdeb.org/dotdeb.gpg && \  
apt-key add dotdeb.gpg && \  
rm dotdeb.gpg && \  
export CFLAGS="$PHP_CFLAGS" CPPFLAGS="$PHP_CPPFLAGS" LDFLAGS="$PHP_LDFLAGS"  
  
# install packages  
RUN \  
apt-get update && \  
apt-get -y install \  
  
build-essential \  
curl \  
git \  
libatomic-ops-dev \  
libc6 \  
libfontconfig1 \  
libfreetype6 \  
libfreetype6-dev \  
libgd2-xpm-dev \  
libgeoip1 \  
libgeoip-dev \  
libjpeg62-turbo-dev \  
libmagickwand-dev \  
libmcrypt-dev \  
libpcre3 \  
libpcre3-dev \  
libperl-dev \  
libpng12-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
lsb-base \  
mysql-client \  
openssl \  
perl \  
php7.0-cli \  
php7.0-curl \  
php7.0-fpm \  
php7.0-gd \  
php7.0-imagick \  
php7.0-imap \  
php7.0-intl \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-pspell \  
php7.0-recode \  
php7.0-sqlite3 \  
php7.0-tidy \  
php7.0-xmlrpc \  
php7.0-xsl \  
python \  
python-dev \  
python-pip \  
sudo \  
unzip \  
vim \  
wget \  
zlib1g \  
zlib1g-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# Install nginx with pagespeed  
RUN \  
curl -f -L -sS https://ngxpagespeed.com/install > /tmp/ngxpagespeed-install &&
\  
chmod +x /tmp/ngxpagespeed-install && \  
/tmp/ngxpagespeed-install \  
\--nginx-version 1.12.0 \  
\--additional-nginx-configure-arguments ' \  
\--with-http_perl_module \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
\--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
\--user=nginx \  
\--group=nginx \  
\--with-compat \  
\--with-file-aio \  
\--with-threads \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_mp4_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-stream \  
\--with-stream_realip_module \  
\--with-stream_ssl_module \  
\--with-stream_ssl_preread_module \  
\--with-cc-opt="-g -O2 -fstack-protector-strong -Wformat -Werror=format-
security -Wp,-D_FORTIFY_SOURCE=2 -fPIC" \  
\--with-ld-opt="-Wl,-z,relro -Wl,-z,now -Wl,--as-needed -pie" \  
'  
  
# Install npm-check-updates  
RUN npm install -g npm-check-updates  
  
# Install composer  
RUN \  
mkdir -p /usr/local/bin && \  
cd /usr/local/bin && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Copy scripts and config into container  
COPY ./usr-local-bin/ /usr/local/bin/  
COPY ./config-php/ /etc/php/7.0/fpm/conf.d/  
COPY ./config-nginx/ /etc/nginx/  
COPY ./config-imagemagick/policy.xml /etc/ImageMagick-6/  
  
RUN mkdir -p /var/cache/nginx  
RUN mkdir -p /usr/share/nginx  
RUN mv /etc/nginx/html /usr/share/nginx/  
RUN nginx -v  
  
EXPOSE 80  
  
CMD nginx-node-entrypoint.sh  

