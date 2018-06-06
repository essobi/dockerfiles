FROM nginx:stable  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y netcat  
  
COPY nginx.conf /etc/nginx  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT []

