FROM ubuntu:14.04  
  
RUN apt-get -q -y update  
RUN apt-get -q -y install cron logrotate make build-essential libssl-dev
zlib1g-dev libpcre3 libpcre3-dev curl pgp yasm git libtool autoconf
apache2-prefork-dev libxml2-dev libcurl4-openssl-dev  
  
RUN apt-get -q -y build-dep nginx  
RUN apt-get -q -y clean  
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN groupadd nginx  
RUN useradd -m -g nginx nginx  
RUN mkdir -p /var/log/nginx /var/cache/nginx /root/src/nginx-rtmp
/root/src/nginx-rtmpt  
RUN git clone git://github.com/arut/nginx-rtmp-module.git /root/src/nginx-rtmp  
#RUN cd /root/src/nginx-rtmp && ./config && make  
RUN git clone https://github.com/kwojtek/nginx-rtmpt-proxy-module.git
/root/src/nginx-rtmpt  
#RUN cd /root/src/nginx-rtmpt && ./configure && make  
  
RUN mkdir /www && chown -R nginx:nginx /www  
  
RUN cd /root \  
&& curl -L -O http://nginx.org/download/nginx-1.10.1.tar.gz \  
&& curl -L -O http://nginx.org/download/nginx-1.10.1.tar.gz.asc \  
&& gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-key A1C052F8 \  
&& gpg nginx-1.10.1.tar.gz.asc \  
&& tar xzf nginx-1.10.1.tar.gz && cd nginx-1.10.1 \  
&& ./configure \  
--prefix=/etc/nginx \  
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
--add-module=/root/src/nginx-rtmp \  
--add-module=/root/src/nginx-rtmpt \  
--with-ipv6 \  
--with-threads \  
--with-stream \  
--with-stream_ssl_module \  
&& make install  
  
RUN ldconfig  
RUN mkdir /var/www && cp /root/src/nginx-rtmp/stat.xsl /var/www/stat.xsl  
  
EXPOSE 80  
EXPOSE 443  
  
CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]  

