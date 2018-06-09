FROM ubuntu:14.04  
LABEL maintainer="a2279871@gmail.com"  
  
RUN apt-get update  
RUN apt-get install vim wget curl make build-essential -y  
  
WORKDIR /usr/src  
  
RUN apt-get install libgeoip-dev -y  
RUN apt-get install libxslt-dev -y  
RUN apt-get install libgd2-xpm-dev -y  
RUN apt-get install unzip -y  
RUN apt-get install libpam0g-dev -y  
  
# pcre  
RUN wget
ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.41.tar.gz -O
pcre.tar.gz \  
&& mkdir pcre \  
&& tar -zxf pcre.tar.gz -C pcre --strip-components=1  
# && cd pcre-8.41 && ./configure && make && make install  
# zlib  
RUN wget http://zlib.net/zlib-1.2.11.tar.gz -O zlib.tar.gz \  
&& mkdir zlib \  
&& tar -zxf zlib.tar.gz -C zlib --strip-components=1  
#&& cd zlib-1.2.11 && ./configure && make && make install  
# openssl  
RUN wget https://www.openssl.org/source/openssl-1.0.2l.tar.gz -O
openssl.tar.gz \  
&& mkdir openssl \  
&& tar -zxf openssl.tar.gz -C openssl --strip-components=1  
# && cd openssl-1.0.2l && ./config --prefix=/usr && make && make install  
# nginx 3rd party module  
RUN wget https://github.com/gnosek/nginx-upstream-fair/archive/master.zip -O
nginx-upstream-fair-master.zip \  
&& unzip nginx-upstream-fair-master.zip  
  
# Pluggable Authentication Module  
# RUN wget https://github.com/sto/ngx_http_auth_pam_module/archive/master.zip
-O ngx_http_auth_pam_module-master.zip \  
# && unzip ngx_http_auth_pam_module-master  
RUN wget
https://github.com/yaoweibin/ngx_http_substitutions_filter_module/archive/master.zip
-O ngx_http_substitutions_filter_module-master.zip \  
&& unzip ngx_http_substitutions_filter_module-master.zip  
  
# nginx-echo module  
# RUN wget https://github.com/openresty/echo-nginx-module/archive/master.zip
-O echo-nginx-module-master.zip \  
# && unzip echo-nginx-module-master.zip  
# sticky module  
RUN wget https://bitbucket.org/nginx-goodies/nginx-sticky-module-
ng/get/1.2.6.tar.gz -O nginx-sticky-module.tar.gz \  
&& mkdir nginx-sticky-module && tar -xzf nginx-sticky-module.tar.gz -C nginx-
sticky-module --strip-components=1  
  
# nginx  
# http://nginx.org/en/docs/configure.html  
# https://www.nginx.com/resources/admin-guide/installing-nginx-open-source/  
RUN wget http://nginx.org/download/nginx-1.9.15.tar.gz  
RUN tar -zxf nginx-1.9.15.tar.gz  
RUN cd nginx-1.9.15 && ./configure \  
\--prefix=/usr/share/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--with-pcre=../pcre --with-zlib=../zlib --with-openssl=../openssl \  
\--without-http_fastcgi_module \  
\--without-http_uwsgi_module \  
\--without-http_scgi_module \  
\--with-debug \  
\--with-stream \  
\--with-ipv6 \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_dav_module \  
\--with-http_gzip_static_module \  
\--with-http_v2_module \  
\--with-http_sub_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-http_geoip_module \  
\--with-http_xslt_module \  
\--with-http_image_filter_module \  
\--with-http_dav_module \  
\--add-module=../nginx-upstream-fair-master \  
\--add-module=../ngx_http_substitutions_filter_module-master \  
\--add-module=../nginx-sticky-module \  
&& make && make install  
  
# --add-module=../echo-nginx-module-master \  
# --add-module=../ngx_http_auth_pam_module-master \  
# --http-client-body-temp-path=/var/lib/nginx/body \  
# --http-proxy-temp-path=/var/lib/nginx/proxy \  
WORKDIR /etc/nginx  
CMD ["nginx", "-g", "'daemon off;'"]  

