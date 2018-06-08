FROM debian:jessie  
  
MAINTAINER Vadim Slizov "z7zmey@gmail.com"  
  
ENV NGINX_VERSION 1.9.9  
ENV NGINX_REDIS2_MODULE_VERSION 0.12  
ENV NGINX_DEVEL_KIT_VERSION 0.2.19  
ENV NGINX_SET_MISC_MODULE_VERSION 0.29  
ENV NGINX_PUSH_STREAM_VERSION 0.5.1  
  
RUN apt-get update \  
&& apt-get install -y ca-certificates libpcre3 libssl-dev libpcre3-dev libgd-
dev make wget gcc  
  
# get nginx  
RUN wget "http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz" \  
&& mkdir -p /usr/src/nginx \  
&& tar -xof nginx-$NGINX_VERSION.tar.gz -C /usr/src/nginx --strip-components=1
\  
&& rm nginx-$NGINX_VERSION.tar.gz  
  
# get redis2 nginx module  
RUN wget "https://github.com/openresty/redis2-nginx-
module/archive/v$NGINX_REDIS2_MODULE_VERSION.tar.gz" \  
&& mkdir -p /usr/src/nginx/redis2-nginx-module \  
&& tar -xof v$NGINX_REDIS2_MODULE_VERSION.tar.gz -C
/usr/src/nginx/redis2-nginx-module \--strip-components=1 \  
&& rm v$NGINX_REDIS2_MODULE_VERSION.tar.gz  
  
# get nginx devel kit  
RUN wget
"https://github.com/simpl/ngx_devel_kit/archive/v$NGINX_DEVEL_KIT_VERSION.tar.gz"
\  
&& mkdir -p /usr/src/nginx/ngx_devel_kit \  
&& tar -xof v$NGINX_DEVEL_KIT_VERSION.tar.gz -C /usr/src/nginx/ngx_devel_kit
--strip-components=1 \  
&& rm v$NGINX_DEVEL_KIT_VERSION.tar.gz  
  
# get set misc nginx module  
RUN wget "https://github.com/openresty/set-misc-nginx-
module/archive/v$NGINX_SET_MISC_MODULE_VERSION.tar.gz" \  
&& mkdir -p /usr/src/nginx/set-misc-nginx-module \  
&& tar -xof v$NGINX_SET_MISC_MODULE_VERSION.tar.gz -C /usr/src/nginx/set-misc-
nginx-module \--strip-components=1 \  
&& rm v$NGINX_SET_MISC_MODULE_VERSION.tar.gz  
  
# get nginx push stream module  
RUN wget "https://github.com/wandenberg/nginx-push-stream-
module/archive/$NGINX_PUSH_STREAM_VERSION.tar.gz" \  
&& mkdir -p /usr/src/nginx/nginx-push-stream-module \  
&& tar -xof $NGINX_PUSH_STREAM_VERSION.tar.gz -C /usr/src/nginx/nginx-push-
stream-module \--strip-components=1 \  
&& rm $NGINX_PUSH_STREAM_VERSION.tar.gz  
  
WORKDIR /usr/src/nginx  
  
RUN useradd --no-create-home nginx  
  
# build  
RUN ./configure \  
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
\--with-mail \  
\--with-mail_ssl_module \  
\--with-file-aio \  
\--with-ipv6 \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-http_v2_module \  
\--with-http_image_filter_module \  
\--add-module=/usr/src/nginx/redis2-nginx-module \  
\--add-module=/usr/src/nginx/ngx_devel_kit \  
\--add-module=/usr/src/nginx/set-misc-nginx-module \  
\--add-module=/usr/src/nginx/nginx-push-stream-module \  
&& make -j2 \  
&& make install \  
&& make clean  
  
# clean  
RUN apt-get purge -yqq make wget gcc && \  
apt-get autoremove -yqq && \  
apt-get clean && \  
rm -rf /usr/src/nginx  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

