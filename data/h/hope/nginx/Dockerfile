FROM hope/base-alpine:3.5  
  
ENV \  
NGINX_VERSION=1.12.0 \  
NGINX_CONFIG=/etc/nginx/nginx.conf  
  
RUN \  
apk add \--no-cache nginx@edge && \  
  
sed -i -e "s/user nginx/user root/g" ${NGINX_CONFIG} && \  
  
# Forward logs to std output  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  
EXPOSE 443  
  
ENTRYPOINT ["nginx", "-c", "/etc/nginx/nginx.conf", "-g", "'daemon off;'"]  

