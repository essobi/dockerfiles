FROM oligertimothee/nginx_with_node:latest  
  
LABEL maintainer="Oliger Timothee" \  
version="1.1"  
  
ADD nginx/default.conf /etc/nginx/conf.d/default.conf  
  
ADD app /tmp/app  
  
RUN cd /tmp/app && nodejs build/build.js  
  
RUN mv /tmp/app/dist/* /usr/share/nginx/html  
  
RUN rm -rf /tmp/app  
  
EXPOSE 80  

