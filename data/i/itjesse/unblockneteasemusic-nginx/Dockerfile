FROM unocha/alpine-base-s6:3.4  
  
MAINTAINER Jesse Zhu <jesse@itjesse.cn>  
  
ENV NGINX_VERSION nginx-1.10.1  
  
RUN build_pkgs="build-base linux-headers openssl-dev pcre-dev git zlib-dev" \  
&& runtime_pkgs="ca-certificates openssl pcre zlib" \  
&& apk add --update-cache ${build_pkgs} ${runtime_pkgs} \  
&& cd /tmp \  
&& git clone --depth=1
https://github.com/yaoweibin/ngx_http_substitutions_filter_module
/tmp/ngx_http_substitutions_filter_module \  
&& wget http://nginx.org/download/${NGINX_VERSION}.tar.gz \  
&& tar xzf ${NGINX_VERSION}.tar.gz \  
&& cd /tmp/${NGINX_VERSION} \  
&& ./configure \  
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
\--with-http_sub_module \  
\--add-module=/tmp/ngx_http_substitutions_filter_module \  
&& make \  
&& make install \  
&& sed -i -e 's/#access_log logs\/access.log main;/access_log \/dev\/stdout;/'
-e 's/#error_log logs\/error.log notice;/error_log stderr notice;/'
/etc/nginx/nginx.conf \  
&& adduser -D nginx \  
&& rm -rf /tmp/* \  
&& apk del ${build_pkgs} \  
&& rm -rf /var/cache/apk/*  
  
COPY nginx.conf default.conf run_nginx /  
  
RUN mkdir -p /etc/services.d/nginx /srv/www/html /var/log/nginx
/var/cache/nginx /etc/nginx/conf.d && \  
mv /run_nginx /etc/services.d/nginx/run && \  
mv /nginx.conf /etc/nginx/nginx.conf && \  
mv /default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80  
  
VOLUME ["/var/cache/nginx", "/var/log/nginx", "/srv/www/html"]  
  
# Volumes  
# - Conf: /etc/nginx/conf.d (default.conf)  
# - Cache: /var/cache/nginx  
# - Logs: /var/log/nginx  
# - Data: /srv/www/html

