FROM nginx:latest  
# Add configuration files  
RUN mkdir -p /etc/nginx/common  
COPY conf/nginx/common/expirecache.conf /etc/nginx/common/expirecache.conf  
COPY conf/nginx/common/pagespeed.conf /etc/nginx/common/pagespeed.conf  
# Install google pagespeed  
  
RUN apt-get update -y && apt-get -y install build-essential zlib1g-dev
libpcre3 libpcre3-dev unzip libssl-dev  
  
  
# Install google pagespeed  
ENV NPS_VERSION 1.12.34.3-stable  
ENV NGINX_VERSION 1.13.5  
  
RUN apt-get install -y wget && apt-get install -y vim && cd &&\  
wget https://github.com/pagespeed/ngx_pagespeed/archive/v${NPS_VERSION}.zip
&&\  
unzip v${NPS_VERSION}.zip &&\  
cd ngx_pagespeed-${NPS_VERSION}/ &&\  
psol_url=https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz &&\  
[ -e scripts/format_binary_url.sh ] && psol_url=$(scripts/format_binary_url.sh
PSOL_BINARY_URL) &&\  
wget ${psol_url} &&\  
tar -xzvf $(basename ${psol_url})  
  
RUN cd \  
&& wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \  
&& tar -xvzf nginx-${NGINX_VERSION}.tar.gz \  
&& cd nginx-${NGINX_VERSION}/ \  
&& ./configure \--add-module=$HOME/ngx_pagespeed-${NPS_VERSION}
\--prefix=/etc/nginx \--sbin-path=/usr/sbin/nginx \--modules-
path=/usr/lib/nginx/modules \--conf-path=/etc/nginx/nginx.conf \--error-log-
path=/var/log/nginx/error.log \--http-log-path=/var/log/nginx/access.log
\--pid-path=/var/run/nginx.pid \--lock-path=/var/run/nginx.lock \--http-
client-body-temp-path=/var/cache/nginx/client_temp \--http-proxy-temp-
path=/var/cache/nginx/proxy_temp \--http-fastcgi-temp-
path=/var/cache/nginx/fastcgi_temp \--http-uwsgi-temp-
path=/var/cache/nginx/uwsgi_temp \--http-scgi-temp-
path=/var/cache/nginx/scgi_temp \--user=nginx \--group=nginx \--with-compat
\--with-file-aio \--with-threads \--with-http_addition_module \--with-
http_auth_request_module \--with-http_dav_module \--with-http_flv_module
\--with-http_gunzip_module \--with-http_gzip_static_module \--with-
http_mp4_module \--with-http_random_index_module \--with-http_realip_module
\--with-http_secure_link_module \--with-http_slice_module \--with-
http_ssl_module \--with-http_stub_status_module \--with-http_sub_module
\--with-http_v2_module \--with-mail \--with-mail_ssl_module \--with-stream
\--with-stream_realip_module \--with-stream_ssl_module \--with-
stream_ssl_preread_module \--with-cc-opt='-g -O2 -fdebug-prefix-
map=/data/builder/debuild/nginx-1.13.5/debian/debuild-base/nginx-1.13.5=.
-specs=/usr/share/dpkg/no-pie-compile.specs -fstack-protector-strong -Wformat
-Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fPIC' \--with-ld-
opt='-specs=/usr/share/dpkg/no-pie-link.specs -Wl,-z,relro -Wl,-z,now
-Wl,\--as-needed -pie' \  
&& make \  
&& make install  
  
WORKDIR /app  

