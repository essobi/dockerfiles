FROM library/ubuntu:xenial AS build  
  
ENV LANG=C.UTF-8  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
python-software-properties \  
software-properties-common \  
apt-utils  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get install -y \  
wget  
  
RUN wget -qO - https://openresty.org/package/pubkey.gpg | apt-key add - \  
&& add-apt-repository -y "deb http://openresty.org/package/ubuntu xenial main"
\  
&& apt-get update  
  
RUN mkdir -p /build /rootfs  
WORKDIR /build  
RUN apt-get download \  
openresty \  
openresty-openssl \  
openresty-pcre \  
openresty-zlib  
RUN find *.deb | xargs -I % dpkg-deb -x % /rootfs  
  
WORKDIR /rootfs  
RUN rm -rf \  
etc/* \  
lib/* \  
usr/share/* \  
usr/local/openresty/luajit/include \  
usr/local/openresty/luajit/lib/pkgconfig \  
usr/local/openresty/nginx/conf/*.default \  
usr/local/openresty/nginx/sbin/stap-nginx \  
usr/local/openresty/nginx/tapset && \  
mkdir -p var/log && \  
ln -s /usr/local/openresty/nginx/conf etc/nginx && \  
ln -s /usr/local/openresty/nginx/logs var/log/nginx && \  
ln -s /dev/stderr usr/local/openresty/nginx/logs/error.log && \  
ln -s /dev/stdout usr/local/openresty/nginx/logs/access.log && \  
sed -i -r \  
-e 's,^ *[#;]? *user *.*$,user root root;,g' \  
-e 's,^ *[#;]? *worker_processes *.*$,worker_processes auto;,g' \  
usr/local/openresty/nginx/conf/nginx.conf  
  
WORKDIR /  
  
FROM clover/base  
  
ENV LANG=C.UTF-8  
COPY \--from=build /rootfs /  
  
CMD ["openresty", "-g", "daemon off;"]  
  
EXPOSE 80 443  

