FROM ubuntu:16.04  
  
# COMMON section  
RUN apt-get update  
RUN apt-get install -y software-properties-common unzip vim git curl wget
build-essential less  
  
# HHVM section  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449  
RUN add-apt-repository "deb http://dl.hhvm.com/ubuntu $(lsb_release -sc) main"  
RUN apt-get update  
  
RUN apt-get install -y hhvm  
RUN /usr/share/hhvm/install_fastcgi.sh  
RUN update-rc.d hhvm defaults  
RUN /usr/bin/update-alternatives --install /usr/bin/php php /usr/bin/hhvm 60  
  
# NGINX openrestly section  
RUN apt-get -y install nginx-extras build-essential libpcre3-dev libssl-dev
libgeoip-dev libpq-dev libxslt1-dev libgd2-xpm-dev  
RUN wget -c https://openresty.org/download/openresty-1.9.15.1.tar.gz  
RUN tar zxvf openresty-1.9.15.1.tar.gz  
RUN cd openresty-1.9.15.1 && ./configure \  
--sbin-path=/usr/sbin/nginx \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--http-client-body-temp-path=/var/lib/nginx/body \  
--http-fastcgi-temp-path=/var/lib/nginx/fastcgi \  
--http-log-path=/var/log/nginx/access.log \  
--http-proxy-temp-path=/var/lib/nginx/proxy \  
--http-scgi-temp-path=/var/lib/nginx/scgi \  
--http-uwsgi-temp-path=/var/lib/nginx/uwsgi \  
--lock-path=/var/lock/nginx.lock \  
--pid-path=/var/run/nginx.pid \  
--with-sha1=/usr/include/openssl \  
--with-md5=/usr/include/openssl \  
--with-http_stub_status_module \  
--with-http_secure_link_module \  
--with-luajit \  
--with-pcre-jit \  
--with-debug \  
--with-http_auth_request_module \  
--with-http_addition_module \  
--with-http_gunzip_module \  
--with-http_image_filter_module \  
--with-http_dav_module \  
--with-http_flv_module \  
--with-http_geoip_module \  
--with-http_gzip_static_module \  
--with-http_realip_module \  
--with-http_stub_status_module \  
--with-http_ssl_module \  
--with-http_sub_module \  
--with-http_xslt_module \  
--with-ipv6 \  
--with-http_postgres_module && \  
make && \  
make install  
  
RUN apt-get -y autoclean  
RUN apt-get -y autoremove  
  
RUN rm -f /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
ADD default /etc/nginx/sites-available/default  
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
  
RUN mkdir -p /var/cache/nginx  
RUN chown www-data:www-data /var/cache/nginx  
  
ADD entrypoint.sh /usr/local/bin/entrypoint  
RUN chmod +x /usr/local/bin/entrypoint  
  
EXPOSE 80  
EXPOSE 443  
  
#ENTRYPOINT /usr/local/bin/entrypoint  
CMD /usr/local/bin/entrypoint  
  
  

