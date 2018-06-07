FROM php:7.1-fpm-alpine  
# BASE ON https://github.com/docker-library/php  
# INSTALL PYTHON2.7  
# EDIT BY YYY  
ENV PATH /usr/local/bin:$PATH  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# https://github.com/docker-library/python/issues/147  
ENV PYTHONIOENCODING UTF-8  
  
# install ca-certificates so that HTTPS works consistently  
# the other runtime dependencies for Python are installed later  
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g'
/etc/apk/repositories  
RUN apk add --no-cache ca-certificates  
  
ENV GPG_KEY C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF  
ENV PYTHON_VERSION 2.7.15  
  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps \  
gnupg \  
openssl \  
tar \  
xz \  
\  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -rf "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& apk add --no-cache --virtual .build-deps \  
bzip2-dev \  
coreutils \  
dpkg-dev dpkg \  
gcc \  
gdbm-dev \  
libc-dev \  
linux-headers \  
make \  
ncurses-dev \  
openssl \  
openssl-dev \  
pax-utils \  
readline-dev \  
sqlite-dev \  
tcl-dev \  
tk \  
tk-dev \  
zlib-dev \  
# add build deps before removing fetch deps in case there's overlap  
&& apk del .fetch-deps \  
\  
&& cd /usr/src/python \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--enable-shared \  
\--enable-unicode=ucs4 \  
&& make -j "$(nproc)" \  
# set thread stack size to 1MB so we don't segfault before we hit
sys.getrecursionlimit()  
#
https://github.com/alpinelinux/aports/commit/2026e1259422d4e0cf92391ca2d3844356c649d0  
EXTRA_CFLAGS="-DTHREAD_STACK_SIZE=0x100000" \  
&& make install \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --virtual .python-rundeps $runDeps \  
&& apk del .build-deps \  
\  
&& find /usr/local -depth \  
\( \  
\( -type d -a \( -name test -o -name tests \) \) \  
-o \  
\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \  
\) -exec rm -rf '{}' + \  
&& rm -rf /usr/src/python  
  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
  
## INSTALL PYTHON3  
ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D  
ENV PYTHON_VERSION 3.6.5  
  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps \  
gnupg \  
openssl \  
tar \  
xz \  
\  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -rf "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& apk add --no-cache --virtual .build-deps \  
bzip2-dev \  
coreutils \  
dpkg-dev dpkg \  
expat-dev \  
gcc \  
gdbm-dev \  
libc-dev \  
libffi-dev \  
linux-headers \  
make \  
ncurses-dev \  
openssl \  
openssl-dev \  
pax-utils \  
readline-dev \  
sqlite-dev \  
tcl-dev \  
tk \  
tk-dev \  
xz-dev \  
zlib-dev \  
# add build deps before removing fetch deps in case there's overlap  
&& apk del .fetch-deps \  
\  
&& cd /usr/src/python \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--enable-loadable-sqlite-extensions \  
\--enable-shared \  
\--with-system-expat \  
\--with-system-ffi \  
\--without-ensurepip \  
&& make -j "$(nproc)" \  
# set thread stack size to 1MB so we don't segfault before we hit
sys.getrecursionlimit()  
#
https://github.com/alpinelinux/aports/commit/2026e1259422d4e0cf92391ca2d3844356c649d0  
EXTRA_CFLAGS="-DTHREAD_STACK_SIZE=0x100000" \  
&& make install \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --virtual .python-rundeps $runDeps \  
&& apk del .build-deps \  
\  
&& find /usr/local -depth \  
\( \  
\( -type d -a \( -name test -o -name tests \) \) \  
-o \  
\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \  
\) -exec rm -rf '{}' + \  
&& rm -rf /usr/src/python  
## INSTALL PIP  
ENV PYTHON_PIP_VERSION 10.0.1  
  
RUN set -ex; \  
\  
apk add --no-cache --virtual .fetch-deps openssl; \  
\  
wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \  
\  
apk del .fetch-deps; \  
\  
python3 get-pip.py \  
\--disable-pip-version-check \  
\--no-cache-dir \  
"pip==$PYTHON_PIP_VERSION" \  
; \  
python get-pip.py \  
\--disable-pip-version-check \  
\--no-cache-dir \  
"pip==$PYTHON_PIP_VERSION" \  
; \  
pip --version; \  
\  
find /usr/local -depth \  
\( \  
\( -type d -a \( -name test -o -name tests \) \) \  
-o \  
\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \  
\) -exec rm -rf '{}' +; \  
rm -f get-pip.py  
  
## INSTALL SUPERVISOR  
  
RUN pip install supervisor -i http://pypi.douban.com/simple --trusted-host
pypi.douban.com  
  
## INSTALL PYTHON MODULES SUPPORT EUREKA CLIENT DISCOVERY  
RUN pip3 install wasp-eureka asyncio -i http://pypi.douban.com/simple
--trusted-host pypi.douban.com  
  
## INSTALL NGINX  
  
ENV NGINX_VERSION 1.14.0  
  
RUN GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 \  
&& CONFIG="\  
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
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_sub_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_mp4_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_random_index_module \  
\--with-http_secure_link_module \  
\--with-http_stub_status_module \  
\--with-http_auth_request_module \  
\--with-http_xslt_module=dynamic \  
\--with-http_image_filter_module=dynamic \  
\--with-http_geoip_module=dynamic \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-stream_ssl_preread_module \  
\--with-stream_realip_module \  
\--with-stream_geoip_module=dynamic \  
\--with-http_slice_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-compat \  
\--with-file-aio \  
\--with-http_v2_module \  
" \  
&& addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
curl \  
gnupg \  
libxslt-dev \  
gd-dev \  
geoip-dev \  
&& curl -fSL https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& found=''; \  
for server in \  
# ha.pool.sks-keyservers.net \  
hkp://keyserver.ubuntu.com:80 \  
hkp://p80.pool.sks-keyservers.net:80 \  
pgp.mit.edu \  
; do \  
echo "Fetching GPG key $GPG_KEYS from $server"; \  
gpg --keyserver "$server" --keyserver-options timeout=10 --recv-keys
"$GPG_KEYS" && found=yes && break; \  
done; \  
test -z "$found" && echo >&2 "error: failed to fetch GPG key $GPG_KEYS" &&
exit 1; \  
gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -rf "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure $CONFIG --with-debug \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& mv objs/nginx objs/nginx-debug \  
&& mv objs/ngx_http_xslt_filter_module.so objs/ngx_http_xslt_filter_module-
debug.so \  
&& mv objs/ngx_http_image_filter_module.so objs/ngx_http_image_filter_module-
debug.so \  
&& mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \  
&& mv objs/ngx_stream_geoip_module.so objs/ngx_stream_geoip_module-debug.so \  
&& ./configure $CONFIG \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \  
&& install -m755 objs/ngx_http_xslt_filter_module-debug.so
/usr/lib/nginx/modules/ngx_http_xslt_filter_module-debug.so \  
&& install -m755 objs/ngx_http_image_filter_module-debug.so
/usr/lib/nginx/modules/ngx_http_image_filter_module-debug.so \  
&& install -m755 objs/ngx_http_geoip_module-debug.so
/usr/lib/nginx/modules/ngx_http_geoip_module-debug.so \  
&& install -m755 objs/ngx_stream_geoip_module-debug.so
/usr/lib/nginx/modules/ngx_stream_geoip_module-debug.so \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& strip /usr/lib/nginx/modules/*.so \  
&& rm -rf /usr/src/nginx-$NGINX_VERSION \  
\  
# Bring in gettext so we can get `envsubst`, then throw  
# the rest away. To do this, we need to install `gettext`  
# then move `envsubst` out of the way so `gettext` can  
# be deleted completely, then move `envsubst` back.  
&& apk add --no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' /usr/sbin/nginx
/usr/lib/nginx/modules/*.so /tmp/envsubst \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --no-cache --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
\  
# Bring in tzdata so users could set the timezones through the environment  
# variables  
&& apk add --no-cache tzdata \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
## INSTALL COMPOSER && PHP EXT  
RUN php -r "readfile('https://getcomposer.org/installer');" | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer config -g repo.packagist composer
https://packagist.phpcomposer.com \  
&&docker-php-ext-install pdo_mysql bcmath  
  
## START SUPERVISOR  
COPY supervisord.conf /etc/supervisord.conf  
COPY supervisor.conf.d /etc/supervisor.conf.d  
COPY nginx.conf /etc/nginx/nginx.conf  
  
COPY start.sh /start.sh  
RUN chmod a+x /start.sh  
ENTRYPOINT [ "/start.sh"]  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 9001

