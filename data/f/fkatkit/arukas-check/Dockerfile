FROM alpine:3.3  
  
ENV NGINX_VERSION=1.10.0 \  
SAMPLEENV=unabled \  
NEXTENV=unabled  
  
COPY cmd.sh envchk.sh /  
  
RUN apk --update add pcre-dev openssl-dev \  
&& apk add --virtual build-dependencies build-base curl \  
&& curl -SLO http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \  
&& tar xzvf nginx-${NGINX_VERSION}.tar.gz \  
&& cd nginx-${NGINX_VERSION} \  
&& ./configure \  
\--with-http_ssl_module \  
\--with-http_gzip_static_module \  
\--prefix=/usr/share/nginx \  
\--sbin-path=/usr/local/sbin/nginx \  
\--conf-path=/etc/nginx/conf/nginx.conf \  
\--pid-path=/var/run/nginx.pid \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
&& make \  
&& make install \  
&& cd / \  
&& apk del build-dependencies \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& rm -rf \  
nginx-${NGINX_VERSION} \  
nginx-${NGINX_VERSION}.tar.gz \  
/var/cache/apk/* \  
&& echo '*/1 * * * * /envchk.sh' >> /etc/crontabs/root \  
&& chmod 755 /cmd.sh \  
&& chmod 755 /envchk.sh  
COPY index.html /usr/share/nginx/html/  
  
  
EXPOSE 80 443  
  
CMD crond start && /envchk.sh && nginx -g "daemon off;"  

