FROM nginx:1.13.9-alpine  
  
ENV NGINX_RTMP_MODULE_VERSION 1.2.1  
  
RUN apk add --no-cache --virtual .build-deps \  
curl \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
&& curl -fSL https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL https://github.com/arut/nginx-rtmp-
module/archive/v$NGINX_RTMP_MODULE_VERSION.tar.gz \  
-o nginx-rtmp-module.tar.gz \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& tar -zxC /usr/src -f nginx-rtmp-module.tar.gz \  
&& rm nginx.tar.gz \  
&& rm nginx-rtmp-module.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure \  
\--with-compat \  
\--with-debug \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--add-dynamic-module=/usr/src/nginx-rtmp-module-$NGINX_RTMP_MODULE_VERSION \  
&& make -j$(getconf _NPROCESSORS_ONLN) modules \  
&& install -m755 objs/ngx_rtmp_module.so
/usr/lib/nginx/modules/ngx_rtmp_module.so \  
&& rm -rf /usr/src/nginx-$NGINX_VERSION \  
&& rm -rf /usr/src/nginx-$NGINX_RTMP_MODULE_VERSION \  
&& apk del .build-deps \  
&& rm -f /etc/nginx/conf.d/*  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx-vh-*.conf /etc/nginx/conf.d/  
  
EXPOSE 80 1935  
  
STOPSIGNAL SIGTERM  
  
CMD ["nginx", "-g", "daemon off;"]  

