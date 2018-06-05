FROM debian:stretch-slim  
  
MAINTAINER Semen Angarsky <seofack@gmail.com>  
  
ENV NGINX_VERSION 1.12.2  
ENV NPS_VERSION 1.13.35.2-stable  
  
# https://docs.docker.com/compose/compose-file/#variable-substitution  
# "Other extended shell-style features, such as ${VARIABLE/foo/bar}, are not
supported."  
# That's why we define the PSOL release manually.  
ENV PSOL_RELEASE "1.13.35.2-"  
  
RUN apt-get update \  
&& apt-get install -y wget build-essential zlib1g-dev libpcre3 libpcre3-dev
unzip uuid-dev libssl-dev  
  
RUN cd "/tmp" \  
# Installs PageSpeed module  
# https://www.modpagespeed.com/doc/build_ngx_pagespeed_from_source  
  
&& wget -qO- https://github.com/apache/incubator-pagespeed-
ngx/archive/v${NPS_VERSION}.tar.gz | tar -zx \  
&& NPS_DIR=$(find . -name "*pagespeed-ngx-${NPS_VERSION}" -type d) \  
&& cd "$NPS_DIR" \  
&& PSOL_URL=https://dl.google.com/dl/page-speed/psol/${PSOL_RELEASE}.tar.gz \  
&& [ -e scripts/format_binary_url.sh ] &&
PSOL_URL=$(scripts/format_binary_url.sh PSOL_BINARY_URL) \  
&& wget ${PSOL_URL} \  
&& tar -xzvf $(basename ${PSOL_URL}) \  
  
# Installs NGINX  
# The NGINX config is taken from the official docker image by an execution of
the command "nginx -V"  
&& cd "/tmp" \  
&& wget -qO- http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar -zx
\  
&& cd "/tmp/nginx-${NGINX_VERSION}" \  
# The config is taken from the official "nginx" dockerhub image by the command
execution "nginx -V".  
&& ./configure \  
--prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--modules-path=/usr/lib/nginx/modules \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--http-client-body-temp-path=/var/cache/nginx/client_temp \  
--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
--user=nginx \  
--group=nginx \  
--with-compat \  
--with-file-aio \  
--with-threads \  
--with-http_addition_module \  
--with-http_auth_request_module \  
--with-http_dav_module \  
--with-http_flv_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_mp4_module \  
--with-http_random_index_module \  
--with-http_realip_module \  
--with-http_secure_link_module \  
--with-http_slice_module \  
--with-http_ssl_module \  
--with-http_stub_status_module \  
--with-http_sub_module \  
--with-http_v2_module \  
--with-mail \  
--with-mail_ssl_module \  
--with-stream \  
--with-stream_realip_module \  
--with-stream_ssl_module \  
--with-stream_ssl_preread_module \  
--with-cc-opt='-g -O2 -fdebug-prefix-
map=/data/builder/debuild/nginx-1.12.2/debian/debuild-base/nginx-1.12.2=.
-specs=/usr/share/dpkg/no-pie-compile.specs -fstack-protector-strong -Wformat
-Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fPIC' \  
--with-ld-opt='-specs=/usr/share/dpkg/no-pie-link.specs -Wl,-z,relro
-Wl,-z,now -Wl,--as-needed -pie' \  
--add-module=/tmp/$NPS_DIR \  
&& make install  
  
RUN mkdir -p
/var/cache/nginx/{client_temp,fastcgi_temp,proxy_temp,uwsgi_temp,scgi_temp}  
  
# Cleans up installation files  
RUN cd && \  
rm -rf /tmp/*  
  
# Adds a basic configuration  
COPY config/nginx.conf /etc/nginx/  
COPY config/pagespeed.conf /etc/nginx/  
  
WORKDIR /var/www  
  
CMD ["nginx", "-g", "daemon off;"]  

