FROM debian:latest  
  
ENV NGINX_VERSION="1.13.3" NGINX_BUILDER_VERSION="0.11.0"  
  
RUN apt-get -y update && \  
apt-get -y --no-install-recommends --no-install-suggests install \  
ca-certificates \  
git \  
wget \  
gcc \  
make \  
libpcre3-dev \  
libssl-dev \  
zlib1g-dev && \  
mkdir /nginx-build && cd /nginx-build  
  
RUN cd /nginx-build && \  
wget https://github.com/cubicdaiya/nginx-
build/releases/download/v${NGINX_BUILDER_VERSION}/nginx-build-linux-
amd64-${NGINX_BUILDER_VERSION}.tar.gz && \  
tar xf nginx-build-linux-amd64-${NGINX_BUILDER_VERSION}.tar.gz  
  
COPY nginx-build-modules /nginx-build/modules  
  
RUN cd /nginx-build && \  
./nginx-build -m modules -d ./work -v ${NGINX_VERSION} \  
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
--user=www-data \  
--group=www-data \  
--with-threads \  
--with-ipv6 \  
--with-http_addition_module \  
--with-http_auth_request_module \  
--with-http_dav_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_realip_module \  
--with-http_slice_module \  
--with-http_ssl_module \  
--with-http_sub_module \  
--with-http_v2_module \  
--with-cc-opt='-g -O2 -fstack-protector-strong -Wformat -Werror=format-
security -Wp,-D_FORTIFY_SOURCE=2 -fPIC' \  
--with-ld-opt='-Wl,-z,relro -Wl,-z,now -Wl,--as-needed -pie' && \  
cd ./work/nginx/${NGINX_VERSION}/nginx-${NGINX_VERSION} && \  
make install && \  
mkdir -p /etc/nginx/conf.d && \  
mkdir -p /var/cache/nginx/client_temp && \  
mkdir -p /etc/nginx/ssl && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
apt-get -y purge \  
git \  
wget \  
gcc \  
make \  
libpcre3-dev \  
libssl-dev && \  
apt-get -y autoremove && apt-get -y clean && \  
dpkg --list |grep "^rc" | cut -d " " -f 3 | xargs dpkg --purge && \  
rm -r /nginx-build && \  
rm /etc/nginx/*.default && \  
rm -r /var/lib/apt/lists/*  
  
COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf  
  
WORKDIR /etc/nginx  
  
VOLUME ["/etc/nginx/conf.d"]  
  
EXPOSE 80/TCP 443/TCP  
  
CMD ["nginx", "-g", "daemon off;"]  

