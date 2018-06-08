FROM openresty/openresty:1.13.6.1-2-alpine-fat  
RUN apk add -U openssl-dev git ca-certificates  
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-openidc 1.5.4  
ENTRYPOINT ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]  

