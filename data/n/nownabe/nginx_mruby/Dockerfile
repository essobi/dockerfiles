FROM alpine:3.6  
MAINTAINER nownabe  
  
ENV NGX_MRUBY_VERSION 1.19.4  
  
# For build.sh  
ENV NGINX_CONFIG_OPT_ENV \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--with-http_ssl_module \  
\--with-http_v2_module \  
\--with-http_realip_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_stub_status_module  
  
RUN \  
apk add \--no-cache --update openssl-dev pcre-dev \  
&& apk add \--no-cache --virtual .build-deps \  
build-base \  
ruby-dev \  
ruby-rake \  
tar \  
wget \  
bison \  
perl \  
curl \  
git \  
&& curl -sLSo ngx_mruby.tar.gz
https://github.com/matsumotory/ngx_mruby/archive/v${NGX_MRUBY_VERSION}.tar.gz
\  
&& tar zxf ngx_mruby.tar.gz \  
&& cd ngx_mruby-${NGX_MRUBY_VERSION} \  
&& sh build.sh \  
&& make install \  
&& cd \  
  
# Initialize  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& mkdir -p /etc/nginx/conf.d \  
  
# envsubst  
&& apk add \--no-cache libintl gettext \  
&& cp /usr/bin/envsubst /usr/local/bin/envsubst \  
  
# Clean up  
&& apk del .build-deps gettext \  
&& rm -rf ngx_mruby-${NGX_MRUBY_VERSION} /var/cache/apk/*  
  
# ENV ENVS $$FOO$$BAR  
# ADD entrypoint.sh /entrypoint.sh  
# ADD nginx.conf.template /etc/nginx/nginx.conf.template  
  
ADD nginx.conf /etc/nginx/nginx.conf  
  
# CMD sh entrypoint.sh  
CMD /usr/local/sbin/nginx -c /etc/nginx/nginx.conf -g "daemon off;"  

