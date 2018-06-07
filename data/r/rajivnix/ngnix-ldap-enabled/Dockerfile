FROM debian:jessie  
  
MAINTAINER RAJEEV REDDY <rajiv.jaggavarapu@paxcel.net>  
  
#ENV NGINX_VERSION release-1.7.10  
  
RUN apt-get update \  
&& apt-get install -y \  
ca-certificates \  
git \  
gcc \  
make \  
libpcre3-dev \  
zlib1g-dev \  
libldap2-dev \  
wget \  
libssl-dev \  
\--fix-missing  
  
# See http://wiki.nginx.org/InstallOptions  
RUN cd ~ \  
&& git clone https://github.com/kvspb/nginx-auth-ldap.git \  
&& pwd \  
&& wget http://nginx.org/download/nginx-1.7.7.tar.gz \  
&& tar -xvzf nginx-1.7.7.tar.gz \  
&& cd nginx-1.7.7 \  
&& chmod +x configure \  
&& ./configure \  
\--user=root \  
\--group=root \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--with-http_gzip_static_module \  
\--with-http_stub_status_module \  
\--with-http_ssl_module \  
\--with-pcre \  
\--with-file-aio \  
\--with-http_realip_module \  
\--add-module=/root/nginx-auth-ldap/ \  
\--with-ipv6 --with-debug \  
&& make \  
&& make install  
  
RUN wget https://raw.githubusercontent.com/calvinbui/nginx-init-
ubuntu/master/nginx -O /etc/init.d/nginx \  
&& chmod +x /etc/init.d/nginx \  
&& update-rc.d -f nginx defaults \  
&& service nginx start  
  
EXPOSE 80 443  
  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]  

