# sudo docker build -f Dockerfile-minimal -t nginx-lua-min .  
# sudo docker build -f Dockerfile-debian -t nginx-lua-min-debian .  
#  
# sudo docker-compose run --rm test  
FROM debian:wheezy  
  
MAINTAINER saksmlz <saksmlz@gmail.com>  
  
ENV NGINX_VERSION 1.5.12  
ENV NGINX_DEVEL_KIT_VERSION 0.2.19  
ENV LUA_NGINX_MODULE_VERSION 0.9.16  
ENV TEST_NGINX_VERSION 0.24  
ENV LUAJIT_VERSION 2.0.4  
  
ENV LUAJIT_LIB /usr/local/lib/  
ENV LUAJIT_INC /LuaJIT-${LUAJIT_VERSION}/src/  
  
RUN echo 'deb-src http://httpredir.debian.org/debian wheezy main' >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get build-dep -y nginx && \  
apt-get install -y wget libtest-longstring-perl libspiffy-perl libtest-base-
perl \  
liblist-moreutils-perl libhttp-response-encoding-perl libncurses5-dev ca-
certificates && \  
  
wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
tar xzvf nginx-${NGINX_VERSION}.tar.gz && \  
rm nginx-${NGINX_VERSION}.tar.gz && \  
#  
wget
https://github.com/simpl/ngx_devel_kit/archive/v${NGINX_DEVEL_KIT_VERSION}.tar.gz
&& \  
tar xzvf v${NGINX_DEVEL_KIT_VERSION}.tar.gz && \  
rm v${NGINX_DEVEL_KIT_VERSION}.tar.gz && \  
#  
wget https://github.com/openresty/lua-nginx-
module/archive/v${LUA_NGINX_MODULE_VERSION}.tar.gz && \  
tar xzvf v${LUA_NGINX_MODULE_VERSION}.tar.gz && \  
rm v${LUA_NGINX_MODULE_VERSION}.tar.gz && \  
  
wget http://search.cpan.org/CPAN/authors/id/A/AG/AGENT/Test-
Nginx-${TEST_NGINX_VERSION}.tar.gz && \  
tar xzvf Test-Nginx-${TEST_NGINX_VERSION}.tar.gz && \  
rm Test-Nginx-${TEST_NGINX_VERSION}.tar.gz && \  
  
wget http://luajit.org/download/LuaJIT-${LUAJIT_VERSION}.tar.gz && \  
tar xzvf LuaJIT-${LUAJIT_VERSION}.tar.gz && \  
rm LuaJIT-${LUAJIT_VERSION}.tar.gz && \  
cd /LuaJIT-${LUAJIT_VERSION} && \  
make -j6 && \  
make install && \  
ln -s /usr/local/lib/libluajit-5.1.so.${LUAJIT_VERSION}
/usr/local/lib/libluajit.so && \  
  
apt-get -y purge wget bzip2 manpages po-debconf man-db geoip-bin libgeoip-dev
libgeoip1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD /entrypoint /entrypoint  
  
ENTRYPOINT /entrypoint  

