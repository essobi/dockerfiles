FROM nginx:1.13  
RUN apt-get update && apt-get install -y \  
nginx-extras  
WORKDIR /lua  
COPY prometheus.lua .  
COPY nginx.conf /etc/nginx/nginx.conf  

