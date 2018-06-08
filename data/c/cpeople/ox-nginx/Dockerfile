FROM nginx:1-alpine  
  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories && \  
apk add \--no-cache \--virtual .build-deps shadow && \  
usermod -u 1000 nginx && \  
mkdir -p /var/www && \  
chown nginx /var/www && \  
apk del .build-deps && \  
rm -rf /var/cache/apk/*  
  
ADD nginx.conf /etc/nginx/  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  

