FROM dockerfile/ubuntu  
MAINTAINER ServiceRocket Tools  
  
ENV NGINX_VERSION 1.7.9  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
apt-get install -y libldap2-dev libssl-dev libpcre3-dev  
  
RUN cd / \  
&& wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \  
&& tar -xvzf nginx-${NGINX_VERSION}.tar.gz \  
&& mv /nginx-${NGINX_VERSION} /nginx \  
&& cd /nginx \  
&& chmod +x configure \  
&& rm /nginx-${NGINX_VERSION}.tar.gz  
  
RUN cd / \  
&& git clone https://github.com/kvspb/nginx-auth-ldap.git  
  
RUN cd /nginx \ && ./configure --user=nginx \  
--group=nginx \  
--prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--conf-path=/etc/nginx/nginx.conf \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--with-http_gzip_static_module \  
--with-http_stub_status_module \  
--with-http_ssl_module \  
--with-pcre \  
--with-file-aio \  
--with-http_realip_module \  
--add-module=/nginx-auth-ldap/ \  
--with-ipv6 \  
--with-debug \  
--http-client-body-temp-path=/var/run/client_body_temp \  
--http-proxy-temp-path=/var/run/proxy_temp \  
--http-fastcgi-temp-path=/var/run/fastcgi_temp \  
--http-uwsgi-temp-path=/var/run/uwsgi_temp \  
--http-scgi-temp-path=/var/run/scgi_temp \  
&& make \  
&& make install \  
&& adduser nginx \  
&& adduser nginx nginx \  
&& echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
CMD ["nginx"]

