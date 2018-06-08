FROM openresty/openresty:latest-xenial  
  
RUN apt-get update \  
&& apt-get install -y libpcre3 libpcre3-dev \  
&& /usr/local/openresty/luajit/bin/luarocks install lua-resty-auto-ssl \  
&& /usr/local/openresty/luajit/bin/luarocks install lrexlib-PCRE \  
&& curl -L https://raw.githubusercontent.com/murara/mobile-
detect.lua/master/mobile-detect.lua -o /usr/local/openresty/lualib/mobile-
detect.lua \  
&& openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 -subj '/CN=sni-
support-required-for-valid-ssl' -keyout /etc/ssl/resty-auto-ssl-fallback.key
-out /etc/ssl/resty-auto-ssl-fallback.crt  
  
COPY nginx-cache-purge /nginx-cache-purge  
COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf  

