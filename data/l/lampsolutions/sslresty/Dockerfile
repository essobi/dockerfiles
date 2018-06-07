FROM phusion/baseimage:0.9.22  
ENV LUAROCKS_VERSION 2.0.13  
ENV LUA_RESTY_AUTO_SSL 0.12.0  
RUN curl -s https://openresty.org/package/pubkey.gpg | apt-key add - && \  
echo "deb http://openresty.org/package/ubuntu xenial main" | tee -a
/etc/apt/sources.list  
RUN apt-get update -y && \  
apt-get dist-upgrade -y && \  
apt-get install openresty make unzip gcc -y  
RUN cd /tmp && \  
curl -sL http://luarocks.org/releases/luarocks-${LUAROCKS_VERSION}.tar.gz >
luarocks-${LUAROCKS_VERSION}.tar.gz && \  
tar -xzf luarocks-${LUAROCKS_VERSION}.tar.gz  
  
RUN cd /tmp/luarocks-${LUAROCKS_VERSION} && \  
./configure --prefix=/usr/local/openresty/luajit/ \  
\--with-lua=/usr/local/openresty/luajit/ \  
\--lua-suffix=jit \  
\--with-lua-include=/usr/local/openresty/luajit/include/luajit-2.1/ && \  
make && make install  
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-auto-ssl
${LUA_RESTY_AUTO_SSL} && \  
apt-get purge gcc make -y && \  
apt-get autoremove -y  
  
# Clean up image  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf  
  
RUN mkdir /etc/service/nginx  
ADD nginx.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
  
EXPOSE 8099 443  
VOLUME /etc/resty-auto-ssl/  
  
CMD ["/sbin/my_init"]

