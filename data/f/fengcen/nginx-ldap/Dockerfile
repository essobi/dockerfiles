FROM debian:jessie  
  
MAINTAINER fengcen <fengcen.love@gmail.com>  
  
ENV NGINX_VERSION 1.11.13  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN BUILD_PACKAGES="\  
gcc \  
make \  
libpcre3-dev \  
libldap2-dev \  
libssl-dev \  
libxslt-dev \  
libgd2-xpm-dev \  
libgeoip-dev \  
libperl-dev \  
wget" \  
&& CONFIG="\  
--add-module=/usr/src/nginx-auth-ldap-master \  
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
--with-http_xslt_module=dynamic \  
--with-http_image_filter_module=dynamic \  
--with-http_geoip_module=dynamic \  
--with-http_perl_module=dynamic \  
--with-threads \  
--with-stream \  
--with-stream_ssl_module \  
--with-stream_ssl_preread_module \  
--with-stream_realip_module \  
--with-stream_geoip_module=dynamic \  
--with-http_slice_module \  
--with-mail \  
--with-mail_ssl_module \  
--with-compat \  
--with-file-aio \  
--with-http_v2_module \  
" \  
&& echo 'deb http://ftp.debian.org/debian/ jessie-backports main' >
/etc/apt/sources.list.d/backports.list \  
&& apt-get update \  
&& apt-get install -t jessie-backports -y $BUILD_PACKAGES \  
&& mkdir /var/log/nginx \  
&& mkdir /etc/nginx \  
&& wget https://github.com/kvspb/nginx-auth-ldap/archive/master.tar.gz -O
ldap.tar.gz \  
&& wget http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -O nginx.tar.gz
\  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f ldap.tar.gz \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm ldap.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure $CONFIG --with-debug \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& mv objs/nginx objs/nginx-debug \  
&& mv objs/ngx_http_xslt_filter_module.so objs/ngx_http_xslt_filter_module-
debug.so \  
&& mv objs/ngx_http_image_filter_module.so objs/ngx_http_image_filter_module-
debug.so \  
&& mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \  
&& mv objs/ngx_http_perl_module.so objs/ngx_http_perl_module-debug.so \  
&& mv objs/ngx_stream_geoip_module.so objs/ngx_stream_geoip_module-debug.so \  
&& ./configure $CONFIG \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& mkdir -p /var/cache/nginx/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \  
&& install -m755 objs/ngx_http_xslt_filter_module-debug.so
/usr/lib/nginx/modules/ngx_http_xslt_filter_module-debug.so \  
&& install -m755 objs/ngx_http_image_filter_module-debug.so
/usr/lib/nginx/modules/ngx_http_image_filter_module-debug.so \  
&& install -m755 objs/ngx_http_geoip_module-debug.so
/usr/lib/nginx/modules/ngx_http_geoip_module-debug.so \  
&& install -m755 objs/ngx_http_perl_module-debug.so
/usr/lib/nginx/modules/ngx_http_perl_module-debug.so \  
&& install -m755 objs/ngx_stream_geoip_module-debug.so
/usr/lib/nginx/modules/ngx_stream_geoip_module-debug.so \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& strip /usr/lib/nginx/modules/*.so \  
&& cd .. \  
&& rm -rf nginx-auth-ldap-master \  
&& rm -rf nginx-$NGINX_VERSION \  
&& apt-get remove --purge -y $BUILD_PACKAGES $(apt-mark showauto) \  
&& apt-get install -t jessie-backports -y libldap2-dev libssl-dev \  
&& rm -rf /var/lib/apt/lists/* \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

