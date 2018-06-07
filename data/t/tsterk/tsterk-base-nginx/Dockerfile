FROM tsterk/tsterk-base-alpine:latest  
MAINTAINER Tim Sterk <tim.sterk@gmail.com>  
LABEL version="0.2"  
  
# Create missing directory's:  
RUN mkdir -pv /run/nginx && \  
# Install nginx:  
apk add \--no-cache nginx && \  
# Configure logging to stdout & stderr  
ln -sfn /dev/stdout /var/log/nginx/access.log && \  
ln -sfn /dev/stderr /var/log/nginx/error.log && \  
# Create default DocumentRoot  
mkdir -pv /var/www/html && \  
chown -R www-data:www-data /var/www/html && \  
chmod 2775 /var/www/html  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY index.html /var/www/html/index.html  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

