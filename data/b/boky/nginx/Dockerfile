FROM alpine:edge  
LABEL maintainer="Bojan Cekrlic (https://github.com/boky8)"  
  
ENV OPENRESTY_VERSION 1.13.6.1  
ENV GLIBC_VERSION 2.27-r0  
  
# Update Alphine, download and install glibc  
RUN true \  
&& apk update && apk upgrade \  
&& apk add curl \  
&& echo " ===> Downloading GLIBC ${GLIBC_VERSION}..." \  
&& curl -C - --retry 5 \--max-time 120 \--connect-timeout 5 -sSL -o glibc.apk
"https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" \  
&& echo " ===> Downloading GLIBC-BIN ${GLIBC_VERSION}..." \  
&& curl -C - --retry 5 \--max-time 120 \--connect-timeout 5 -sSL -o glibc-
bin.apk "https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk" \  
&& echo " ===> Downloading GLIBC-I18N ${GLIBC_VERSION}..." \  
&& curl -C - --retry 5 \--max-time 120 \--connect-timeout 5 -sSL -o
glibc-i18n.apk "https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-i18n-${GLIBC_VERSION}.apk" \  
&& echo " ===> Installing GLIBC..." \  
&& apk add --allow-untrusted glibc.apk \  
&& apk add --allow-untrusted glibc-bin.apk \  
&& apk add --allow-untrusted glibc-i18n.apk \  
&& /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc/usr/lib \  
&& /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 \  
&& ln -sf /usr/glibc-compat/bin/ld /bin/ld \  
&& echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf \  
&& rm -f glibc.apk glibc-bin.apk \  
&& echo " ===> Installing run-time dependecies..." \  
&& apk add bash curl perl unzip ca-certificates openssl pcre zlib openssl
supervisor logrotate xz gd libxslt \  
&& rm -rf /var/cache/apk/* \  
# RUN true \  
&& echo " ===> Downloading GeoIP data..." \  
&& mkdir -p /usr/local/share/GeoIP/ && cd /usr/local/share/GeoIP/ \  
&& curl -C - --retry 5 \--max-time 120 \--connect-timeout 5 -sSL
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz | gunzip
> GeoLiteCity.dat \  
&& curl -C - --retry 5 --max-time 120 --connect-timeout 5 -sSL
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz|
gunzip > GeoIP.dat \  
# RUN true \  
&& mkdir -p "/usr/src" \  
&& echo " ===> Downloading nginx_brotli_module" \  
&& curl -C - --retry 5 \--max-time 120 \--connect-timeout 5 -sSL -o
/tmp/ngx_brotli_module.zip -SL
https://github.com/cloudflare/ngx_brotli_module/archive/master.zip \  
&& cd /tmp && unzip ngx_brotli_module.zip && mv /tmp/ngx_brotli_module-master
/usr/src/ngx_brotli_module \  
&& true \  
&& echo " ===> Downloading brotli compression algorithm" \  
&& curl -C - --retry 5 \--max-time 120 \--connect-timeout 5 -sSL -o
/tmp/brotli.zip
https://github.com/google/brotli/archive/222564a95d9ab58865a096b8d9f7324ea5f2e03e.zip
\  
&& rm -rf /usr/src/ngx_brotli_module/brotli \  
&& cd /usr/src/ngx_brotli_module && unzip /tmp/brotli.zip && mv brotli-*
brotli \  
&& true \  
&& echo " ===> Downloading nginx_ajp_module" \  
&& curl -C - --retry 5 \--max-time 120 \--connect-timeout 5 -sSL -o
/tmp/nginx_ajp_module.zip -SL
https://github.com/yaoweibin/nginx_ajp_module/archive/master.zip \  
&& cd /tmp && unzip nginx_ajp_module.zip && mv /tmp/nginx_ajp_module-master
/usr/src/nginx_ajp_module \  
&& true \  
&& echo " ===> Downloading nginx_upstream_check_module" \  
&& curl -C - --retry 5 \--max-time 120 \--connect-timeout 5 -sSL -o
/tmp/nginx_upstream_check_module.zip -SL
https://github.com/yaoweibin/nginx_upstream_check_module/archive/master.zip \  
&& cd /tmp && unzip nginx_upstream_check_module.zip && mv
/tmp/nginx_upstream_check_module-master /usr/src/nginx_upstream_check_module \  
# RUN true \  
&& echo " ===> Installing dependencies..." \  
&& build_pkgs="build-base linux-headers autoconf automake cmake g++ gcc gd-dev
geoip-dev git libc-dev libtool libxslt-dev make ncurses-dev openssl-dev pcre-
dev perl-dev readline-dev wget zlib-dev" \  
&& addgroup -S nginx && adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G
nginx nginx \  
&& apk add ${build_pkgs} \  
&& true \  
&& echo " ===> Downloading and installing GeoIP" \  
&& cd /tmp \  
&& curl --retry 5 \--max-time 120 \--connect-timeout 5 -sSL
http://geolite.maxmind.com/download/geoip/api/c/GeoIP.tar.gz | tar xvz \  
&& cd GeoIP-* && ./configure && make && make install \  
&& true \  
&& mkdir -p /usr/src/ngx_openresty \  
&& cd /usr/src/ngx_openresty \  
&& echo " ===> Downloading OpenResty ${OPENRESTY_VERSION}..." \  
&& curl -L -sSL
http://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz | tar -xvz
\  
# RUN true \  
&& cd /usr/src/ngx_openresty/openresty-* \  
&& echo " ===> Configuring OpenResty..." \  
&& readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& readonly J_PARRALEL="-j${NPROC}" \  
&& export CXXFLAGS="$CXXFLAGS -fPIC" \  
&& export CFLAGS="$CFLAGS -fPIC" \  
&& echo "using upto $NPROC threads" \  
&& ./configure \  
\--prefix=/usr/local/openresty \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--http-client-body-temp-path=$VAR_PREFIX/client_body_temp \  
\--http-proxy-temp-path=$VAR_PREFIX/proxy_temp \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/lock/nginx.lock \  
\--user=nginx \  
\--group=nginx \  
\--with-threads \  
\--with-file-aio \  
\--with-luajit \  
\--with-pcre-jit \  
\--with-ipv6 \  
\--with-http_iconv_module \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_v2_module \  
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
\--with-http_auth_request_module \  
\--with-http_stub_status_module \  
\--with-http_xslt_module=dynamic \  
\--with-http_image_filter_module=dynamic \  
\--with-http_geoip_module=dynamic \  
\--with-http_perl_module=dynamic \  
\--with-mail \  
\--with-mail_ssl_module \  
\--add-dynamic-module=/usr/src/nginx_ajp_module \  
\--add-module=/usr/src/ngx_brotli_module \  
\--add-dynamic-module=/usr/src/nginx_upstream_check_module \  
\--without-http_ssi_module \  
\--without-http_uwsgi_module \  
\--without-http_scgi_module \  
\--with-cc-opt="-fdiagnostics-color=always -Wno-error" \  
$J_PARRALEL \  
&& cd build/nginx-*/ && ln -sf /usr/src/ngx_brotli_module/brotli . \  
&& cd /usr/src/ngx_openresty/openresty-* \  
&& echo " ===> Building OpenResty..." \  
&& make $J_PARRALEL \  
&& echo " ===> Installing OpenResty..." \  
&& make install \  
&& echo " ===> Finishing up..." \  
&& mkdir -p /usr/local/bin \  
&& ln -sf /usr/sbin/nginx /usr/local/bin/nginx \  
&& ln -sf /usr/sbin/nginx /usr/local/bin/openresty \  
&& ln -sf /usr/local/openresty/bin/resty /usr/local/bin/resty \  
&& ln -sf /usr/local/openresty/luajit/bin/luajit-*
/usr/local/openresty/luajit/bin/lua \  
&& ln -sf /usr/local/openresty/luajit/bin/luajit-* /usr/local/bin/lua \  
&& ln -sf /usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& strip /usr/lib/nginx/modules/*.so \  
&& apk del ${build_pkgs} \  
&& rm -rf /var/cache/apk/* \  
&& (rm -rf /usr/src/ngx_* || true) \  
&& (rm -rf /usr/srct/nginx_* || true) \  
&& (rm -rf /tmp/* || true)  
  
COPY supervisord.conf /etc/supervisord.conf  
COPY logrotate.sh /usr/local/logrotate.sh  
COPY nginx /etc/logrotate.d/nginx  
RUN chmod +x /usr/local/logrotate.sh  
  
EXPOSE 80  
EXPOSE 8080  
EXPOSE 8081  
EXPOSE 443  
EXPOSE 8443  
  
USER root  
WORKDIR /tmp  
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

