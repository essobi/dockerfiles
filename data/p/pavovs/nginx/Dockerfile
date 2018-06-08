FROM debian:jessie  
MAINTAINER Pavel Ovsiannikov <pavovs@yandex.ru>  
  
RUN apt-get update && apt-get install -y --no-install-recommends --no-install-
suggests \  
ca-certificates \  
curl \  
gcc \  
g++ \  
libssl-dev \  
make \  
vim \  
wget \  
&& apt-get purge nano vim-tiny \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget
ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.40.tar.gz \  
&& wget http://zlib.net/zlib-1.2.11.tar.gz \  
&& wget http://nginx.org/download/nginx-1.12.0.tar.gz  
  
RUN tar -zxf pcre-8.40.tar.gz \  
&& cd pcre-8.40 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& tar -zxf zlib-1.2.11.tar.gz \  
&& cd zlib-1.2.11 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& tar -zxf nginx-1.12.0.tar.gz \  
&& cd nginx-1.12.0 \  
&& ./configure \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/var/run/nginx.pid \  
\--user=root \  
\--group=root \  
\--with-pcre=../pcre-8.40 \  
\--with-zlib=../zlib-1.2.11 \  
\--with-stream \  
\--with-mail=dynamic \  
\--with-http_auth_request_module \  
\--with-http_v2_module \  
\--with-http_ssl_module \  
\--with-debug \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf pcre-8.40 zlib-1.2.11 nginx-1.12.0 ./*.tar.gz \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  
  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  

