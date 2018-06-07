FROM alpine:latest  
  
MAINTAINER Dome C. <dome@tel.co.th>  
  
# Docker Build Arguments  
ARG RESTY_VERSION="1.11.2.5"  
ARG RESTY_LUAROCKS_VERSION="2.3.0"  
ARG RESTY_OPENSSL_VERSION="1.0.2k"  
ARG RESTY_PCRE_VERSION="8.40"  
ARG RESTY_J="1"  
ARG RESTY_CONFIG_OPTIONS="\  
\--with-file-aio \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_geoip_module=dynamic \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_image_filter_module=dynamic \  
\--with-http_mp4_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-http_xslt_module=dynamic \  
\--with-ipv6 \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-md5-asm \  
\--with-pcre-jit \  
\--with-sha1-asm \  
\--with-stream \  
\--with-stream_ssl_module \  
\--add-module=/tmp/nginx_upstream_check_module \  
\--with-threads \  
"  
ARG RESTY_CONFIG_OPTIONS_MORE=""  
# These are not intended to be user-specified  
ARG _RESTY_CONFIG_DEPS="--with-openssl=/tmp/openssl-${RESTY_OPENSSL_VERSION}
--with-pcre=/tmp/pcre-${RESTY_PCRE_VERSION}"  
# 1) Install apk dependencies  
# 2) Download and untar OpenSSL, PCRE, and OpenResty  
# 3) Build OpenResty  
# 4) Cleanup  
RUN apk add --no-cache --virtual .build-deps \  
curl \  
gd-dev \  
geoip-dev \  
libxslt-dev \  
perl-dev \  
readline-dev \  
zlib-dev \  
&& apk add --no-cache \  
build-base \  
curl \  
gd \  
geoip \  
libgcc \  
libxslt \  
linux-headers \  
make \  
perl \  
unzip \  
zlib patch\  
&& cd /tmp \  
&& curl -fSL
https://www.openssl.org/source/openssl-${RESTY_OPENSSL_VERSION}.tar.gz -o
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& tar xzf openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& curl -fSL https://ftp.pcre.org/pub/pcre/pcre-${RESTY_PCRE_VERSION}.tar.gz
-o pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& tar xzf pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& curl -fSL https://openresty.org/download/openresty-${RESTY_VERSION}.tar.gz
-o openresty-${RESTY_VERSION}.tar.gz \  
&& tar xzf openresty-${RESTY_VERSION}.tar.gz \  
&& curl --retry 5 --max-time 120 --connect-timeout 5 -o
/tmp/nginx_upstream_check_module.zip -SL
https://github.com/yaoweibin/nginx_upstream_check_module/archive/master.zip \  
&& cd /tmp && unzip nginx_upstream_check_module.zip && mv
/tmp/nginx_upstream_check_module-master /tmp/nginx_upstream_check_module  
RUN true \  
&& cd /tmp/openresty-${RESTY_VERSION}/bundle/nginx-1.11.2 \  
&& pwd \  
&& patch -p0 < /tmp/nginx_upstream_check_module/check_1.11.1+.patch \  
&& cd /tmp/openresty-${RESTY_VERSION} \  
&& ./configure -j${RESTY_J} ${_RESTY_CONFIG_DEPS} ${RESTY_CONFIG_OPTIONS}
${RESTY_CONFIG_OPTIONS_MORE} \  
&& make -j${RESTY_J} \  
&& make -j${RESTY_J} install \  
&& cd /tmp \  
&& rm -rf \  
openssl-${RESTY_OPENSSL_VERSION} \  
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
openresty-${RESTY_VERSION}.tar.gz openresty-${RESTY_VERSION} \  
pcre-${RESTY_PCRE_VERSION}.tar.gz pcre-${RESTY_PCRE_VERSION} \  
&& curl -fSL
http://luarocks.org/releases/luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz -o
luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& tar xzf luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& cd luarocks-${RESTY_LUAROCKS_VERSION} \  
&& ./configure \  
\--prefix=/usr/local/openresty/luajit \  
\--with-lua=/usr/local/openresty/luajit \  
\--lua-suffix=jit-2.1.0-beta3 \  
\--with-lua-include=/usr/local/openresty/luajit/include/luajit-2.1 \  
&& make build \  
&& make install \  
&& cd /tmp \  
&& rm -rf luarocks-${RESTY_LUAROCKS_VERSION}
luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& apk add --no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
&& runDeps="$( \  
scanelf --needed --nobanner /tmp/envsubst \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual $runDeps \  
&& apk del .build-deps .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
&& ln -sf /dev/stdout /usr/local/openresty/nginx/logs/access.log \  
&& ln -sf /dev/stderr /usr/local/openresty/nginx/logs/error.log  
  
# Add additional binaries into PATH for convenience  
ENV
PATH=/usr/local/openresty/luajit/bin:/usr/local/openresty/nginx/sbin:/usr/local/openresty/bin:$PATH  
  
RUN \  
# Add gettext for envsubst  
apk add \--no-cache gettext &&\  
# Keep configuration files in /etc/nginx  
ln -sf /usr/local/openresty/nginx/conf /etc/nginx &&\  
# Install lua-resty-auto-ssl  
# See: https://github.com/GUI/lua-resty-auto-ssl  
apk add \--no-cache curl bash openssl bash curl grep sed &&\  
luarocks install lua-resty-auto-ssl &&\  
mkdir /etc/resty-auto-ssl &&\  
chown nobody /etc/resty-auto-ssl  
  
# Add proxy config  
COPY init.sh /init.sh  
COPY *.conf /etc/nginx/  
COPY default /etc/nginx/site/  
COPY index.html /opt/domecloud/html/  
  
# Add Let's Encrypt root certificate for OCSP stapling  
COPY isrgrootx1.pem /etc/ssl/isrgrootx1.pem  
COPY comodo.pem /etc/ssl/  
  
EXPOSE 80  
EXPOSE 443  
HEALTHCHECK \--interval=2m --timeout=3s \  
CMD curl -k -f http://127.0.0.1/ || exit 1  
COPY .bashrc /root/  
COPY shells /etc  
ENV TERM screen-256color  
ENV SHELL=/bin/bash  
  
ENTRYPOINT ["/init.sh"]  

