FROM debian:jessie  
MAINTAINER Keith Bentrup <kbentrup@magento.com>  
  
# reference: https://github.com/nginxinc/docker-nginx  
# compile options from "docker run nginx nginx -V"  
  
ENV NGINX_VERSION 1.10.0  
  
# mostly default options but with image filter  
# note: can't remove all build dependencies (cf. apt-get install vs
autoremove). some needed even after build.  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes curl \  
install-info \  
gnupg \  
build-essential \  
libpcre3 \  
libpcre3-dev \  
zlib1g-dev \  
ca-certificates \  
libssl-dev \  
zip \  
libgd2-xpm-dev && \  
cd /tmp && \  
curl -O http://nginx.org/download/nginx-1.10.0.tar.gz && \  
tar -zxf nginx-1.10.0.tar.gz && \  
cd nginx-1.10.0 && \  
./configure \  
--prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
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
--with-http_ssl_module \  
--with-http_realip_module \  
--with-http_addition_module \  
--with-http_sub_module \  
--with-http_dav_module \  
--with-http_flv_module \  
--with-http_mp4_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_random_index_module \  
--with-http_secure_link_module \  
--with-http_stub_status_module \  
--with-http_auth_request_module \  
--with-http_image_filter_module \  
--with-mail \  
--with-mail_ssl_module \  
--with-file-aio \  
--with-http_v2_module \  
--with-cc-opt='-g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat
-Werror=format-security -Wp,-D_FORTIFY_SOURCE=2' \  
--with-ld-opt='-Wl,-z,relro -Wl,--as-needed' \  
--with-ipv6 && \  
make && \  
cp /tmp/nginx-1.10.0/objs/nginx /usr/sbin/nginx && \  
useradd nginx && \  
apt-get --purge autoremove -y --force-yes curl \  
install-info \  
build-essential \  
libpcre3-dev \  
ca-certificates \  
libssl-dev \  
zip && \  
apt-get clean && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
COPY nginx /etc/nginx/  
COPY docker-entrypoint.sh /  
  
# forward request and error logs to docker log collector  
RUN mkdir -p /etc/nginx/conf.d /var/log/nginx && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 80 443  

