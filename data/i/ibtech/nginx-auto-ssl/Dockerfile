FROM openresty/openresty:latest-xenial  
  
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-auto-ssl  
  
RUN openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 -subj '/CN=sni-
support-required-for-valid-ssl' -keyout /etc/ssl/resty-auto-ssl-fallback.key
-out /etc/ssl/resty-auto-ssl-fallback.crt \  
&& mkdir -p /tmp/letsencrypt/conf.d/ \  
&& echo 'LICENSE="https://letsencrypt.org/documents/LE-
SA-v1.2-November-15-2017.pdf"' > /tmp/letsencrypt/conf.d/config.sh  
  
ADD nginx.conf /usr/local/openresty/nginx/conf/nginx.conf  
  
ENTRYPOINT ["/usr/local/openresty/nginx/sbin/nginx", "-g", "daemon off;"]  

