FROM alpine:latest AS pagespeed  
  
# This sadly requires an old version of
http://www.libpng.org/pub/png/libpng.html  
ARG LIBPNG_VERSION=1.2.59  
  
# Check https://github.com/pagespeed/ngx_pagespeed/releases for the latest
version  
ARG NGX_PAGESPEED_VERSION=1.12.34.3  
ARG PAGESPEED_VERSION=1.12.34.3  
  
# Number of CPUs during compile time  
ARG CPU=4  
  
RUN set -x && \  
apk \--no-cache add \  
apache2-dev \  
apr-dev \  
apr-util-dev \  
build-base \  
ca-certificates \  
curl \  
tar \  
icu-dev \  
libjpeg-turbo-dev \  
linux-headers \  
gperf \  
libressl-dev \  
pcre-dev \  
python \  
zlib-dev  
  
# Build libpng  
RUN cd /tmp && \  
curl -L
http://prdownloads.sourceforge.net/libpng/libpng-${LIBPNG_VERSION}.tar.gz |
tar -zx && \  
cd /tmp/libpng-${LIBPNG_VERSION} && \  
./configure \--build=$CBUILD \--host=$CHOST \--prefix=/usr \--enable-shared
\--with-libpng-compat && \  
make install V=0 -j$CPU  
  
  
# Build PageSpeed  
COPY mod-pagespeed-beta-1.12.34.3.tar.bz2 patches/*.patch /tmp/  
  
RUN cd /tmp && \  
mkdir modpagespeed && \  
tar -jxf mod-pagespeed-beta-1.12.34.3.tar.bz2 \--strip-components=1 -C
modpagespeed && \  
cd modpagespeed && \  
patch -p1 < /tmp/automatic_makefile.patch && \  
patch -p1 < /tmp/libpng_cflags.patch && \  
patch -p1 < /tmp/pthread_nonrecursive_np.patch && \  
patch -p1 < /tmp/rename_c_symbols.patch && \  
patch -p1 < /tmp/stack_trace_posix.patch && \  
./generate.sh -D use_system_libs=1 -D _GLIBCXX_USE_CXX11_ABI=0 -D
use_system_icu=1 && \  
cd /tmp/modpagespeed/src && \  
make BUILDTYPE=Release CXXFLAGS=" -I/usr/include/apr-1
-I/tmp/libpng-${LIBPNG_VERSION} -fPIC -DUCHAR_TYPE=uint16_t
-D_GLIBCXX_USE_CXX11_ABI=0" CFLAGS=" -I/usr/include/apr-1
-I/tmp/libpng-${LIBPNG_VERSION} -fPIC -D_GLIBCXX_USE_CXX11_ABI=0" -j$CPU && \  
cd /tmp/modpagespeed/src/pagespeed/automatic/ && \  
make psol BUILDTYPE=Release CXXFLAGS=" -I/usr/include/apr-1
-I/tmp/libpng-${LIBPNG_VERSION} -fPIC -DUCHAR_TYPE=uint16_t
-D_GLIBCXX_USE_CXX11_ABI=0" CFLAGS=" -I/usr/include/apr-1
-I/tmp/libpng-${LIBPNG_VERSION} -fPIC -D_GLIBCXX_USE_CXX11_ABI=0" -j$CPU  
  
RUN mkdir -p /tmp/ngx_pagespeed/psol && \  
mkdir -p /tmp/ngx_pagespeed/psol/lib/Release/linux/x64 && \  
mkdir -p /tmp/ngx_pagespeed/psol/include/out/Release && \  
curl -L https://github.com/apache/incubator-pagespeed-
ngx/archive/v${NGX_PAGESPEED_VERSION}-stable.tar.gz | tar -zx \--strip-
components=1 -C /tmp/ngx_pagespeed && \  
cp -r /tmp/modpagespeed/src/out/Release/obj
/tmp/ngx_pagespeed/psol/include/out/Release/ && \  
cp -r /tmp/modpagespeed/src/net /tmp/ngx_pagespeed/psol/include/ && \  
cp -r /tmp/modpagespeed/src/testing /tmp/ngx_pagespeed/psol/include/ && \  
cp -r /tmp/modpagespeed/src/pagespeed /tmp/ngx_pagespeed/psol/include/ && \  
cp -r /tmp/modpagespeed/src/third_party /tmp/ngx_pagespeed/psol/include/ && \  
cp -r /tmp/modpagespeed/src/tools /tmp/ngx_pagespeed/psol/include/ && \  
cp -r /tmp/modpagespeed/src/pagespeed/automatic/pagespeed_automatic.a
/tmp/ngx_pagespeed/psol/lib/Release/linux/x64 && \  
cp -r /tmp/modpagespeed/src/url /tmp/ngx_pagespeed/psol/include/  
  
  
FROM alpine:latest AS nginx  
# Check https://github.com/pagespeed/ngx_pagespeed/releases for the latest
version  
# Check http://nginx.org/en/download.html for the latest version.  
ARG NGINX_VERSION=1.12.2  
  
# Number of CPUs during compile time  
ARG CPU=4  
  
RUN set -x && \  
apk \--no-cache add \  
apache2-dev \  
apr-dev \  
apr-util-dev \  
build-base \  
ca-certificates \  
curl \  
tar \  
icu-dev \  
libjpeg-turbo-dev \  
linux-headers \  
libressl-dev \  
pcre-dev \  
zlib-dev  
  
COPY \--from=pagespeed /usr/lib/libpng* /usr/lib/  
COPY \--from=pagespeed /tmp/ngx_pagespeed /tmp/ngx_pagespeed/  
# Build Nginx with support for PageSpeed  
RUN cd /tmp && \  
curl -L http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar -zx && \  
cd /tmp/nginx-${NGINX_VERSION} && \  
./configure \  
\--prefix=/var/lib/nginx \  
\--sbin-path=/usr/sbin \  
\--modules-path=/usr/lib/nginx \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_gzip_static_module \  
\--with-file-aio \  
\--with-http_v2_module \  
\--without-http_autoindex_module \  
\--without-http_browser_module \  
\--without-http_geo_module \  
\--without-http_memcached_module \  
\--without-http_userid_module \  
\--without-mail_pop3_module \  
\--without-mail_imap_module \  
\--without-mail_smtp_module \  
\--without-http_split_clients_module \  
\--without-http_scgi_module \  
\--without-http_referer_module \  
\--without-http_upstream_ip_hash_module \  
\--prefix=/etc/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--pid-path=/var/run/nginx.pid \  
\--add-module=/tmp/ngx_pagespeed\  
\--with-cc-opt="-fPIC -I /usr/include/apr-1" \  
\--with-ld-opt="-Wl,--start-group -luuid -lapr-1 -laprutil-1 -licudata -licuuc
-lpng12 -lturbojpeg -ljpeg" && \  
make install \--silent -j$CPU  
  
  
FROM alpine:latest  
MAINTAINER Nico Berlee <nico@berlee.nl>  
  
RUN apk \--no-cache add \  
libuuid \  
apr \  
apr-util \  
libjpeg-turbo \  
icu \  
icu-libs \  
pcre \  
zlib  
  
COPY \--from=pagespeed /usr/lib/libpng* /usr/lib/  
COPY \--from=nginx /usr/sbin/nginx /usr/sbin/nginx  
COPY \--from=nginx /var/log/nginx /var/log/nginx/  
COPY \--from=nginx /etc/nginx /etc/nginx  
# forward request and error logs to docker log collector  
# Make PageSpeed cache writable  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
mkdir -p /var/cache/ngx_pagespeed && \  
chmod -R o+wr /var/cache/ngx_pagespeed  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  
  

