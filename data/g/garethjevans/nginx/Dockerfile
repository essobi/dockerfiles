FROM ubuntu:vivid  
  
MAINTAINER Cai Cooper <caicooper82@gmail.com>  
  
WORKDIR /tmp  
  
RUN apt-get update  
  
# Install prerequisites for Nginx compile  
RUN apt-get install -y wget \  
tar \  
gcc \  
build-essential \  
make \  
libldap2-dev \  
libssl-dev \  
libpcre3-dev \  
git  
  
# Download Nginx and Nginx modules source  
RUN wget http://nginx.org/download/nginx-1.9.4.tar.gz -O nginx.tar.gz && \  
mkdir /tmp/nginx && \  
tar -xzvf nginx.tar.gz -C /tmp/nginx --strip-components=1 &&\  
git clone https://github.com/kvspb/nginx-auth-ldap nginx/nginx-auth-ldap  
  
# Build Nginx  
WORKDIR /tmp/nginx  
RUN ./configure \  
\--user=root \  
\--with-debug \  
\--prefix=/usr/share/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--pid-path=/run/nginx.pid \  
\--lock-path=/run/lock/subsys/nginx \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--with-http_dav_module \  
\--add-module=nginx-auth-ldap && \  
make && \  
make install  
  
# Cleanup after Nginx build  
RUN apt-get remove -y wget \  
gcc \  
build-essential \  
make \  
libldap2-dev \  
libssl-dev \  
libpcre3-dev \  
git && \  
rm -rf /tmp/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# DATA VOLUMES  
VOLUME ["/data/nginx/www"]  
VOLUME ["/data/nginx/config"]  
  
EXPOSE 80 443  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]  

