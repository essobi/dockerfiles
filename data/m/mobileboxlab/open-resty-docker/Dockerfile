FROM openresty/openresty:xenial  
  
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-jwt  
  
CMD ["/usr/local/openresty/bin/openresty", "-c", "/nginx.conf"]

