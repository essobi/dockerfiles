FROM alpine:3.7  
MAINTAINER Soma Szélpál <szelpalsoma@gmail.com>  
  
ENV OPENRESTY_VERSION 1.13.6.1  
ENV NGINX_RTMP_MODULE_VERSION 1.2.1  
ENV NGINX_OPENTRACING_MODULE_VERSION 0.2.1  
ENV OPENTRACING_VERSION 1.2.0  
ENV JAEGER_VERSION 0.2.0  
ENV FFMPEG_VERSION 3.4.2  
  
ENV OPENRESTY openresty-${OPENRESTY_VERSION}  
ENV NGINX_RTMP_MODULE nginx-rtmp-module-${NGINX_RTMP_MODULE_VERSION}  
ENV NGINX_OPENTRACING_MODULE nginx-
opentracing-${NGINX_OPENTRACING_MODULE_VERSION}  
ENV OPENTRACING opentracing-cpp-${OPENTRACING_VERSION}  
ENV JAEGER cpp-client-${JAEGER_VERSION}  
  
# Common build tools  
ENV BUILD_DEPS_OPENRESTY="unzip gcc binutils-libs binutils build-base libgcc
make pkgconf pkgconfig openssl openssl-dev ca-certificates pcre nasm yasm
yasm-dev coreutils musl-dev libc-dev pcre-dev zlib-dev cmake perl-dev"  
  
# FFMPEG dependencies  
ENV BUILD_DEPS_FFMPEG "unzip gcc binutils-libs binutils build-base libgcc make
pkgconf pkgconfig pcre nasm yasm yasm-dev coreutils musl-dev libc-dev pcre-dev
zlib-dev cmake gnutls-dev libogg-dev libvpx-dev libvorbis-dev freetype-dev
libass-dev libwebp-dev rtmpdump-dev libtheora-dev lame-dev xvidcore-dev
imlib2-dev x264-dev bzip2-dev perl-dev sdl2-dev libxfixes-dev libva-dev alsa-
lib-dev v4l-utils-dev opus-dev x265-dev"  
  
ADD *.patch /tmp  
  
# Installing nginx  
RUN set -x \  
&& apk update && apk add --no-cache --virtual .build-dependencies-openresty
${BUILD_DEPS_OPENRESTY} \  
&& cd /tmp \  
########################################  
# Build Opentracing cpp lib.  
########################################  
&& wget https://github.com/opentracing/opentracing-
cpp/archive/v${OPENTRACING_VERSION}.tar.gz -O ${OPENTRACING}.tar.gz \  
&& tar zxf ${OPENTRACING}.tar.gz \  
&& cd ${OPENTRACING} \  
&& mkdir .build && cd .build \  
&& cmake -DCMAKE_BUILD_TYPE=Release \  
-DBUILD_TESTING=OFF .. \  
&& make && make install \  
########################################  
# Build Jaeger cpp lib  
########################################  
&& cd /tmp \  
&& wget https://github.com/jaegertracing/cpp-
client/archive/v${JAEGER_VERSION}.tar.gz -O ${JAEGER}.tar.gz \  
&& tar zxf ${JAEGER}.tar.gz \  
&& cd ${JAEGER} \  
&& mkdir .build && cd .build \  
&& cmake -DCMAKE_BUILD_TYPE=Release \  
-DBUILD_TESTING=OFF \  
-DJAEGERTRACING_WITH_YAML_CPP=OFF .. \  
&& make && make install \  
&& export HUNTER_INSTALL_DIR=$(cat _3rdParty/Hunter/install-root-dir) \  
########################################  
# Get nginx-rtmp.  
########################################  
&& cd /tmp \  
&& wget https://github.com/arut/nginx-rtmp-
module/archive/v${NGINX_RTMP_MODULE_VERSION}.tar.gz -O
${NGINX_RTMP_MODULE}.tar.gz \  
&& tar zxf ${NGINX_RTMP_MODULE}.tar.gz \  
&& cd nginx-rtmp-module-${NGINX_RTMP_MODULE_VERSION} \  
&& patch -p1 < /tmp/rtmp-exec-stdin-1.2.1.patch \  
########################################  
# Get nginx-opentracing.  
########################################  
&& cd /tmp \  
&& wget https://github.com/opentracing-contrib/nginx-
opentracing/archive/v${NGINX_OPENTRACING_MODULE_VERSION}.tar.gz -O
${NGINX_OPENTRACING_MODULE}.tar.gz \  
&& tar zxf ${NGINX_OPENTRACING_MODULE}.tar.gz \  
########################################  
# Install openresty, it contains nginx  
# and lua, all of the nginx configure  
# options are usable.  
########################################  
&& addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& cd /tmp \  
&& wget http://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz -O
${OPENRESTY}.tar.gz \  
&& tar zxf ${OPENRESTY}.tar.gz \  
&& cd ${OPENRESTY} \  
&& ./configure \  
\--add-dynamic-module=/tmp/${NGINX_OPENTRACING_MODULE}/opentracing \  
\--add-dynamic-module=/tmp/${NGINX_OPENTRACING_MODULE}/jaeger \  
\--add-module=/tmp/${NGINX_RTMP_MODULE} \  
\--with-http_auth_request_module \  
\--with-cc-opt="-I$HUNTER_INSTALL_DIR/include" \  
\--with-ld-opt="-L$HUNTER_INSTALL_DIR/lib" \  
\--without-http_echo_module \  
\--without-http_xss_module \  
\--without-http_coolkit_module \  
\--without-http_set_misc_module \  
\--without-http_form_input_module \  
\--without-http_encrypted_session_module \  
\--without-http_srcache_module \  
\--without-http_lua_upstream_module \  
\--without-http_headers_more_module \  
\--without-http_array_var_module \  
\--without-http_memc_module \  
\--without-http_redis2_module \  
\--without-http_redis_module \  
\--without-http_rds_json_module \  
\--without-http_rds_csv_module \  
\--without-stream_lua_module \  
\--without-http_ssl_module \  
\--without-lua_cjson \  
\--without-lua_redis_parser \  
\--without-lua_rds_parser \  
\--without-lua_resty_dns \  
\--without-lua_resty_memcached \  
\--without-lua_resty_redis \  
\--without-lua_resty_mysql \  
\--without-lua_resty_upload \  
\--without-lua_resty_upstream_healthcheck \  
\--without-lua_resty_string \  
\--without-lua_resty_websocket \  
\--without-lua_resty_limit_traffic \  
\--without-lua_resty_lock \  
\--without-lua_resty_lrucache \  
\--without-mail_pop3_module \  
\--without-mail_imap_module \  
\--without-mail_smtp_module \  
\--with-pcre \  
\--with-debug \  
\--with-compat \  
\--with-luajit \  
\--user=nginx \  
\--group=nginx \  
&& make && make install \  
########################################  
# Cleanup.  
########################################  
&& apk del .build-dependencies-openresty \  
&& rm -rf /var/cache/* /tmp/* $HOME/.hunter \  
# Need to recreate the apk cache folder or apk will die  
&& mkdir -p /var/cache/apk  
  
# Installing ffmpeg  
RUN set -x \  
########################################  
# Install ffmpeg dependencies  
########################################  
&& apk add --no-cache --virtual .build-dependencies-ffmpeg
${BUILD_DEPS_FFMPEG} \  
&& echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& apk add --no-cache --update fdk-aac-dev \  
########################################  
# Download ffmpeg  
########################################  
&& cd /tmp/ \  
&& wget http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.gz \  
&& tar zxf ffmpeg-${FFMPEG_VERSION}.tar.gz \  
&& cd /tmp/ffmpeg-${FFMPEG_VERSION} \  
&& ./configure \  
\--enable-version3 \  
\--enable-gpl \  
\--enable-nonfree \  
\--enable-small \  
\--enable-libmp3lame \  
\--enable-libx264 \  
\--enable-libx265 \  
\--enable-libvpx \  
\--enable-libtheora \  
\--enable-libvorbis \  
\--enable-libopus \  
\--enable-libfdk-aac \  
\--enable-libass \  
\--enable-libwebp \  
\--enable-librtmp \  
\--enable-postproc \  
\--enable-avresample \  
\--enable-libfreetype \  
\--enable-gnutls \  
\--enable-avfilter \  
\--enable-libxvid \  
\--enable-libv4l2 \  
\--enable-pic \  
\--enable-shared \  
\--enable-vaapi \  
\--enable-pthreads \  
\--enable-shared \  
\--disable-stripping \  
\--disable-static \  
\--disable-debug \  
&& make && make install && make distclean \  
&& apk del .build-dependencies-ffmpeg \  
&& rm -rf /var/cache/* /tmp/* \  
# Need to recreate the apk cache folder or apk will die  
&& mkdir -p /var/cache/apk  
  
# Updating certificates  
RUN apk update \  
&& apk add --no-cache openssl ca-certificates \  
&& update-ca-certificates  
  
# Installing runtime dependencies and helpers  
RUN apk add --update --no-cache curl libstdc++ pcre libgcc libxcb libvorbis
libass alsa-lib sdl2 v4l-utils-libs freetype librtmp gnutls libbz2 xvidcore
x265 x264-libs libwebp libvpx libtheora opus lame libva libx11 perl  
  
# Add openresty bins to PATH  
ENV
PATH=$PATH:/usr/local/openresty/luajit/bin:/usr/local/openresty/nginx/sbin:/usr/local/openresty/bin  
  
# Adding nginx configuration file  
ADD nginx.conf /usr/local/openresty/nginx/conf/nginx.conf  
  
# Prepare data directory  
RUN mkdir -p /data  
RUN mkdir -p /data/hls  
RUN mkdir -p /data/dash  
  
# Prepare www directory  
RUN mkdir -p /www  
  
# Add static files  
ADD static /www/static  
  
# Expose RTMP port  
EXPOSE 1935  
  
# Expose HTTP port  
EXPOSE 80  
  
# Start NGINX  
CMD ["/usr/local/openresty/nginx/sbin/nginx"]  

