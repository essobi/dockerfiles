FROM ubuntu  
MAINTAINER Daniel Ramirez <javamonn@gmail.com>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update && apt-get -y install \  
libreadline-dev libncurses5-dev libpcre3-dev libssl-dev perl make build-
essential wget libpq-dev  
  
RUN apt-get -y build-dep nginx \  
&& apt-get -q -y clean && rm -rf /var/cache/apt/archives/*
/var/lib/apt/lists/*  
  
RUN wget https://openresty.org/download/ngx_openresty-1.9.3.1.tar.gz \  
&& tar xvfz ngx_openresty-1.9.3.1.tar.gz \  
&& cd ngx_openresty-1.9.3.1 \  
&& ./configure --with-luajit --with-http_addition_module --with-
http_dav_module --with-http_geoip_module --with-http_gzip_static_module
--with-http_image_filter_module --with-http_realip_module --with-
http_stub_status_module --with-http_ssl_module --with-http_sub_module --with-
http_xslt_module --with-ipv6 --with-http_postgres_module --with-pcre-jit \  
&& make \  
&& make install \  
&& rm -rf /ngx_openresty*  
  
RUN mkdir /logs && chmod 777 /logs  
  
EXPOSE 80  
EXPOSE 443  
ADD revveries.nginx.conf ./revveries.nginx.conf  
CMD for file in /etc/secret/*; do source $file; done &&
/usr/local/openresty/nginx/sbin/nginx -p `pwd` -c revveries.nginx.conf  

