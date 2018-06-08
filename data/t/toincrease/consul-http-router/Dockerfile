FROM alpine:3.3  
MAINTAINER Ron van der Wijngaard <rvdwijngaard@to-increase.com>  
  
ENV NGINX_VERSION nginx-1.7.10  
ENV HEADERS_MORE_VERSION 0.261  
ENV CONSUL_TEMPLATE_VERSION 0.14.0  
RUN apk update && \  
apk add openssl-dev pcre-dev zlib-dev wget build-base && \  
mkdir -p /tmp/src && \  
cd /tmp/src && \  
wget --no-check-certificate https://github.com/openresty/headers-more-nginx-
module/archive/v${HEADERS_MORE_VERSION}.tar.gz && \  
tar -zxvf v${HEADERS_MORE_VERSION}.tar.gz && \  
wget http://nginx.org/download/${NGINX_VERSION}.tar.gz && \  
tar -zxvf ${NGINX_VERSION}.tar.gz && \  
cd /tmp/src/${NGINX_VERSION} && \  
./configure \  
\--with-http_ssl_module \  
\--with-http_gzip_static_module \  
\--prefix=/opt/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--add-module=/tmp/src/headers-more-nginx-module-${HEADERS_MORE_VERSION} \  
\--pid-path=/var/run/nginx.pid \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--sbin-path=/usr/sbin/nginx && \  
make && \  
make install && \  
apk del build-base && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
RUN cd / \  
&& wget --no-check-certificate -O consul-template.zip
https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& unzip consul-template.zip \  
&& rm /consul-template.zip \  
&& mkdir -p /tmp/nginx/client-body \  
&& apk del wget \  
&& rm -rf /var/cache/apk/*  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD cors-options.conf /etc/nginx/cors-options.conf  
ADD cache-control.conf /etc/nginx/cache-control.conf  
ADD index.html /www/index.html  
ADD reload.sh /reload.sh  
RUN chmod +x /reload.sh  
ADD nginx.ctmpl /nginx.ctmpl  
ADD robots.txt /etc/nginx/robots.txt  
  
EXPOSE 80  
EXPOSE 81  
ENTRYPOINT ["/consul-template"]  
CMD ["-consul", "consul.service.consul:8500", "-dedup", "-template",
"/nginx.ctmpl:/etc/nginx/nginx.conf:/reload.sh"]  

