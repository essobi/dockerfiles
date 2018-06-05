# Build with:  
# docker build -t xpnsec/nginx-modsecurity  
# Run with:  
# docker run -d -it -p 80:80 -p 443:443 -v
/home/xpn/docker/nginx/html:/usr/local//nginx/html xpnsec/nginx-modsecurity  
# Logs with:  
# docker logs <INSTID>  
FROM ubuntu:14.04  
MAINTAINER xpnsec  
  
EXPOSE 80  
EXPOSE 443  
ADD files/modsecurity-2.9.1.tar.gz /usr/src/  
ADD files/nginx-1.11.7.tar.gz /usr/src/  
ADD files/crs-3.0.0.tar.gz /usr/src/  
  
RUN apt-get update && \  
apt-get install -y libpcre3-dev build-essential apache2-dev libxml2-dev && \  
cd /usr/src/modsecurity-2.9.1/ && \  
./configure --enable-standalone-module --disable-mlogc && \  
make && \  
cd /usr/src/nginx-1.11.7/ && \  
./configure --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf
--pid-path=/var/run/nginx.pid --error-log-path=/var/log/nginx/error.log
--http-log-path=/var/log/nginx/access.log --lock-path=/var/lock/nginx.lock
--add-module=/usr/src/modsecurity-2.9.1/nginx/modsecurity --with-
http_ssl_module --without-http_access_module --without-http_auth_basic_module
--without-http_autoindex_module --without-http_empty_gif_module --without-
http_fastcgi_module --without-http_referer_module --without-
http_memcached_module --without-http_scgi_module --without-
http_split_clients_module --without-http_ssi_module --without-
http_uwsgi_module --with-http_v2_module && \  
make && \  
make install  
  
ADD files/modsecurity.conf /etc/nginx/  
ADD files/unicode.mapping /etc/nginx/  
ADD files/crs_data/* /etc/nginx/  
ADD files/nginx.conf /etc/nginx/  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
CMD nginx  

