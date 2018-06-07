FROM haproxy:1.7  
  
ENV SYSLOG_SOCKET /dev/log  
COPY bin/syslog-init /usr/local/bin/  
  
######################  
# Lua  
######################  
  
ENV WITH_LUA /usr  
ENV LUA_LIB /usr/lib/lua  
ENV LUA_INCLUDE /usr/include  
ENV LUAROCKS_VERSION 2.4.2  
ENV LUAROCKS_INSTALL luarocks-$LUAROCKS_VERSION  
ENV TMP_LOC /tmp/luarocks  
COPY setup/install-lua.sh /tmp/install-lua.sh  
RUN /bin/sh /tmp/install-lua.sh && rm /tmp/install-lua.sh  
  
######################  
# HAProxy  
######################  
  
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
COPY backend-lookup.lua /usr/local/etc/haproxy/backend-lookup.lua  
COPY backend-lookup-config.lua /usr/local/etc/haproxy/backend-lookup-
config.lua  
  
EXPOSE 80 443 8900  
  
ENTRYPOINT ["/usr/local/bin/syslog-init", "/docker-entrypoint.sh"]  
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]  

