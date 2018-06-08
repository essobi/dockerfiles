FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y nginx nginx-extras && \  
rm -rf /var/lib/apt/lists/*  
  
CMD nginx -g "daemon off;"  

