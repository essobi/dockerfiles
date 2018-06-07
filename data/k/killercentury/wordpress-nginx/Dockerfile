FROM wordpress:fpm  
  
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]

