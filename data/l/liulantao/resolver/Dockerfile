FROM centos:centos7  
MAINTAINER Liu Lantao <liulantao@gmail.com>  
ENV REFRESHED_AT 2015-07-30  
RUN yum -y -q install http://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum makecache  
  
RUN yum -y -q install gcc pcre-devel openssl-devel make jemalloc-devel lua-
devel GeoIP-devel  
  
RUN useradd -r -d /etc/nginx -s /bin/false nginx  
  
WORKDIR /usr/src/tengine  
RUN curl -sLO http://tengine.taobao.org/download/tengine-2.1.0.tar.gz  
RUN tar zxvf tengine-2.1.0.tar.gz  
  
WORKDIR /usr/src/tengine/tengine-2.1.0  
RUN curl -sLO
https://github.com/Lax/ngx_http_accounting_module/archive/v0.4.tar.gz  
RUN tar zxvf v0.4.tar.gz  
  
RUN curl -sLO https://github.com/openresty/echo-nginx-
module/archive/v0.58.tar.gz  
RUN tar zxvf v0.58.tar.gz  
  
RUN ./configure --prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--http-client-body-temp-path=/var/cache/nginx/client_temp \  
--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
--user=nginx \  
--group=nginx \  
--with-http_geoip_module --with-http_lua_module --add-
module=ngx_http_accounting_module-0.4 --add-module=echo-nginx-module-0.58 \  
--with-http_ssl_module \  
--with-http_realip_module \  
--with-http_addition_module \  
--with-http_sub_module \  
--with-http_dav_module \  
--with-http_flv_module \  
--with-http_mp4_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_random_index_module \  
--with-http_secure_link_module \  
--with-http_stub_status_module \  
--with-http_auth_request_module \  
--with-mail \  
--with-mail_ssl_module \  
--with-file-aio \  
--with-http_spdy_module \  
--with-ipv6 \  
--with-jemalloc  
  
RUN make  
RUN make install  
  
RUN curl -sLO
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
&& gunzip GeoIP.dat.gz  
RUN mv GeoIP.dat /etc/nginx  
#RUN curl -sLO
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz &&
gunzip GeoLiteCity.dat.gz  
#RUN mv GeoLiteCity.dat /etc/nginx  
  
RUN mkdir -p /var/cache/nginx  
RUN chown nginx.nginx /var/cache/nginx  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY resolver.conf /etc/nginx/conf.d/resolver.conf  
  
ENTRYPOINT ["/usr/sbin/nginx"]  
CMD ["-g", "daemon off;"]  

