FROM ubuntu:14.04  
MAINTAINER Gert Van Gool <gert@vangool.mx>  
  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Fix locales  
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
  
# Enable universe & src repo's  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main restricted
universe\ndeb-src http://archive.ubuntu.com/ubuntu trusty main restricted
universe\ndeb http://archive.ubuntu.com/ubuntu trusty-updates main restricted
universe\ndeb-src http://archive.ubuntu.com/ubuntu trusty-updates main
restricted universe\n" > /etc/apt/sources.list  
  
# Install build tools for nginx  
RUN apt-get update && \  
apt-get install build-essential wget -y && \  
apt-get build-dep nginx-full -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV NGINX_VERSION 1.6.2  
  
# Nginx  
RUN cd /usr/src/ && wget
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && tar xf
nginx-${NGINX_VERSION}.tar.gz && rm -f nginx-${NGINX_VERSION}.tar.gz  
# Extra modules  
ADD modules /usr/src/nginx-modules/  
ENV MODULESDIR /usr/src/nginx-modules  
# Compiling nginx  
RUN cd /usr/src/nginx-${NGINX_VERSION} && ./configure \  
--prefix=/etc/nginx \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--sbin-path=/usr/sbin \  
--http-client-body-temp-path=/var/lib/nginx/body \  
--http-fastcgi-temp-path=/var/lib/nginx/fastcgi \  
--http-log-path=/var/log/nginx/access.log \  
--http-proxy-temp-path=/var/lib/nginx/proxy \  
--http-scgi-temp-path=/var/lib/nginx/scgi \  
--http-uwsgi-temp-path=/var/lib/nginx/uwsgi \  
--lock-path=/var/lock/nginx.lock \  
--pid-path=/var/run/nginx.pid \  
--with-http_addition_module \  
--with-http_dav_module \  
--with-http_geoip_module \  
--with-http_gzip_static_module \  
--with-http_image_filter_module \  
--with-http_realip_module \  
--with-http_stub_status_module \  
--with-http_ssl_module \  
--with-http_sub_module \  
--with-http_xslt_module \  
--with-ipv6 \  
--with-debug \  
--with-sha1=/usr/include/openssl \  
--with-md5=/usr/include/openssl \  
--add-module=${MODULESDIR}/nginx-auth-pam \  
--add-module=${MODULESDIR}/nginx-cache-purge \  
--add-module=${MODULESDIR}/nginx-echo \  
--add-module=${MODULESDIR}/nginx-upstream-fair  
# Other possible modules  
#--add-module=${MODULESDIR}/chunkin-nginx-module  
#--add-module=${MODULESDIR}/headers-more-nginx-module  
#--add-module=${MODULESDIR}/naxsi/naxsi_src  
#--add-module=${MODULESDIR}/nginx-dav-ext-module  
#--add-module=${MODULESDIR}/nginx-development-kit  
#--add-module=${MODULESDIR}/nginx-http-push  
#--add-module=${MODULESDIR}/nginx-lua  
#--add-module=${MODULESDIR}/nginx-upload-module  
#--add-module=${MODULESDIR}/nginx-upload-progress  
  
RUN cd /usr/src/nginx-${NGINX_VERSION} && make && make install  
# Create the /var/lib/nginx directory (for temp paths)  
RUN mkdir -p /var/lib/nginx  
  
ADD nginx /etc/nginx/  
  
EXPOSE 80 443  
CMD ["nginx"]  

