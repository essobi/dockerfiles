FROM openresty/openresty:alpine-fat  
  
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-http  
  
COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf  
COPY entrypoint.sh /entrypoint-nginx.sh  
  
ENTRYPOINT ["/entrypoint-nginx.sh"]  
CMD ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]  

