FROM alpine  
MAINTAINER lucienchu<lucienchu@hotmail.com>  
  
RUN apk update \  
&& apk upgrade \  
&& apk add curl \  
pcre-dev \  
zlib-dev \  
zlib \  
unzip \  
perl \  
openssl \  
make \  
gcc \  
libc-dev \  
libpq \  
postgresql-dev \  
git \  
postgresql-client \  
linux-headers \  
netcat-openbsd  
  
WORKDIR /app  
  
RUN git clone https://github.com/yzprofile/ngx_http_dyups_module.git \  
&& git clone https://github.com/openresty/stream-lua-nginx-module.git  
  
# openssl  
RUN curl --progress --remote-name
https://www.openssl.org/source/openssl-1.0.2j.tar.gz \  
&& tar zxvf openssl-1.0.2j.tar.gz \  
&& cd openssl-1.0.2j \  
&& ./config \  
&& make && make install\  
&& make clean \  
&& ./config shared \  
&& make && make install  
  
# openresty  
RUN cd /app \  
&& curl --progress --remote-name
https://openresty.org/download/openresty-1.11.2.1.tar.gz \  
&& tar zxvf openresty-1.11.2.1.tar.gz \  
&& cd openresty-1.11.2.1 \  
&& ./configure --prefix=/usr/local/openresty \  
\--with-luajit \  
\--with-http_ssl_module \  
\--with-pcre-jit \  
\--with-ipv6 \  
\--with-http_gzip_static_module \  
\--with-stream \  
\--with-http_realip_module \  
\--with-stream_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_postgres_module \  
\--with-http_iconv_module \  
\--with-openssl=/app/openssl-1.0.2j \  
\--http-client-body-temp-path=/usr/local/openresty/nginx/run/client_body_temp
\  
\--http-proxy-temp-path=/usr/local/openresty/nginx/run/proxy_temp \  
\--http-fastcgi-temp-path=/usr/local/openresty/nginx/run/fastcgi_temp \  
\--http-uwsgi-temp-path=/usr/local/openresty/nginx/run/uwsgi_temp \  
\--http-scgi-temp-path=/usr/local/openresty/nginx/run/scgi_temp \  
\--add-module=/app/ngx_http_dyups_module \  
\--add-module=/app/stream-lua-nginx-module \  
&& make && make install  
  
# luarocks  
RUN cd /app \  
&& curl --progress --remote-name
http://luarocks.github.io/luarocks/releases/luarocks-2.4.1.tar.gz \  
&& tar zxvf luarocks-2.4.1.tar.gz \  
&& cd luarocks-2.4.1 \  
&& ./configure \  
\--lua-suffix=jit \  
\--with-lua=/usr/local/openresty/luajit \  
\--with-lua-include=/usr/local/openresty/luajit/include/luajit-2.1 \  
&& make build && make install  
  
# dnsmasq  
RUN cd /app \  
&& curl --progress --remote-name
http://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.76.tar.gz \  
&& tar zxvf dnsmasq-2.76.tar.gz \  
&& cd dnsmasq-2.76 \  
&& make install  
  
# serf  
RUN cd /app \  
&& curl --progress --remote-name
https://releases.hashicorp.com/serf/0.8.0/serf_0.8.0_linux_amd64.zip \  
&& unzip serf_0.8.0_linux_amd64.zip \  
&& mv serf /usr/local/openresty/bin/  
  
RUN luarocks install luasocket 2.0.2  
RUN luarocks install
https://raw.githubusercontent.com/Mashape/kong/master/kong-0.9.5-0.rockspec  
  
COPY config/kong/ /usr/local/bin/  
COPY config/dnsmasq/dnsmasq.conf /etc/dnsmasq.conf  
COPY config/postgres /tmp/  
COPY docker-entrypoint.sh /tmp/  
  
RUN rm -rf /app/*  
  
#EXPOSE 7946, 8000, 8001, 8443  
CMD ["/bin/sh", "/tmp/docker-entrypoint.sh"]  
  

