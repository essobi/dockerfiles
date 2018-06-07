FROM nginx:1.9.15-alpine  
  
COPY docker.nginx.conf /etc/nginx/nginx.conf  
COPY docker.vh.conf /etc/nginx/vh.conf  
  
ENV GROUP_ID=110  
ENV NGINX_USER_ID=100  
  
RUN deluser nginx && \  
addgroup -S nginx -g $GROUP_ID && \  
  
# user nginx must be a system user  
adduser -S -D -H -s /sbin/nologin -g nginx -G nginx -u $NGINX_USER_ID nginx  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

