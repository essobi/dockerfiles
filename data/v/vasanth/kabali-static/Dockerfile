FROM nginx:mainline-alpine  
  
COPY assets.tar.gz /tmp/  
  
RUN mkdir -p /usr/share/nginx/html \  
&& tar -zxf /tmp/assets.tar.gz -C /usr/share/nginx/html \  
&& rm -f /tmp/assets.tar.gz  

