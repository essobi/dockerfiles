FROM alpine:3.7  
MAINTAINER David Sn "divad.nnamtdeis@gmail.com"  
  
ENV NGINX_VERSION=1.12.2 \  
PAGESPEED_VERSION=1.12.34.3 \  
LIBPNG_VERSION=1.2.56 \  
MAKE_J=4  
  
# Install required build packages  
RUN apk --no-cache add \  
libuuid \  
apr \  
apr-util \  
libjpeg-turbo \  
icu \  
icu-libs \  
pcre \  
zlib  
  
# Compile NGINX + mod_pagespeed from source  
RUN set -x && \  
apk \--no-cache add -t .build-deps \  
apache2-dev \  
apr-dev \  
apr-util-dev \  
build-base \  
ca-certificates \  
curl \  
icu-dev \  
libjpeg-turbo-dev \  
linux-headers \  
libxslt-dev \  
gd-dev \  
geoip-dev \  
gperf \  
libressl-dev \  
pcre-dev \  
python \  
zlib-dev && \  
# Add user and groups for nginx daemon  
addgroup -g 1000 -S www-data && \  
adduser -u 1000 -D -S -h /var/cache/nginx -s /sbin/nologin -G www-data www-
data && \  
cd /tmp && \  
# Build libpng  
# This requires an older version from SourceForge, see:
https://sourceforge.net/projects/libpng/files/  
curl -L
http://prdownloads.sourceforge.net/libpng/libpng-${LIBPNG_VERSION}.tar.gz |
tar -zx && \  
cd /tmp/libpng-${LIBPNG_VERSION} && \  
sed -i 's/wait/echo/' configure && \  
./configure --build=$CBUILD --host=$CHOST --prefix=/usr \--enable-shared
--with-libpng-compat && \  
make install V=0 -j$MAKE_J && \  
cd /tmp && \  
# Build PageSpeed module from source  
# For latest ngx_pagespeed version, check:
https://github.com/pagespeed/ngx_pagespeed/releases  
curl -L https://github.com/We-Amp/ngx-pagespeed-alpine/blob/master/mod-
pagespeed-beta-1.12.34.3.tar.bz2?raw=true | tar -jx && \  
curl -L
https://github.com/pagespeed/ngx_pagespeed/archive/v${PAGESPEED_VERSION}-stable.tar.gz
| tar -zx && \  
mv incubator-pagespeed-ngx-${PAGESPEED_VERSION}-stable/
ngx_pagespeed-${PAGESPEED_VERSION}-stable/ && \  
cd /tmp/modpagespeed-${PAGESPEED_VERSION} && \  
curl -L https://raw.githubusercontent.com/We-Amp/ngx-pagespeed-
alpine/master/patches/automatic_makefile.patch | patch -p1 && \  
curl -L https://raw.githubusercontent.com/We-Amp/ngx-pagespeed-
alpine/master/patches/libpng_cflags.patch | patch -p1 && \  
curl -L https://raw.githubusercontent.com/We-Amp/ngx-pagespeed-
alpine/master/patches/pthread_nonrecursive_np.patch | patch -p1 && \  
curl -L https://raw.githubusercontent.com/We-Amp/ngx-pagespeed-
alpine/master/patches/rename_c_symbols.patch | patch -p1 && \  
curl -L https://raw.githubusercontent.com/We-Amp/ngx-pagespeed-
alpine/master/patches/stack_trace_posix.patch | patch -p1 && \  
./generate.sh -D use_system_libs=1 -D _GLIBCXX_USE_CXX11_ABI=0 -D
use_system_icu=1 && \  
cd /tmp/modpagespeed-${PAGESPEED_VERSION}/src && \  
make BUILDTYPE=Release CXXFLAGS=" -I/usr/include/apr-1
-I/tmp/libpng-${LIBPNG_VERSION} -fPIC -DUCHAR_TYPE=uint16_t
-D_GLIBCXX_USE_CXX11_ABI=0" CFLAGS=" -I/usr/include/apr-1
-I/tmp/libpng-${LIBPNG_VERSION} -fPIC -D_GLIBCXX_USE_CXX11_ABI=0" -j$MAKE_J &&
\  
cd /tmp/modpagespeed-${PAGESPEED_VERSION}/src/pagespeed/automatic/ && \  
make psol BUILDTYPE=Release CXXFLAGS=" -I/usr/include/apr-1
-I/tmp/libpng-${LIBPNG_VERSION} -fPIC -DUCHAR_TYPE=uint16_t
-D_GLIBCXX_USE_CXX11_ABI=0" CFLAGS=" -I/usr/include/apr-1
-I/tmp/libpng-${LIBPNG_VERSION} -fPIC -D_GLIBCXX_USE_CXX11_ABI=0" -j$MAKE_J &&
\  
mkdir -p /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable/psol && \  
mkdir -p
/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable/psol/lib/Release/linux/x64 && \  
mkdir -p
/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable/psol/include/out/Release && \  
cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/out/Release/obj
/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable/psol/include/out/Release/ && \  
cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/net
/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable/psol/include/ && \  
cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/testing
/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable/psol/include/ && \  
cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/pagespeed
/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable/psol/include/ && \  
cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/third_party
/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable/psol/include/ && \  
cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/tools
/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable/psol/include/ && \  
cp -r
/tmp/modpagespeed-${PAGESPEED_VERSION}/src/pagespeed/automatic/pagespeed_automatic.a
/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable/psol/lib/Release/linux/x64 && \  
cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/url
/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable/psol/include/ && \  
cd /tmp && \  
# Build nginx with PageSpeed module  
# For latest nginx version, check: http://nginx.org/en/download.html  
curl -L http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar -zx && \  
cd /tmp/nginx-${NGINX_VERSION} && \  
./configure \  
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
\--add-module=/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-stable \  
\--with-cc-opt="-fPIC -I /usr/include/apr-1" \  
\--with-ld-opt="-Wl,--start-group -luuid -lapr-1 -laprutil-1 -licudata -licuuc
-lpng12 -lturbojpeg -ljpeg" && \  
make install --silent -j$MAKE_J && \  
# Clean-up temporary files  
cd && \  
apk del .build-deps && \  
rm -rf /tmp/* && \  
# Forward request and error logs to docker log collector  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
# Make PageSpeed cache writable:  
mkdir -p /var/cache/ngx_pagespeed && \  
chmod -R o+wr /var/cache/ngx_pagespeed  
  
# Copy configuration files  
COPY config/conf.d /etc/nginx/conf.d  
COPY config/nginx.conf /etc/nginx/nginx.conf  
  
# Open ports and start nginx  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

