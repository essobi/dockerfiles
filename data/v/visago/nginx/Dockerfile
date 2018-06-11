FROM debian:jessie  
#  
# ORIGINAL MAINTAINER Henrik Sachse <t3x7m3@posteo.de>  
#  
# Personalized version by Elvin Tan <elvin@elvin.net>  
#  
  
ENV NGINX_VERSION release-1.11.13  
  
# Use jessie-backports for openssl >= 1.0.2  
# This is required by nginx-auth-ldap when ssl_check_cert is turned on.  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& echo 'deb http://ftp.debian.org/debian/ jessie-backports main' >
/etc/apt/sources.list.d/backports.list \  
&& apt-get update \  
&& apt-get install -t jessie-backports -y \  
ca-certificates \  
git \  
gcc \  
make \  
libpcre3-dev \  
zlib1g-dev \  
libldap2-dev \  
libssl-dev \  
wget  
  
# See http://wiki.nginx.org/InstallOptions  
RUN mkdir /var/log/nginx \  
&& mkdir /etc/nginx \  
&& cd ~ \  
&& git clone https://github.com/kvspb/nginx-auth-ldap.git \  
&& git clone https://github.com/nginx/nginx.git \  
&& cd ~/nginx \  
&& git checkout tags/${NGINX_VERSION} \  
&& ./auto/configure \  
\--add-module=/root/nginx-auth-ldap \  
\--with-http_ssl_module \  
\--with-debug \  
\--conf-path=/etc/nginx/nginx.conf \  
\--sbin-path=/usr/sbin/nginx \  
\--pid-path=/var/log/nginx/nginx.pid \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-debug \  
\--with-file-aio \  
\--with-threads \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_v2_module \  
\--with-http_auth_request_module \  
&& make install \  
&& cd .. \  
&& rm -rf nginx-auth-ldap \  
&& rm -rf nginx  
  
EXPOSE 80  
  
# Disabled. Please always log to a file via nginx.conf !  
# forward request and error logs to docker log collector  
#RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
# && ln -sf /dev/stderr /var/log/nginx/error.log  
  
STOPSIGNAL SIGTERM  
CMD ["nginx", "-g", "daemon off;"]  
  
#  
#docker run --name nginx -p 80:80 \  
# -v /home/nginx.conf:/etc/nginx/nginx.conf:ro \  
# -v /home/www:/home/www \  
# -v /var/log/nginx:/var/log/nginx \  
# -d visago/nginx  
#

