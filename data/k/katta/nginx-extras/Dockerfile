FROM debian:jessie  
# runtime nginx dependencies  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get install -q -y
\--no-install-recommends \  
fontconfig-config \  
fonts-dejavu-core \  
fonts-liberation \  
geoip-database \  
init-system-helpers \  
libarchive-extract-perl \  
libbz2-1.0 \  
libc6 \  
libexpat1 \  
libfontconfig1 \  
libfreetype6 \  
libgcc1 \  
libgcrypt20 \  
libgd3 \  
libgdbm3 \  
libgeoip1 \  
libgoogle-perftools4 \  
libgpg-error0 \  
libjbig0 \  
libjpeg62-turbo \  
liblog-message-perl \  
liblog-message-simple-perl \  
liblzma5 \  
libmodule-pluggable-perl \  
libpam0g \  
libpcre3 \  
libpcre3 \  
libperl5.20 \  
libpng12-0 \  
libpod-latex-perl \  
libssl1.0.0 \  
libterm-ui-perl \  
libtext-soundex-perl \  
libtiff5 \  
libvpx1 \  
libx11-6 \  
libx11-data \  
libxau6 \  
libxcb1 \  
libxdmcp6 \  
libxml2 \  
libxpm4 \  
libxslt1.1 \  
perl \  
perl-modules \  
perlapi-5.20.1 \  
rename \  
sgml-base \  
ttf-bitstream-vera \  
ucf \  
xml-core \  
zlib1g \  
&& rm -rf /var/lib/apt/lists/*  
  
  
# prepare Nginx build env  
ENV NGINX_VERSION 1.9.5  
ENV nginxBuildDeps "\  
binutils \  
ca-certificates \  
curl \  
dpkg-dev \  
libgd-dev \  
libgeoip-dev \  
libgoogle-perftools-dev \  
libpcre3-dev \  
libperl-dev \  
libssl-dev \  
libxslt1-dev \  
"  
# see http://nginx.org/en/pgp_keys.html  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -q -y \--no-install-
recommends $nginxBuildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -SL "http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz" -o
nginx.tar.gz \  
&& curl -SL "http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc" -o
nginx.tar.gz.asc \  
&& gpg \--keyserver pgp.mit.edu \--recv-key \  
A09CD539B8BB8CBE96E82BDFABD4D3B3F5806B4D \  
4C2C85E705DC730833990C38A9376139A524C53E \  
B0F4253373F8F6F510D42178520A9993A1C052F8 \  
65506C02EFC250F1B7A3D694ECF0E90B2C172083 \  
7338973069ED3F443F4D37DFA64FD5B17ADB39A8 \  
6E067260B83DCF2CA93C566F518509686C7E5E82 \  
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& gpg \--verify nginx.tar.gz.asc \  
&& mkdir -p /usr/src/nginx \  
&& tar -xf nginx.tar.gz -C /usr/src/nginx \--strip-components=1 \  
&& rm nginx.tar.gz*  
  
# openssl  
ENV OPENSSL_VERSION 1.0.2d  
RUN mkdir -p /usr/src/openssl \  
&& curl -sL https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz |
\  
tar xz -C /usr/src/openssl \--strip-components=1  
# install shared dependencies  
ENV buildDeps "\  
g++ \  
gcc \  
libc6-dev \  
libpcre3-dev \  
libxml2-dev \  
make \  
zlib1g-dev \  
"  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -q -y \--no-install-
recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
# build modsecurity  
ENV MODSECURITY_VERSION 2.9.0  
ENV modsecurityBuildDeps "\  
apache2-prefork-dev \  
libapr1-dev \  
libaprutil1-dev \  
libcurl3-dev \  
"  
# TODO add --disable-mlogc  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get install -q -y
\--no-install-recommends \  
libaprutil1 \  
libpcre3 \  
$modsecurityBuildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/modsecurity \  
&& curl -sL
"https://www.modsecurity.org/tarball/${MODSECURITY_VERSION}/modsecurity-${MODSECURITY_VERSION}.tar.gz"
| \  
tar xz -C /usr/src/modsecurity \--strip-components=1 \  
&& cd /usr/src/modsecurity \  
&& CFLAGS="$(dpkg-buildflags --get CFLAGS)" \  
CPPFLAGS="$(dpkg-buildflags --get CPPFLAGS)" \  
LDFLAGS="$(dpkg-buildflags --get LDFLAGS)" \  
./configure \--enable-standalone-module \--disable-apache2-module
\--prefix=/usr \  
&& make -j"$(nproc)"\  
&& rm -r iis tests  
  
# pagespeed module  
ENV NPS_VERSION 1.9.32.6-beta  
RUN mkdir -p /usr/src/pagespeed \  
&& curl -sL
https://github.com/pagespeed/ngx_pagespeed/archive/release-${NPS_VERSION}.tar.gz
| \  
tar xz -C /usr/src/pagespeed \--strip-components=1 \  
&& mkdir -p /usr/src/pagespeed/psol \  
&& curl -sL https://dl.google.com/dl/page-
speed/psol/${NPS_VERSION%-beta}.tar.gz | \  
tar xz -C /usr/src/pagespeed/psol \--strip-components=1  
# devel kit module  
ENV DEVEL_KIT_VERSION v0.2.19  
RUN mkdir -p /usr/src/ngx_devel_kit \  
&& curl -sL
https://github.com/simpl/ngx_devel_kit/archive/${DEVEL_KIT_VERSION}.tar.gz | \  
tar xz -C /usr/src/ngx_devel_kit \--strip-components=1  
# lua module  
ENV LUA_MOD_VERSION v0.9.16  
ENV luaBuildDeps "\  
liblua5.1-0-dev \  
"  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -q -y \--no-install-
recommends \  
$luaBuildDeps \  
lua5.1 \  
liblua5.1-0 \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/lua-nginx-module \  
&& ln -s /usr/lib/x86_64-linux-gnu/liblua5.1.so /usr/lib/liblua.so \  
&& curl -sL https://github.com/openresty/lua-nginx-
module/archive/${LUA_MOD_VERSION}.tar.gz | \  
tar xz -C /usr/src/lua-nginx-module \--strip-components=1  
# echo module  
ENV ECHO_VERSION v0.58  
RUN mkdir -p /usr/src/echo-nginx-module \  
&& curl -sL https://github.com/openresty/echo-nginx-
module/archive/${ECHO_VERSION}.tar.gz | \  
tar xz -C /usr/src/echo-nginx-module \--strip-components=1  
# header more module  
ENV HEADERS_MORE_VERSION v0.261  
RUN mkdir -p /usr/src/headers-more-nginx-module \  
&& curl -sL https://github.com/openresty/headers-more-nginx-
module/archive/${HEADERS_MORE_VERSION}.tar.gz | \  
tar xz -C /usr/src/headers-more-nginx-module \--strip-components=1  
# cache purge module  
ENV CACHE_PURGE_VERSION 2.3  
RUN mkdir -p /usr/src/ngx_cache_purge \  
&& curl -sL
https://github.com/FRiCKLE/ngx_cache_purge/archive/${CACHE_PURGE_VERSION}.tar.gz
| \  
tar xz -C /usr/src/ngx_cache_purge \--strip-components=1  
# fancy index module  
ENV FANCY_INDEX_VERSION v0.3.5  
RUN mkdir -p /usr/src/ngx-fancyindex \  
&& curl -sL https://github.com/aperezdc/ngx-
fancyindex/archive/${FANCY_INDEX_VERSION}.tar.gz | \  
tar xz -C /usr/src/ngx-fancyindex \--strip-components=1  
# auth pam module  
ENV AUTH_PAM_VERSION v1.4  
ENV authPamBuildDEps "libpam0g-dev"  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -q -y \--no-install-
recommends $authPamBuildDEps \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/ngx_http_auth_pam_module \  
&& curl -sL
https://github.com/stogh/ngx_http_auth_pam_module/archive/${AUTH_PAM_VERSION}.tar.gz
| \  
tar xz -C /usr/src/ngx_http_auth_pam_module \--strip-components=1  
# dav ext module  
ENV DAV_EXT_VERSION v0.0.3  
ENV davExtBuildDEps "libexpat-dev"  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -q -y \--no-install-
recommends $davExtBuildDEps \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/nginx-dav-ext-module \  
&& curl -sL https://github.com/arut/nginx-dav-ext-
module/archive/${DAV_EXT_VERSION}.tar.gz | \  
tar xz -C /usr/src/nginx-dav-ext-module \--strip-components=1  
# http push module  
ENV HTTP_PUSH_VERSION v0.73  
RUN mkdir -p /usr/src/nginx_http_push_module \  
&& curl -sL
https://github.com/slact/nginx_http_push_module/archive/${HTTP_PUSH_VERSION}.tar.gz
| \  
tar xz -C /usr/src/nginx_http_push_module \--strip-components=1  
# upload progress module  
ENV UPLOAD_PROGRESS_VERSION v0.9.1  
RUN mkdir -p /usr/src/nginx-upload-progress-module \  
&& curl -sL https://github.com/masterzen/nginx-upload-progress-
module/archive/${UPLOAD_PROGRESS_VERSION}.tar.gz | \  
tar xz -C /usr/src/nginx-upload-progress-module \--strip-components=1  
# upstream fair module  
ENV UPSTREAM_FAIR_VERSION master  
RUN mkdir -p /usr/src/nginx-upstream-fair \  
&& curl -sL https://github.com/gnosek/nginx-upstream-
fair/archive/${UPSTREAM_FAIR_VERSION}.tar.gz | \  
tar xz -C /usr/src/nginx-upstream-fair \--strip-components=1  
# substitutions filter module  
ENV SUBSTITUTIONS_FILTER_VERSION v0.6.4  
RUN mkdir -p /usr/src/ngx_http_substitutions_filter_module \  
&& curl -sL
https://github.com/yaoweibin/ngx_http_substitutions_filter_module/archive/${SUBSTITUTIONS_FILTER_VERSION}.tar.gz
| \  
tar xz -C /usr/src/ngx_http_substitutions_filter_module \--strip-components=1  
# set misc module  
ENV SET_MISC_VERSION v0.29  
RUN mkdir -p /usr/src/set-misc-nginx-module \  
&& curl -sL https://github.com/openresty/set-misc-nginx-
module/archive/${SET_MISC_VERSION}.tar.gz | \  
tar xz -C /usr/src/set-misc-nginx-module \--strip-components=1  
# naxsi module  
ENV NAXSI_VERSION 0.54rc3  
RUN mkdir -p /usr/src/naxsi \  
&& curl -sL https://github.com/nbs-
system/naxsi/archive/${NAXSI_VERSION}.tar.gz | \  
tar xz -C /usr/src/naxsi \--strip-components=1  
# drizzle module  
ENV DRIZZLE_VERSION v0.1.9  
ENV drizzleBuildDeps "python python2.7 intltool libprotobuf-dev protobuf-
compiler libgcrypt11-dev"  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -q -y \--no-install-
recommends $drizzleBuildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/drizzle \  
&& curl -sL http://openresty.org/download/drizzle7-2011.07.21.tar.gz | \  
tar xz -C /usr/src/drizzle \--strip-components=1 \  
&& cd /usr/src/drizzle \  
&& CFLAGS="$(dpkg-buildflags --get CFLAGS)" \  
CPPFLAGS="$(dpkg-buildflags --get CPPFLAGS)" \  
LDFLAGS="$(dpkg-buildflags --get LDFLAGS)" \  
./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--datadir=/usr/share \  
\--without-server \  
&& make libdrizzle-1.0 -j"$(nproc)" \  
&& make install-libdrizzle-1.0 \  
&& mkdir -p /usr/src/drizzle-nginx-module \  
&& curl -sL https://github.com/openresty/drizzle-nginx-
module/archive/${DRIZZLE_VERSION}.tar.gz | \  
tar xz -C /usr/src/drizzle-nginx-module \--strip-components=1  
# lua resty mysql module  
ENV LUA_RESTY_MYSQL_VERSION v0.15  
RUN mkdir -p /usr/src/lua-resty-mysql \  
&& curl -sL https://github.com/openresty/lua-resty-
mysql/archive/${LUA_RESTY_MYSQL_VERSION}.tar.gz | \  
tar xz -C /usr/src/lua-resty-mysql \--strip-components=1  
# array var module  
ENV ARRAY_VAR_VERSION v0.04  
RUN mkdir -p /usr/src/array-var-nginx-module \  
&& curl -sL https://github.com/openresty/array-var-nginx-
module/archive/${ARRAY_VAR_VERSION}.tar.gz | \  
tar xz -C /usr/src/array-var-nginx-module \--strip-components=1  
# auth request module  
RUN mkdir -p /usr/src/http_auth_request \  
&& curl -sL
http://mdounin.ru/hg/ngx_http_auth_request_module/archive/tip.tar.gz | \  
tar xz -C /usr/src/http_auth_request \--strip-components=1  
# coolkit module  
ENV COOLKIT_VERSION 0.2rc3  
RUN mkdir -p /usr/src/ngx_coolkit \  
&& curl -sL https://github.com/FRiCKLE/ngx_coolkit/archive/0.2rc3.tar.gz | \  
tar xz -C /usr/src/ngx_coolkit \--strip-components=1  
# encrypted session module  
ENV ENCRYPTED_SESSION_VERSION v0.04  
RUN mkdir -p /usr/src/encrypted-session-nginx-module \  
&& curl -sL https://github.com/openresty/encrypted-session-nginx-
module/archive/${ENCRYPTED_SESSION_VERSION}.tar.gz | \  
tar xz -C /usr/src/encrypted-session-nginx-module \--strip-components=1  
# form input module  
ENV FORM_INPUT_VERSION v0.11  
RUN mkdir -p /usr/src/form-input-nginx-module \  
&& curl -sL https://github.com/calio/form-input-nginx-
module/archive/${FORM_INPUT_VERSION}.tar.gz | \  
tar xz -C /usr/src/form-input-nginx-module \--strip-components=1  
# iconv module  
ENV ICONV_VERSION v0.11  
ENV LIBICONV_VERSION 1.13  
#ENV iconvBuildDeps libiconv  
RUN mkdir /usr/src/libiconv \  
&& curl -sL
http://ftp.gnu.org/pub/gnu/libiconv/libiconv-${LIBICONV_VERSION}.tar.gz | \  
tar xz -C /usr/src/libiconv \--strip-components=1 \  
&& cd /usr/src/libiconv \  
&& CFLAGS="$(dpkg-buildflags --get CFLAGS)" \  
CPPFLAGS="$(dpkg-buildflags --get CPPFLAGS)" \  
LDFLAGS="$(dpkg-buildflags --get LDFLAGS)" \  
./configure \  
\--prefix=/usr \  
&& make -j$(nproc)\  
&& make install \  
&& mkdir -p /usr/src/iconv-nginx-module \  
&& curl -sL https://github.com/calio/iconv-nginx-
module/archive/${ICONV_VERSION}.tar.gz | \  
tar xz -C /usr/src/iconv-nginx-module \--strip-components=1  
# memc module  
ENV MEMC_VERSION v0.16  
RUN mkdir /usr/src/memc-nginx-module \  
&& curl -sL https://github.com/openresty/memc-nginx-
module/archive/${MEMC_VERSION}.tar.gz | \  
tar xz -C /usr/src/memc-nginx-module \--strip-components=1  
# postgres module  
ENV POSTGRES_VERSION 1.0rc7  
ENV postgresBuildDeps "libpq-dev"  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -q -y \--no-install-
recommends $postgresBuildDeps libpq5 \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /usr/src/ngx_postgres \  
&& curl -sL
https://github.com/FRiCKLE/ngx_postgres/archive/${POSTGRES_VERSION}.tar.gz | \  
tar xz -C /usr/src/ngx_postgres \--strip-components=1  
# nginscript  
ENV nginscriptBuildDeps "mercurial mercurial-common"  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -q -y \--no-install-
recommends $nginscriptBuildDeps \  
&& cd /usr/src \  
&& hg clone http://hg.nginx.org/njs  
# build nginx  
# NOTE: passing option -j"$(nproc)" to make command sometimes cause some build
errors in openssl  
RUN cd /usr/src/nginx \  
&& ./configure \  
\--with-cc-opt="$(dpkg-buildflags --get CFLAGS) $(dpkg-buildflags --get
CPPFLAGS)" \  
\--with-ld-opt="$(dpkg-buildflags --get LDFLAGS)" \  
\--user=www-data \  
\--group=www-data \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--http-log-path=/proc/self/fd/1 \  
\--error-log-path=/proc/self/fd/2 \  
\--pid-path=/var/run/nginx/nginx.pid \  
\--lock-path=/var/run/nginx/nginx.lock \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
\--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
\--with-file-aio \  
\--with-google_perftools_module \  
\--with-http_addition_module \  
\--with-http_dav_module \  
\--with-http_degradation_module \  
\--with-http_flv_module \  
\--with-http_geoip_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_image_filter_module \  
\--with-http_mp4_module \  
\--with-http_perl_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_secure_link_module \  
\--with-http_v2_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_xslt_module \  
\--with-ipv6 \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-pcre-jit \  
\--with-openssl=/usr/src/openssl \  
\--with-openssl-opt="-Wa,--noexecstack no-idea no-mdc2 no-rc5 no-zlib enable-
tlsext no-ssl2 no-ssl3" \  
\--with-sha1=/usr/include/openssl \  
\--with-md5=/usr/include/openssl \  
\--add-module=/usr/src/ngx_devel_kit \  
\--add-module=/usr/src/array-var-nginx-module \  
\--add-module=/usr/src/drizzle-nginx-module \  
\--add-module=/usr/src/echo-nginx-module \  
\--add-module=/usr/src/encrypted-session-nginx-module \  
\--add-module=/usr/src/form-input-nginx-module \  
\--add-module=/usr/src/headers-more-nginx-module \  
\--add-module=/usr/src/http_auth_request \  
\--add-module=/usr/src/iconv-nginx-module \  
\--add-module=/usr/src/lua-nginx-module \  
\--add-module=/usr/src/memc-nginx-module \  
\--add-module=/usr/src/modsecurity/nginx/modsecurity \  
\--add-module=/usr/src/naxsi/naxsi_src \  
\--add-module=/usr/src/nginx-dav-ext-module \  
\--add-module=/usr/src/nginx-upload-progress-module \  
\--add-module=/usr/src/nginx-upstream-fair \  
\--add-module=/usr/src/ngx-fancyindex \  
\--add-module=/usr/src/ngx_cache_purge \  
\--add-module=/usr/src/ngx_coolkit \  
\--add-module=/usr/src/ngx_http_auth_pam_module \  
\--add-module=/usr/src/ngx_http_substitutions_filter_module \  
\--add-module=/usr/src/ngx_postgres \  
\--add-module=/usr/src/njs/nginx \  
\--add-module=/usr/src/pagespeed \  
\--add-module=/usr/src/set-misc-nginx-module \  
&& make \  
&& make install  
# --add-module=/usr/src/nginx_http_push_module \  
# install nginx files  
RUN mkdir -p /var/run/nginx \  
&& chown -R www-data:www-data /etc/nginx/html /var/run/nginx \  
&& mkdir -p /var/cache/nginx/client_temp \  
&& mkdir -p /var/cache/nginx/fastcgi_temp \  
&& mkdir -p /var/cache/nginx/pagespeed \  
&& mkdir -p /var/cache/nginx/proxy_temp \  
&& mkdir -p /var/cache/nginx/scgi_temp \  
&& mkdir -p /var/cache/nginx/uwsgi_temp \  
&& chown -R www-data:www-data /var/cache/nginx  
# install modsecurity files  
RUN /usr/bin/install -m 644 /usr/src/modsecurity/unicode.mapping
/etc/nginx/unicode.mapping \  
&& /usr/bin/install -m 644 /usr/src/modsecurity/modsecurity.conf-recommended
/etc/nginx/modsecurity.conf \  
&& /usr/bin/install -m 644 /usr/src/modsecurity/standalone/.libs/standalone.so
/usr/local/lib/standalone.so \  
&& /usr/bin/install -m 644
/usr/src/modsecurity/standalone/.libs/standalone.lai
/usr/local/lib/standalone.lai \  
&& /usr/bin/install -m 644 /usr/src/modsecurity/standalone/.libs/standalone.a
/usr/local/lib/standalone.a \  
&& /usr/bin/install -m 755 /usr/src/modsecurity/tools/rules-updater.pl
/usr/sbin/rules-updater.pl  
# clean  
RUN DEBIAN_FRONTEND=noninteractive apt-get purge -q -y \--auto-remove \  
$buildDeps \  
$authPamBuildDEps \  
$davExtBuildDEps \  
$drizzleBuildDeps \  
$luaBuildDeps \  
$modsecurityBuildDeps \  
$nginxBuildDeps \  
$pagespeedBuildDeps \  
$postgresBuildDeps \  
$nginscriptBuildDeps \  
&& rm -rf /usr/src/nginx \  
&& rm -rf /usr/src/array-var-nginx-module \  
&& rm -rf /usr/src/drizzle \  
&& rm -rf /usr/src/drizzle-nginx-module \  
&& rm -rf /usr/src/echo-nginx-module \  
&& rm -rf /usr/src/encrypted-session-nginx-module \  
&& rm -rf /usr/src/form-input-nginx-module \  
&& rm -rf /usr/src/headers-more-nginx-module \  
&& rm -rf /usr/src/http_auth_request \  
&& rm -rf /usr/src/iconv-nginx-module \  
&& rm -rf /usr/src/lua-nginx-module \  
&& rm -rf /usr/src/memc-nginx-module \  
&& rm -rf /usr/src/modpagespeed \  
&& rm -rf /usr/src/modsecurity \  
&& rm -rf /usr/src/naxsi \  
&& rm -rf /usr/src/nginx-dav-ext-module \  
&& rm -rf /usr/src/nginx-upload-progress-module \  
&& rm -rf /usr/src/nginx-upstream-fair \  
&& rm -rf /usr/src/nginx_http_push_module \  
&& rm -rf /usr/src/ngx-fancyindex \  
&& rm -rf /usr/src/ngx_cache_purge \  
&& rm -rf /usr/src/ngx_coolkit \  
&& rm -rf /usr/src/ngx_devel_kit \  
&& rm -rf /usr/src/ngx_http_auth_pam_module \  
&& rm -rf /usr/src/ngx_http_substitutions_filter_module \  
&& rm -rf /usr/src/njs \  
&& rm -rf /usr/src/openssl \  
&& rm -rf /usr/src/pagespeed \  
&& rm -rf /usr/src/set-misc-nginx-module  
  
WORKDIR /etc/nginx/html  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  
  
# USER www-data  

