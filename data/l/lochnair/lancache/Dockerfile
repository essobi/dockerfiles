FROM nginx:mainline-alpine  
  
RUN apk add \  
\--no-cache \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/community \  
\--update \  
shadow \  
su-exec  
  
RUN mkdir -p /var/lancache/installs && \  
mkdir -p /var/lancache/logs && \  
mkdir -p /var/lancache/other && \  
mkdir -p /var/lancache/tmp  
  
VOLUME /var/lancache  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
ADD lancache/nginx.conf /etc/nginx/nginx.conf  
ADD lancache/lancache/ /etc/nginx/lancache  
ADD lancache/sites/ /etc/nginx/sites/  
  
RUN sed -i 's|user www-data www-data;|user nginx nginx;|g'
/etc/nginx/nginx.conf  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

