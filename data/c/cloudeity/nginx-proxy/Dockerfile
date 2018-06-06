FROM openresty/openresty:alpine-fat  
  
MAINTAINER Cloudeity Inc <contact@cloudeity.com>  
  
# Install packages  
RUN apk add --update ca-certificates bash git openssl openssl-dev && rm -rf
/var/cache/apk/*  
  
# Install Lua modules  
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-http  
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-auto-ssl  
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-session  
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-jwt  
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-hmac  
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-openidc  
  
# Make paths and set permissions  
RUN mkdir /etc/resty-auto-ssl && chown nobody /etc/resty-auto-ssl  
  
# Generate backup key  
RUN openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 \  
-subj '/CN=sni-support-required-for-valid-ssl' \  
-keyout /etc/ssl/resty-auto-ssl-fallback.key \  
-out /etc/ssl/resty-auto-ssl-fallback.crt  
  
COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf.tmpl  
COPY 502.html /usr/local/openresty/nginx/html/502.html  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
# Persist certificates  
VOLUME ["/etc/resty-auto-ssl"]  
  
ENTRYPOINT ["/entrypoint.sh"]  

