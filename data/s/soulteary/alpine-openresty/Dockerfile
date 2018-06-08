FROM soulteary/alpine-base:3.4  
MAINTAINER soulteary <soulteary@gmail.com>  
  
# https://github.com/quiklyn/docker-openresty  
# https://openresty.org/#Download  
ENV OPENRESTY_VERSION 1.11.2.1  
# https://github.com/keplerproject/luarocks/wiki/Release-history  
ENV LUAROCKS_VERSION 2.4.0  
ENV OPENRESTY_PREFIX /usr/local/openresty  
ENV NGINX_PREFIX ${OPENRESTY_PREFIX}/nginx  
ENV LUAJIT_PREFIX ${OPENRESTY_PREFIX}/luajit  
  
ENV PATH
"${NGINX_PREFIX}/sbin:${LUAJIT_PREFIX}/bin:${OPENRESTY_PREFIX}/bin:${PATH}"  
COPY ./docker-build.sh /  
RUN ./docker-build.sh  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off; error_log logs/error.log info;"]  

