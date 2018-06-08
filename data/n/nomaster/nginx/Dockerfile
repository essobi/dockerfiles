FROM openresty/openresty:alpine-fat  
  
LABEL maintainer="Mic Szillat <mic@nomaster.cc>"  
  
RUN apk add --update-cache openssl bash \  
&& /usr/local/openresty/luajit/bin/luarocks install lua-resty-http \  
&& /usr/local/openresty/luajit/bin/luarocks install lua-resty-auto-ssl \  
&& openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 -subj '/CN=sni-
support-required-for-valid-ssl' -keyout /etc/ssl/resty-auto-ssl-fallback.key
-out /etc/ssl/resty-auto-ssl-fallback.crt \  
&& mkdir -p /etc/resty-auto-ssl/storage \  
&& chown -R nobody:nobody /etc/resty-auto-ssl/storage  
  
ADD nginx.conf /usr/local/openresty/nginx/conf/nginx.conf  
ADD ssl.conf /usr/local/openresty/nginx/conf/ssl.conf  
  
EXPOSE 80  
EXPOSE 443  
VOLUME /etc/resty-auto-ssl/storage  
  
ENTRYPOINT ["/usr/local/openresty/nginx/sbin/nginx"]  

