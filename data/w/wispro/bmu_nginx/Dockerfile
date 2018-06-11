FROM nginx:1.13-alpine  
  
RUN mkdir /data  
  
COPY cert.pem /data/cert.pem  
COPY cert.key /data/cert.key  
COPY nginx.conf /etc/nginx/nginx.conf  

