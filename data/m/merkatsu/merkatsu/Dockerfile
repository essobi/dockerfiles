FROM mhart/alpine-node:4  
ENV NGINX_VERSION nginx-1.9.5  
WORKDIR /src  
  
ADD . .  
  
RUN chmod +x docker_init.sh  
  
RUN apk --update add make gcc g++ python openssl-dev pcre-dev zlib-dev wget
build-base \  
&& wget http://nginx.org/download/${NGINX_VERSION}.tar.gz \  
&& tar -zxvf ${NGINX_VERSION}.tar.gz \  
&& cd ${NGINX_VERSION} \  
&& ./configure \  
\--with-http_ssl_module \  
\--with-http_v2_module \  
\--with-http_gzip_static_module \  
\--prefix=/etc/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--sbin-path=/usr/local/sbin/nginx \  
&& make \  
&& make install \  
&& cd /src \  
&& rm -rf ${NGINX_VERSION} && rm ${NGINX_VERSION}.tar.gz \  
&& rm -rf /etc/nginx/nginx.conf \  
&& npm install --production \  
&& apk del make gcc g++ python wget build-base \  
&& rm -rf /tmp/* /root/.npm /root/.node-gyp /var/cache/apk/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr
/var/log/nginx/error.log  
  
RUN cp nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80 443  
CMD ["./docker_init.sh"]

