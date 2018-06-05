FROM absalomedia/mini  
MAINTAINER Lawrence Meckan <media@absalom.biz>  
  
# Set correct environment variables.  
ENV DOCKER_NAME rev_nginx_sass_speed  
  
# https://github.com/pagespeed/ngx_pagespeed/releases  
ENV PAGESPEED_VERSION 1.12.34.2  
# http://nginx.org/en/download.html  
ENV NGINX_VERSION 1.12.0  
# https://www.openssl.org/source  
ENV OPENSSL_VERSION 1.1.0e  
  
# Enable ssh access  
RUN rm -f /etc/service/sshd/down  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
### ...put your own build instructions here... ###  
EXPOSE 80 443  
# RUN apt-get update  
# RUN DEBIAN_FRONTEND=noninteractive sudo apt-get upgrade -y  
RUN useradd -r -s /usr/sbin/nologin nginx && mkdir -p /var/log/nginx
/var/cache/nginx  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
RUN apt-get -y --no-install-recommends install wget build-essential zlib1g-dev
libpcre3-dev libxslt1-dev libxml2-dev libgd2-xpm-dev libgeoip-dev libgoogle-
perftools-dev libperl-dev  
RUN echo "Downloading ngx_pagespeed v${PAGESPEED_VERSION} ..." && wget -qO -
https://github.com/pagespeed/ngx_pagespeed/archive/v${PAGESPEED_VERSION}-beta.tar.gz
| tar zxf - -C /tmp  
RUN echo "Downloading pagespeed psol v${PAGESPEED_VERSION} ..." && wget -qO -
https://dl.google.com/dl/page-speed/psol/${PAGESPEED_VERSION}-x64.tar.gz | tar
xzf - -C /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta  
RUN echo "Downloading SASS architecture ..." && cd /tmp && git clone
https://github.com/absalomedia/sass-nginx-module.git && cd sass-nginx-module
&& git submodule init && git submodule update && cd lib/libsass && make shared
&& cd lib && ls -asl && cp libsass.so /usr/lib/libsass.so  
RUN echo "Set up Libsass shared lib" && cd /usr/lib && ls -asl  
RUN echo "Downloading Nginx v${NGINX_VERSION} ..." && wget -qO -
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar zxf - -C /tmp  
RUN echo "Downloading Openssl v${OPENSSL_VERSION} ..." && wget -qO -
https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz | tar xzf -
-C /tmp  
RUN cd /tmp/nginx-${NGINX_VERSION} && ./configure \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
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
\--without-http_autoindex_module \  
\--without-http_ssi_module \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-file-aio \  
\--with-http_v2_module \  
\--with-http_slice_module \  
\--with-cc-opt='-g -O2 -fstack-protector --param=ssp-buffer-size=4
-I/tmp/sass-nginx-module/lib/libsass/include -Wformat -Werror=format-security
-Wp,-D_FORTIFY_SOURCE=2' \  
\--with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-L/tmp/sass-nginx-
module/lib/libsass/lib,-z,relro -Wl,--as-needed' \  
\--with-ipv6 \  
\--with-pcre-jit \  
\--with-openssl=/tmp/openssl-${OPENSSL_VERSION} \  
\--add-module=/tmp/sass-nginx-module \  
\--add-module=/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta && make && make
install  
RUN rm -Rf /var/lib/apt/lists/* /var/tmp/* && \  
apt-get purge -yqq wget build-essential && \  
apt-get autoremove -yqq && \  
apt-get clean  
  
# for mount tmpfs volumes  
VOLUME ["/var/cache/nginx"]  
VOLUME ["/var/cache/pagespeed"]  
  
# for mount configs  
VOLUME ["/etc/nginx/sites-enabled"]  
  
ENV DEFAULT_APP_USER nginx  
ENV DEFAULT_APP_GROUP nginx  
ENV DEFAULT_APP_UID 1000  
ENV DEFAULT_APP_GID 1000  
ENV DEFAULT_UPLOAD_MAX_SIZE 30M  
ENV DEFAULT_NGINX_MAX_WORKER_PROCESSES 8  
ENV DEFAULT_CHOWN_APP_DIR true  
  
ENV SSL_ENABLED true  
  
COPY . /app  
  
RUN chmod 750 /app/bin/*.sh  
  
RUN /app/bin/init_nginx.sh  
  
CMD ["/sbin/my_init"]  
  

