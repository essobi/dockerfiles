FROM kazukgw/docker-ffmpeg  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
136221EE520DDFAF0A905689B9316A7BC7917B12 \  
&& apt-get -q -y update \  
&& apt-get -q -y install cron luarocks supervisor logrotate \  
make build-essential libpcre3-dev libssl-dev wget \  
iputils-arping libexpat1-dev \  
libpcre3-dev libssl-dev curl\  
&& apt-get -q -y clean && rm -rf /var/cache/apt/archives/*
/var/lib/apt/lists/*  
  
RUN groupadd nginx  
RUN useradd -m -g nginx nginx  
  
ADD nginx-rtmp-module /root/nginx-rtmp-module  
  
ENV OPENRESTY_VERSION 1.9.7.1  
RUN wget -nv
http://openresty.org/download/ngx_openresty-$OPENRESTY_VERSION.tar.gz \  
-O /root/ngx_openresty-$OPENRESTY_VERSION.tar.gz \  
&& tar -xzf /root/ngx_openresty-$OPENRESTY_VERSION.tar.gz -C /root/ \  
&& cd /root/ngx_openresty-$OPENRESTY_VERSION/ \  
&& ./configure --prefix=/usr/local/openresty --with-http_gunzip_module --with-
luajit \  
\--with-luajit-xcflags=-DLUAJIT_ENABLE_CHECKHOOK \  
\--http-client-body-temp-path=/var/nginx/client_body_temp \  
\--http-proxy-temp-path=/var/nginx/proxy_temp \  
\--http-log-path=/var/nginx/access.log \  
\--error-log-path=/var/nginx/error.log \  
\--pid-path=/var/nginx/nginx.pid \  
\--lock-path=/var/nginx/nginx.lock \  
\--with-http_stub_status_module \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--without-http_fastcgi_module \  
\--without-http_uwsgi_module \  
\--without-http_scgi_module \  
\--add-module=/root/nginx-rtmp-module --user=nginx \  
&& make \  
&& make install  
  
RUN mkdir -p /var/log/nginx \  
/usr/local/openresty/nginx/conf/server_conf \  
/usr/local/openresty/nginx/conf/rtmp_conf \  
/usr/local/openresty/nginx/conf/lua  
  
ADD nginx.conf.template /usr/local/openresty/nginx/conf/nginx.conf.template  
ADD appinit /usr/bin/appinit  
RUN chmod 744 /usr/bin/appinit  
  
EXPOSE 80  
EXPOSE 1935  
EXPOSE 6379  
CMD ["appinit"]  

