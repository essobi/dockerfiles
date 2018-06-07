FROM debian:wheezy  
  
ENV OPENRESTY_VERSION 1.9.7.4  
ENV PATH /usr/local/openresty/nginx/sbin:$PATH  
  
RUN BUILD_PACKAGES="libreadline-dev libncurses5-dev libpcre3-dev libssl-dev
perl make build-essential wget libgeoip-dev"; \  
apt-get update && apt-get install -y $BUILD_PACKAGES ca-certificates tar
libpcre3 \  
&& mkdir /build_tmp && cd /build_tmp \  
&& wget http://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz \  
&& tar xf openresty-${OPENRESTY_VERSION}.tar.gz \  
&& cd openresty-${OPENRESTY_VERSION} && ./configure \  
\--with-pcre-jit \  
\--with-ipv6 \  
\--with-http_geoip_module \  
\--with-http_gzip_static_module \  
\--with-http_realip_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
&& make && make install \  
&& apt-get remove --purge -y $BUILD_PACKAGES \  
&& apt-get install -y libgeoip1 \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /build_tmp  
  
VOLUME /nginx  
  
WORKDIR /nginx  
  
CMD ["nginx", "-p", "/nginx/", "-c", "conf/nginx.conf"]  

