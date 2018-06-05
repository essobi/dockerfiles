FROM learninglayers/base  
MAINTAINER Yordan Manolov <manolov@dbis.rwth-aachen.de>  
  
# Install build dependencies  
RUN apt-get install -qqy \  
wget \  
tar \  
libreadline-dev \  
libncurses5-dev \  
libpcre3-dev \  
libssl-dev \  
perl \  
make \  
ca-certificates  
  
# Set build dir  
WORKDIR /opt  
ENV OPENRESTY_VERSION 1.9.3.1  
RUN wget
http://openresty.org/download/ngx_openresty-${OPENRESTY_VERSION}.tar.gz \  
&& readonly CPUTHR=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& tar xvzf ngx_openresty-${OPENRESTY_VERSION}.tar.gz \  
&& cd ngx_openresty-* \  
&& ./configure --with-pcre-jit --with-ipv6 -j${CPUTHR}\  
&& make -j${CPUTHR} \  
&& make install  
  
WORKDIR /usr/local/openresty  
  
# Make sure the docker log collector has access to the openresty logs  
RUN ln -sf /dev/stdout /usr/local/openresty/nginx/logs/access.log  
RUN ln -sf /dev/stderr /usr/local/openresty/nginx/logs/error.log  
  
EXPOSE 80 443  
CMD /usr/local/openresty/nginx/sbin/nginx -c
/usr/local/openresty/conf/nginx.conf #-g daemon off  

