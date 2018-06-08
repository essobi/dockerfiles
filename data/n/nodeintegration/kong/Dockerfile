FROM debian:jessie  
MAINTAINER Brendan Beveridge <brendan@nodeintegration.com.au>  
  
ENV KONG_VERSION 0.10.2  
RUN apt-get update -q && \  
apt-get install -yqq wget openssl libpcre3 procps perl patch && \  
rm -rf /var/lib/apt/lists/*  
RUN wget
https://github.com/Mashape/kong/releases/download/${KONG_VERSION}/kong-${KONG_VERSION}.jessie_all.deb
-O /tmp/kong-${KONG_VERSION}.jessie_all.deb && \  
dpkg -i /tmp/kong-${KONG_VERSION}.jessie_all.deb && \  
rm /tmp/kong-${KONG_VERSION}.jessie_all.deb && \  
wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 && \  
chmod +x /usr/local/bin/dumb-init  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
RUN mkdir -p /usr/local/kong/logs \  
&& ln -sf /tmp/logpipe /usr/local/kong/logs/access.log \  
&& ln -sf /tmp/logpipe /usr/local/kong/logs/admin_access.log \  
&& ln -sf /tmp/logpipe /usr/local/kong/logs/admin_error.log \  
&& ln -sf /tmp/logpipe /usr/local/kong/logs/serf.log \  
&& ln -sf /tmp/logpipe /usr/local/kong/logs/error.log  
  
RUN touch /etc/kong/kong.admin.htpasswd  
COPY ./conf_loader.lua.patch /tmp/  
COPY ./kong_defaults.lua.patch /tmp/  
COPY ./nginx_kong.lua.patch /tmp/  
COPY ./nginx_kong.lua-acl.patch /tmp/  
  
RUN cd /usr/local/share/lua/5.1/kong && \  
patch -p0 < /tmp/conf_loader.lua.patch && \  
patch -p0 < /tmp/kong_defaults.lua.patch && \  
patch -p0 < /tmp/nginx_kong.lua.patch && \  
patch -p0 < /tmp/nginx_kong.lua-acl.patch  
  
EXPOSE 8000 8443 8001 7946  
CMD ["kong", "start"]  

