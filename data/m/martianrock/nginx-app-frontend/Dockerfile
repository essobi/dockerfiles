FROM alpine:3.6  
  
ENV NGINX_VERSION=1.13.5 \  
NGINX_HTTP_AUTH_PAM_MODULE_VERSION=1.5.1 \  
NGINX_RTMP_MODULE_VERSION=1.2.0 \  
NGINX_DAV_EXT_MODULE_VERSION=0.1.0 \  
NGINX_HTTP_SHIBBOLETH_VERSION=2.0.1 \  
NGINX_UPSTREM_FAIR_VERSION=0.1.2 \  
NGINX_STICKY_MODULE_NG_VERSION=master \  
NGINX_AUTH_LDAP_VERSION=master  
  
RUN cd ~ &&\  
echo 'if [ "_master" != _$3 ]; then export pref="v"; else export pref=""; fi;
wget --no-check-certificate $1/$2/archive/$pref$3.zip && unzip $pref$3 && mv
$2-$3 $2' > getgh && chmod +x getgh && \  
apk --update add musl-dev libressl-dev pcre-dev zlib-dev geoip-dev expat-dev
apr-dev apr-util-dev curl-dev linux-pam-dev && \  
apk --update add --no-cache --virtual .build-dependencies gcc make wget && \  
./getgh https://github.com/kvspb nginx-auth-ldap master && \  
./getgh https://github.com/arut nginx-dav-ext-module
${NGINX_DAV_EXT_MODULE_VERSION} && \  
./getgh https://github.com/nginx-shib nginx-http-shibboleth
${NGINX_HTTP_SHIBBOLETH_VERSION} && \  
./getgh https://github.com/itoffshore nginx-upstream-fair
${NGINX_UPSTREM_FAIR_VERSION} && \  
./getgh https://github.com/sto ngx_http_auth_pam_module
${NGINX_HTTP_AUTH_PAM_MODULE_VERSION} && \  
./getgh https://github.com/arut nginx-rtmp-module ${NGINX_RTMP_MODULE_VERSION}
&& \  
wget --no-check-certificate https://bitbucket.org/nginx-goodies/nginx-sticky-
module-ng/get/${NGINX_STICKY_MODULE_NG_VERSION}.zip && mkdir temp && unzip
${NGINX_STICKY_MODULE_NG_VERSION} -d temp && mkdir nginx-sticky-module && mv
temp/*/* nginx-sticky-module/ && rm -rf temp
${NGINX_STICKY_MODULE_NG_VERSION}.zip && \  
wget --no-check-certificate
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && tar -zxvf
nginx-${NGINX_VERSION}.tar.gz && rm nginx-${NGINX_VERSION}.tar.gz && \  
cd nginx-${NGINX_VERSION} && \  
./configure \  
\--with-http_addition_module \  
\--with-http_ssl_module \  
\--with-http_gzip_static_module \  
\--with-http_stub_status_module \  
\--with-http_realip_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_geoip_module=dynamic \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_v2_module \  
\--with-http_sub_module \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-stream_geoip_module=dynamic \  
\--with-mail_ssl_module \  
\--with-compat \  
\--add-dynamic-module=../nginx-auth-ldap \  
\--add-dynamic-module=../nginx-dav-ext-module \  
\--add-dynamic-module=../nginx-http-shibboleth \  
\--add-dynamic-module=../nginx-upstream-fair \  
\--add-dynamic-module=../nginx-sticky-module \  
\--add-dynamic-module=../ngx_http_auth_pam_module \  
\--add-dynamic-module=../nginx-rtmp-module \  
\--prefix=/etc/nginx \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--modules-path=/usr/lib/nginx/modules \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
&& \  
addgroup -S nginx && \  
adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx && \  
make && make install && \  
rm -rf /etc/nginx/html/ && \  
mkdir /etc/nginx/conf.d/ && \  
mkdir -p /usr/share/nginx/html/ && \  
install -m644 html/index.html /usr/share/nginx/html/ && \  
install -m644 html/50x.html /usr/share/nginx/html/ && \  
ln -s ../../usr/lib/nginx/modules /etc/nginx/modules && \  
strip /usr/sbin/nginx && \  
strip /usr/lib/nginx/modules/*.so && \  
apk del .build-dependencies && \  
rm -rf ~/* && \  
rm -rf /var/cache/apk/* && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
echo -e $(echo "\  
user nginx;\\n\  
worker_processes 1;\\n\  
error_log /var/log/nginx/error.log warn;\\n\  
pid /var/run/nginx.pid;\\n\  
events {\\n\  
worker_connections 1024;\\n\  
}\\n\  
\\n\  
http {\\n\  
include /etc/nginx/mime.types;\\n\  
default_type application/octet-stream;\\n\  
log_format main '\$remote_addr - \$remote_user [\$time_local] \"\$request\"
'\\n\  
'\$status \$body_bytes_sent \"\$http_referer\" '\\n\  
'\"\$http_user_agent\" \"\$http_x_forwarded_for\"';\\n\  
access_log /var/log/nginx/access.log main;\\n\  
sendfile on;\\n\  
#tcp_nopush on;\\n\  
keepalive_timeout 65;\\n\  
#gzip on;\\n\  
include /etc/nginx/conf.d/*.conf;\\n\  
}\\n\  
")> /etc/nginx/nginx.conf  
  
VOLUME ["/var/log/nginx"]  
  
WORKDIR /etc/nginx  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  
  

