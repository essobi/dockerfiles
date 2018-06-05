FROM augustash/alpine-base-s6:1.0.2  
# environment  
ENV NGINX_DH_SIZE 2048  
ENV NGINX_SSL_SUBJECT /C=US/ST=MN/L=Minneapolis/O=August Ash/OU=Local
Server/CN=*  
  
# packages & configure  
RUN apk-install nginx && \  
mkdir -p \  
/var/lib/nginx \  
/etc/nginx/conf.d \  
/etc/nginx/hosts.d \  
/etc/nginx/keys && \  
rm -rf /etc/nginx/conf.d/* /etc/nginx/nginx.conf /var/lib/nginx/run && \  
apk-cleanup  
  
# RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
# ln -sf /dev/stderr /var/log/nginx/error.log  
  
# copy root filesystem  
COPY rootfs /  
# external  
EXPOSE 80 443  
WORKDIR /src  
  
# run s6 supervisor  
ENTRYPOINT ["/init"]  

