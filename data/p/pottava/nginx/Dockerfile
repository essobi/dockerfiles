# Nginx v1.8  
# docker run --rm -p 80:80 -v $(pwd)/html:/etc/nginx/html pottava/nginx:1.8  
# docker run --rm -p 80:80 -v
$(pwd)/conf/nginx.conf:/etc/nginx/conf/nginx.conf pottava/nginx:1.8  
  
FROM alpine:3.4  
  
ENV NGINX_VERSION=1.8.1  
  
RUN apk --no-cache add --virtual build-dependencies build-base curl \  
&& apk --no-cache add pcre-dev openssl-dev libatomic_ops-dev \  
&& set -e \  
&& mkdir -p /tmp/src /var/lib/nginx /var/log/nginx \  
&& cd /tmp/src \  
&& curl \--location --silent
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar xzf - \  
&& cd /tmp/src/nginx-${NGINX_VERSION} \  
&& ./configure \  
\--with-cc-opt="-Wno-maybe-uninitialized -Wno-pointer-sign" \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/local/sbin/nginx \  
\--pid-path=/run/nginx.pid \  
\--lock-path=/run/nginx.lock \  
\--with-ipv6 \  
\--with-libatomic \  
\--with-pcre \  
\--with-pcre-jit \  
\--http-client-body-temp-path=/var/lib/nginx/client_body_temp \  
\--http-proxy-temp-path=/var/lib/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/var/lib/nginx/fastcgi_temp \  
\--http-uwsgi-temp-path=/var/lib/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/lib/nginx/scgi_temp \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_gzip_static_module \  
\--with-http_realip_module \  
\--with-http_sub_module \  
\--with-http_secure_link_module \  
&& make \  
&& make install \  
&& apk del --purge build-dependencies \  
&& cd / \  
&& rm -rf /tmp/src /var/www/html \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
CMD ["nginx", "-g", "daemon off;"]  

