FROM alpine:edge  
  
ENV NGINX_VERSION 1.12.1  
# Install required software  
RUN \  
apk add --no-cache pcre openldap && \  
apk add --no-cache --virtual build-dependencies build-base curl pcre-dev
openldap-dev zlib-dev && \  
curl -sL http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz -o
/nginx.tar.gz && \  
curl -sL https://github.com/kvspb/nginx-auth-ldap/archive/master.zip -o
/nginx-auth-ldap.zip && \  
mkdir /var/log/nginx \  
&& mkdir /etc/nginx \  
&& tar -C ~/ -xzf /nginx.tar.gz \  
&& unzip -x /nginx-auth-ldap.zip -d ~/ \  
&& cd ~/nginx-${NGINX_VERSION} \  
&& ./configure \  
\--add-module=/root/nginx-auth-ldap-master \  
\--with-http_ssl_module \  
\--with-http_v2_module \  
\--with-debug \  
\--conf-path=/etc/nginx/nginx.conf \  
\--sbin-path=/usr/sbin/nginx \  
\--pid-path=/var/log/nginx/nginx.pid \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
&& make install \  
&& cd .. \  
&& rm -rf nginx-auth-ldap \  
&& rm -rf nginx-${NGINX_VERSION} \  
&& apk del build-dependencies \  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
  
EXPOSE 80 443  
  
CMD ["/usr/sbin/nginx","-g","daemon off;"]  

