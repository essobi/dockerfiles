FROM fishisfast/ruby  
  
### ** RAILS APP ** ###  
RUN gem install foreman  
  
ENV APP_PATH /app  
RUN mkdir -p $APP_PATH  
WORKDIR $APP_PATH  
  
# Extracted from https://github.com/nginxinc/docker-
nginx/blob/master/mainline/jessie/Dockerfile  
### ** NGINX to serve assets ** ###  
ENV NGINX_VERSION 1.11.13-1~jessie  
  
RUN set -e; \  
NGINX_GPGKEY=573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62; \  
found=''; \  
for server in \  
ha.pool.sks-keyservers.net \  
hkp://keyserver.ubuntu.com:80 \  
hkp://p80.pool.sks-keyservers.net:80 \  
pgp.mit.edu \  
; do \  
echo "Fetching GPG key $NGINX_GPGKEY from $server"; \  
apt-key adv --keyserver "$server" \--keyserver-options timeout=10 --recv-keys
"$NGINX_GPGKEY" && found=yes && break; \  
done; \  
test -z "$found" && echo >&2 "error: failed to fetch GPG key $NGINX_GPGKEY" &&
exit 1; \  
exit 0  
  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN mkdir -p /etc/nginx/conf.d  
COPY nginx_default.conf /etc/nginx/conf.d/default.conf  

