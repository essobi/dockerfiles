FROM php:7.1-fpm  
MAINTAINER markoos <sergey.semenyuk@gen.tech>  
  
RUN apt-get update && \  
  
toolsDependencies=" \  
rsyslog \  
mysql-client \  
cron \  
htop \  
vim \  
telnet \  
net-tools \  
wget \  
git \  
rssh \  
zip \  
" && \  
  
mainDependencies=" \  
zlib1g-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libicu-dev \  
libpq-dev \  
libxml2-dev \  
libmemcached-dev \  
libgearman-dev \  
librabbitmq-dev \  
libkrb5-dev \  
libsasl2-dev \  
libssl-dev \  
libc-client2007e-dev \  
gnupg \  
gnupg2 \  
gnupg-agent \  
dirmngr \  
" && \  
  
verticaDependencies=" \  
unixodbc \  
unixodbc-dev \  
" && \  
  
nginxDependencies=" \  
libpcre3 \  
libpcre3-dev \  
libgeoip-dev \  
autoconf \  
make \  
build-essential \  
libperl-dev \  
" && \  
  
pythonDependencies=" \  
python-numpy \  
python-gearman \  
" && \  
  
  
apt-get install -y $toolsDependencies $mainDependencies $verticaDependencies
$nginxDependencies $pythonDependencies --no-install-recommends  
  
  
RUN docker-php-ext-configure pdo_odbc --with-pdo-odbc=unixODBC,/usr \  
&& docker-php-ext-install pdo_odbc \  
&& docker-php-ext-configure imap --with-imap-ssl --with-kerberos \  
&& docker-php-ext-install imap \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install sockets intl mcrypt bcmath zip pcntl pdo_mysql
mysqli soap \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-enable opcache \  
&& pecl install memcached && docker-php-ext-enable memcached \  
&& pecl install redis && docker-php-ext-enable redis \  
&& pecl install amqp && docker-php-ext-enable amqp \  
# install gearman  
&& git clone https://github.com/wcgallego/pecl-gearman.git \  
&& ( \  
cd pecl-gearman\  
&& phpize \  
&& ./configure \  
&& make install \  
) \  
&& rm -rf ../pecl-gearman \  
&& docker-php-ext-enable gearman \  
  
### install kafka  
&& git clone https://github.com/edenhill/librdkafka.git \  
&& ( \  
cd librdkafka\  
&& ./configure \  
&& make \  
&& make install \  
) \  
&& rm -rf ../librdkafka \  
&& pecl install rdkafka \  
&& docker-php-ext-enable rdkafka \  
  
&& rm -rf /usr/local/etc/php-fpm.d/*  
VOLUME /usr/local/etc/php-fpm.d  
  
# install pHash-0.9.6  
# && git clone https://github.com/hszcg/pHash-0.9.6.git \  
# && ( \  
# cd pHash-0.9.6/pHash-0.9.6 \  
# && ls -la \  
# && ./configure --enable-openmp=yes --enable-video-hash=no LIBS='-lpthread' \  
# && make && make install \  
# && cd bindings/php && phpize \  
# && ./configure LIBS="-lpthread" \  
# && make && make install \  
# ) \  
# && rm -rf ../../pHash-0.9.6 \  
# && docker-php-ext-enable pHash \  
################## nginx #########################  
ARG NGINX_VERSION  
ENV NGINX_VERSION ${NGINX_VERSION:-1.12.2}  
  
RUN mkdir -p /tmp/nginx \  
&& git clone git://github.com/mailru/graphite-nginx-module /tmp/graphite-
nginx-module \  
&& wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz -O - | tar
-zxf - -C /tmp/nginx --strip=1 \  
&& cd /tmp/nginx && patch -p1 < /tmp/graphite-nginx-
module/graphite_module_v1_7_7.patch && ./configure \  
\--prefix=/usr/share/nginx \  
\--sbin-path=/usr/sbin \  
\--conf-path=/etc/nginx/nginx.conf \  
\--lock-path=/var/lock/nginx.lock \  
\--pid-path=/var/run/nginx.pid \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--add-module=/tmp/graphite-nginx-module \  
\--with-http_ssl_module \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_geoip_module \  
\--with-http_realip_module \  
\--with-http_v2_module \  
\--with-http_sub_module \  
\--with-http_gzip_static_module \  
\--with-http_stub_status_module \  
\--with-http_perl_module \  
&& make -j$(nproc) && make install  
  
  
## Build nghttp2 libraries from source  
#ARG NGHTTP2_RELEASE  
#ENV NGHTTP2_RELEASE ${NGHTTP2_RELEASE:-1.27.0}  
#RUN wget
https://github.com/nghttp2/nghttp2/releases/download/v${NGHTTP2_RELEASE}/nghttp2-${NGHTTP2_RELEASE}.tar.gz
\  
# && tar -xzf nghttp2-${NGHTTP2_RELEASE}.tar.gz \  
# && cd nghttp2-${NGHTTP2_RELEASE} \  
# && ./configure && make && make install && ldconfig  
#RUN apt-get -y install g++ make binutils autoconf automake autotools-dev
libtool pkg-config \  
# libcunit1-dev libev-dev libevent-dev libjansson-dev \  
# libjemalloc-dev cython python3-dev python-setuptools  
## Build curl from source  
#ARG CURL_RELEASE  
#ENV CURL_RELEASE ${CURL_RELEASE:-7.58.0}  
#RUN wget https://curl.haxx.se/download/curl-${CURL_RELEASE}.tar.gz \  
# && tar -xzf curl-${CURL_RELEASE}.tar.gz \  
# && cd curl-${CURL_RELEASE} \  
# && ./configure --with-nghttp2=/usr/local --with-ssl \  
# && make && make install && ldconfig  
###===--- Supervisor  
ARG SUPERVISOR_VERSION  
ENV SUPERVISOR_VERSION ${SUPERVISOR_VERSION:-3.3.3}  
RUN apt-get install -y python-pip \  
&& pip install supervisor==${SUPERVISOR_VERSION} \  
&& pip install superlance \  
&& mkdir -p /etc/supervisor/conf.d \  
&& mkdir -p /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/  
# Clean image  
RUN apt-get clean && rm -rf /var/cache/apt/archives/* /var/www/html/*
/usr/local/src/* /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& apt-get autoremove -y \  
&& echo "export TERM=xterm-256color" >> /root/.bashrc \  
&& echo "export COLUMNS=300" >> /root/.bashrc \  
&& echo "export LINES=50" >> /root/.bashrc  
  
# stty rows 50 && stty cols 300  
# stty size  
  
COPY entrypoint.sh /entrypoint.sh  
#RUN chmod +x /entrypoint.sh  
ENTRYPOINT [""]  
CMD ["/entrypoint.sh"]  

