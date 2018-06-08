FROM ubuntu:14.04  
MAINTAINER Josh Chaney "josh@chaney.io"  
ADD modsecurity-2.8.0.tar.gz /root/temp/  
ADD nginx-1.7.4.tar.gz /root/temp/  
ADD modsecurity_data.tar.gz /etc/nginx/  
COPY nginx.conf /root/  
COPY nginx_ssl.conf /root/  
COPY modsecurity.conf /etc/nginx/  
COPY bootstrap.sh /sbin/  
  
RUN apt-get update && \  
apt-get install -y libpcre3-dev build-essential apache2-dev libxml2-dev && \  
cd /root/temp/modsecurity-2.8.0 && \  
./configure --enable-standalone-module --disable-mlogc && \  
make && \  
cd /root/temp/nginx-1.7.4 && \  
./configure --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf
--prefix=/etc/nginx --pid-path=/var/run/nginx.pid --error-log-
path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log
--lock-path=/var/lock/nginx.lock --add-
module=/root/temp/modsecurity-2.8.0/nginx/modsecurity --with-http_ssl_module
--without-http_access_module --without-http_auth_basic_module --without-
http_autoindex_module --without-http_empty_gif_module --without-
http_fastcgi_module --without-http_referer_module --without-
http_memcached_module --without-http_scgi_module --without-
http_split_clients_module --without-http_ssi_module --without-
http_uwsgi_module --with-http_spdy_module && \  
make && \  
make install && \  
apt-get purge -y build-essential && \  
apt-get -y autoremove && \  
rm -rf /root/temp && \  
chmod +x /sbin/bootstrap.sh  
  
ENV NXWP 1  
ENV NXWC 1024  
ENV FQDN www.example.com  
  
ENTRYPOINT ["bootstrap.sh"]  

