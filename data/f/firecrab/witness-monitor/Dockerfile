FROM smebberson/alpine-nginx  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Add website files  
ADD witness-monitor/dist /usr/html  

