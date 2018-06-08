# Dockerfile - alpine  
# https://github.com/openresty/docker-openresty  
  
  
FROM domecloud/alpine  
  
MAINTAINER Chanchai Junlouchai <neverlock@gmail.com>  
  
# Docker Build Arguments  
ARG RESTY_VERSION="1.11.2.3"  
ARG RESTY_OPENSSL_VERSION="1.0.2k"  
ARG RESTY_PCRE_VERSION="8.39"  
ARG RESTY_J="1"  
ARG RESTY_WAF_VERSION="0.11"  
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
\--with-luajit \  
\--with-pcre-jit \  
\--with-sha1-asm \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-threads \  
"  
  
# These are not intended to be user-specified  
ARG _RESTY_CONFIG_DEPS="--with-openssl=/tmp/openssl-${RESTY_OPENSSL_VERSION}
--with-pcre=/tmp/pcre-${RESTY_PCRE_VERSION}"  
  
ENV LUAJIT_VERSION=2.1  
ENV LUAROCKS_SRC_SHA1=5f1e1658ef8c7c9710fbc751cad79eb69ae2a891 \  
LUAROCKS_VERSION=2.4.0 \  
LUA_SUFFIX=jit-2.1.0-beta2 \  
OPENRESTY_PREFIX=/usr/local/openresty  
  
  
# 1) Install apk dependencies  
# 2) Download and untar OpenSSL, PCRE, and OpenResty  
# 3) Build OpenResty  
# 4) Cleanup  
  
RUN \  
apk add --no-cache --virtual .build-deps \  
build-base \  
curl \  
gd-dev \  
geoip-dev \  
libxslt-dev \  
linux-headers \  
make \  
perl-dev \  
readline-dev \  
zlib-dev \  
&& apk add --no-cache \  
gd \  
geoip \  
libgcc \  
libxslt \  
zlib \  
git \  
libstdc++ \  
python \  
lua5.1-dev \  
pcre-dev \  
&& cd /tmp \  
&& curl -fSL
https://www.openssl.org/source/openssl-${RESTY_OPENSSL_VERSION}.tar.gz -o
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& tar xzf openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& curl -kfSL
https://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${RESTY_PCRE_VERSION}.tar.gz
-o pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& tar xzf pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& curl -fSL https://openresty.org/download/openresty-${RESTY_VERSION}.tar.gz
-o openresty-${RESTY_VERSION}.tar.gz \  
&& tar xzf openresty-${RESTY_VERSION}.tar.gz \  
&& cd /tmp/openresty-${RESTY_VERSION} \  
&& ./configure -j${RESTY_J} ${_RESTY_CONFIG_DEPS} ${RESTY_CONFIG_OPTIONS} \  
&& make -j${RESTY_J} \  
&& make -j${RESTY_J} install \  
#&& cd /opt/lixen \  
#&& ln -sf /opt/lixen/ /usr/local/openresty \  
##&& ln -sf /usr/bin/luarocks-5.1 /usr/bin/luarocks \  
#&& export PATH=$PATH:/opt/lixen/luajit/bin/:/opt/lixen/bin/ \  
##&& export
PATH=$PATH:/usr/local/openresty/luajit/bin/:/usr/local/openresty/bin/ \  
##&& luarocks-5.1 install lua-resty-waf \  
##&& cp -rf /usr/local/openresty/site/lualib/* /usr/local/openresty/lualib/ \  
##&& rm -rf /usr/local/openresty/site/lualib/ \  
#&& cp -rf /opt/lixen/site/lualib/* /opt/lixen/lualib/ \  
#&& rm -rf /opt/lixen/site/lualib/ \  
&& ln -sf $OPENRESTY_PREFIX/luajit/bin/luajit-*
$OPENRESTY_PREFIX/luajit/bin/lua \  
&& ln -sf $OPENRESTY_PREFIX/luajit/bin/luajit-* /usr/local/bin/lua \  
&& curl -sSL
http://keplerproject.github.io/luarocks/releases/luarocks-${LUAROCKS_VERSION}.tar.gz
-o /tmp/luarocks.tar.gz \  
&& cd /tmp \  
#&& echo "${LUAROCKS_SRC_SHA1} *luarocks.tar.gz" | sha1sum -c - \  
&& tar -xzf luarocks.tar.gz \  
&& cd luarocks-* \  
&& ./configure \  
\--prefix=${OPENRESTY_PREFIX}/luajit \  
\--lua-suffix=${LUA_SUFFIX} \  
\--with-lua=${OPENRESTY_PREFIX}/luajit \  
\--with-lua-lib=${OPENRESTY_PREFIX}/luajit/lib \  
\--with-lua-
include=${OPENRESTY_PREFIX}/luajit/include/luajit-${LUAJIT_VERSION} \  
&& make build \  
&& make install \  
&& make bootstrap \  
&& cd /tmp \  
&& rm -rf /tmp/luarocks-* \  
&& rm -rf ~/.cache/luarocks \  
&& ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luarocks /usr/local/bin/luarocks \  
###  
&& export
PATH=$PATH:/usr/local/openresty/luajit/bin/:/usr/local/openresty/bin/ \  
&& luarocks install lua-resty-waf \  
&& cp -rf /usr/local/openresty/site/lualib/* /usr/local/openresty/lualib/ \  
&& rm -rf /usr/local/openresty/site/lualib/ \  
###  
&& cd /tmp \  
&& rm -rf \  
luarocks.tar.gz \  
openssl-${RESTY_OPENSSL_VERSION} \  
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
openresty-${RESTY_VERSION}.tar.gz openresty-${RESTY_VERSION} \  
pcre-${RESTY_PCRE_VERSION}.tar.gz pcre-${RESTY_PCRE_VERSION} \  
&& apk del .build-deps \  
&& ln -sf /dev/stdout /usr/local/openresty/nginx/logs/access.log \  
&& ln -sf /dev/stderr /usr/local/openresty/nginx/logs/error.log  
  
COPY conf/ /usr/local/openresty/nginx/conf/  
COPY start.sh /  
COPY .bashrc /root/  
RUN chmod +x /start.sh  
ENV TERM screen-256color  
ENV SHELL=/bin/bash  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/openresty/nginx/sbin  
  
ENTRYPOINT ["/start.sh"]  

