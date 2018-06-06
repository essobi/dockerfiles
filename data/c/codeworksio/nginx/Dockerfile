FROM codeworksio/ubuntu:18.04-20180210  
# SEE: https://github.com/nginxinc/docker-
nginx/blob/master/mainline/alpine/Dockerfile  
ARG APT_PROXY  
ARG APT_PROXY_SSL  
ENV NGINX_VERSION="1.13.8"  
RUN set -ex; \  
\  
buildDependencies="\  
build-essential \  
libpcre3-dev \  
libssl-dev \  
zlib1g-dev \  
"; \  
if [ -n "$APT_PROXY" ]; then echo "Acquire::http { Proxy
\"http://${APT_PROXY}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
if [ -n "$APT_PROXY_SSL" ]; then echo "Acquire::https { Proxy
\"https://${APT_PROXY_SSL}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
apt-get --yes update; \  
apt-get --yes install \  
$buildDependencies \  
; \  
configureOptions="\  
\--user=$SYSTEM_USER \  
\--group=$SYSTEM_USER \  
\--sbin-path=/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--with-file-aio \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_ssl_module \  
\--with-threads \  
"; \  
cd /tmp; \  
curl -L "https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz" -o
nginx-$NGINX_VERSION.tar.gz; \  
tar -xf nginx-$NGINX_VERSION.tar.gz; \  
cd /tmp/nginx-$NGINX_VERSION; \  
./configure $configureOptions \--with-debug; \  
make -j$(getconf _NPROCESSORS_ONLN); \  
mv objs/nginx objs/nginx-debug; \  
\  
./configure $configureOptions; \  
make -j$(getconf _NPROCESSORS_ONLN); \  
make install; \  
install -m755 objs/nginx-debug /sbin/nginx-debug; \  
strip /sbin/nginx*; \  
\  
mkdir -p \  
/etc/nginx/conf.d \  
/usr/local/nginx \  
/var/log/nginx; \  
chown -R $SYSTEM_USER:$SYSTEM_USER \  
/usr/local/nginx \  
/var/log/nginx; \  
\  
apt-get purge --yes --auto-remove $buildDependencies; \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apt/*; \  
rm -f /etc/apt/apt.conf.d/00proxy  
  
COPY assets/ /  
  
VOLUME [ "/var/www" ]  
EXPOSE 8080 8443  
CMD [ "/sbin/init.sh" ]  
  
### METADATA
###################################################################  
ARG IMAGE  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
ARG VCS_URL  
LABEL \  
org.label-schema.name=$IMAGE \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.schema-version="1.0"  

