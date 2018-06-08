FROM centos:centos7  
  
MAINTAINER Nitra  
  
# import GPG signing key  
ADD etc/pki/rpm-gpg/RPM-GPG-KEY-nginx /etc/pki/rpm-gpg/RPM-GPG-KEY-nginx  
RUN rpm \--import /etc/pki/rpm-gpg/RPM-GPG-KEY-nginx  
# install package  
ADD etc/yum.repos.d/nginx-mainline.repo /etc/yum.repos.d/nginx-mainline.repo  
RUN yum install -y nginx wget mc tar openssl-devel pcre-devel gcc gcc-c++
kernel-devel make vim  
RUN mkdir /home/nginx_temp && cd /home/nginx_temp && wget
http://nginx.org/download/nginx-1.8.0.tar.gz && \  
wget http://labs.frickle.com/files/ngx_cache_purge-2.3.tar.gz && tar -xvf
nginx-1.8.0.tar.gz && tar -xvf ngx_cache_purge-2.3.tar.gz && cd
/home/nginx_temp/nginx-1.8.0 && \  
./configure \--prefix=/etc/nginx \--sbin-path=/usr/sbin/nginx \--conf-
path=/etc/nginx/nginx.conf \--error-log-path=/var/log/nginx/error.log \--http-
log-path=/var/log/nginx/access.log \--pid-path=/var/run/nginx.pid \--lock-
path=/var/run/nginx.lock \--http-client-body-temp-
path=/var/cache/nginx/client_temp \--http-proxy-temp-
path=/var/cache/nginx/proxy_temp \--http-fastcgi-temp-
path=/var/cache/nginx/fastcgi_temp \--user=nginx \--group=nginx \--without-
http_scgi_module \--without-http_uwsgi_module \--with-http_gzip_static_module
\--with-http_stub_status_module \--with-pcre-jit \--with-http_ssl_module
\--with-http_gunzip_module \--with-ipv6 \--add-
module=/home/nginx_temp/ngx_cache_purge-2.3 && \  
make && make install  
  
ADD vhost.conf /etc/nginx/conf.d/default.conf  
ADD start.sh /start.sh  
# forward request logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN /bin/sed -i "29i\gzip on;" /etc/nginx/nginx.conf && \  
/bin/sed -i "30i\gzip_disable "msie6";" /etc/nginx/nginx.conf && \  
/bin/sed -i "31i\gzip_vary on;" /etc/nginx/nginx.conf && \  
/bin/sed -i "32i\gzip_proxied any;" /etc/nginx/nginx.conf && \  
/bin/sed -i "33i\gzip_comp_level 6;" /etc/nginx/nginx.conf && \  
/bin/sed -i "34i\gzip_buffers 16 8k;" /etc/nginx/nginx.conf && \  
/bin/sed -i "35i\gzip_types text/plain text/css application/json
application/x-javascript text/xml application/xml application/xml+rss
text/javascript;" /etc/nginx/nginx.conf  
### Add autostart script  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
# Endpoint  
CMD ["/start.sh"]  
  

