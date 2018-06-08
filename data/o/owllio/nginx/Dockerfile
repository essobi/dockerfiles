FROM owllio/baseimage  
  
RUN cd /tmp && wget http://nginx.org/download/nginx-1.7.7.tar.gz && tar -xzvf
nginx-1.7.7.tar.gz  
RUN cd /tmp/nginx-1.7.7 && ./configure \  
--prefix=/usr/share/nginx \  
--sbin-path=/usr/sbin/nginx \  
--conf-path=/etc/nginx/nginx.conf \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/lock/nginx.lock \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/access.log \  
--user=www-data \  
--group=www-data \  
--without-mail_pop3_module \  
--without-mail_imap_module \  
--without-mail_smtp_module \  
--without-http_fastcgi_module \  
--without-http_uwsgi_module \  
--without-http_scgi_module \  
--without-http_memcached_module \  
--with-ipv6 \  
--with-http_ssl_module \  
--with-http_stub_status_module \  
--with-http_gzip_static_module  
RUN cd /tmp/nginx-1.7.7 && make && make install  
  
  
# Remove the source files.. we don't need them anymore  
RUN rm -rf /tmp/nginx-1.7.7  
  
EXPOSE 80  
EXPOSE 443  
  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx"]  
  
WORKDIR /etc/nginx  
  
CMD /usr/sbin/nginx -g "daemon off;"  

