FROM sergeyzh/centos6-epel  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com  
  
ENV OPENSSL_VERSION=1.0.2h NGINX_VERSION=1.10.1  
  
ADD rpms/ /root/rpms/  
RUN rpm \--rebuilddb ; yum localinstall -y /root/rpms/*.rpm && \  
yum groupinstall -y 'Development Tools' && \  
yum install -y pcre-devel libxml2-devel libxslt-devel GeoIP-devel gd-devel
perl-ExtUtils-Embed.x86_64 nginx which  
  
# openssl  
RUN cd /usr/src && wget
https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz && \  
tar zxf openssl-$OPENSSL_VERSION.tar.gz && cd openssl-$OPENSSL_VERSION/ &&
./config && \  
make && make test && make install && mv /usr/bin/openssl /root/ && ln -s
/usr/local/ssl/bin/openssl /usr/bin/openssl  
# nginx  
RUN cd /usr/src && wget http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz
&& \  
tar zxf nginx-$NGINX_VERSION.tar.gz && mkdir nginx-$NGINX_VERSION-src-rpm &&
cd nginx-$NGINX_VERSION-src-rpm && \  
wget
http://nginx.org/packages/rhel/6/SRPMS/nginx-$NGINX_VERSION-1.el6.ngx.src.rpm
&& \  
rpm2cpio nginx-1.10.1-1.el6.ngx.src.rpm | cpio -idmv \--no-absolute-filenames
&& \  
tar zxvf njs-1c50334fbea6.tar.gz && mv njs-1c50334fbea6
/usr/src/nginx-$NGINX_VERSION/ && \  
cd /usr/src/nginx-$NGINX_VERSION/ && ./configure \--prefix=/etc/nginx \--sbin-
path=/usr/sbin/nginx \--modules-path=/usr/lib64/nginx/modules \--conf-
path=/etc/nginx/nginx.conf \--error-log-path=/var/log/nginx/error.log \--http-
log-path=/var/log/nginx/access.log \--pid-path=/var/run/nginx.pid \--lock-
path=/var/run/nginx.lock \--http-client-body-temp-
path=/var/cache/nginx/client_temp \--http-proxy-temp-
path=/var/cache/nginx/proxy_temp \--http-fastcgi-temp-
path=/var/cache/nginx/fastcgi_temp \--http-uwsgi-temp-
path=/var/cache/nginx/uwsgi_temp \--http-scgi-temp-
path=/var/cache/nginx/scgi_temp \--user=nginx \--group=nginx \--with-
http_ssl_module \--with-http_realip_module \--with-http_addition_module
\--with-http_sub_module \--with-http_dav_module \--with-http_flv_module
\--with-http_mp4_module \--with-http_gunzip_module \--with-
http_gzip_static_module \--with-http_random_index_module \--with-
http_secure_link_module \--with-http_stub_status_module \--with-
http_auth_request_module \--with-http_xslt_module=dynamic \--with-
http_image_filter_module=dynamic \--with-http_geoip_module=dynamic \--with-
http_perl_module=dynamic \--add-dynamic-module=njs-1c50334fbea6/nginx \--with-
threads \--with-stream \--with-stream_ssl_module \--with-http_slice_module
\--with-mail \--with-mail_ssl_module \--with-file-aio \--with-ipv6 \--with-
http_v2_module \--with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2
-fexceptions -fstack-protector \--param=ssp-buffer-size=4 -m64 -mtune=generic'
\--with-openssl=/usr/src/openssl-$OPENSSL_VERSION && make && make install  
  
ADD etcd-v0.4.5-linux-amd64.tar.gz /  
RUN cd /etcd-v0.4.5-linux-amd64 ; mv etcdctl /usr/bin/ ; rm -rf
/etcd-v0.4.5-linux-amd64  
  
ADD reloader.sh /  
RUN chmod a+x /reloader.sh  
  
ADD functions.sh /  
  
ADD run-services.sh /  
RUN chmod +x /run-services.sh ; mkdir -p /conf/nginx  
# Change config paths to relative  
RUN sed -i 's|/etc/nginx/||g' /etc/nginx/nginx.conf  
  
CMD /run-services.sh  
  
EXPOSE 80 443  

