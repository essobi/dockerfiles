FROM meupatrocinio/docker-php7-newrelic:latest  
  
# Repository/Image Maintainer  
MAINTAINER Rafael Bernardo <rafael@meupatrocinio.com>  
  
# Reset user to root to allow software install  
USER root  
  
# Copy nginx and entry script  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY start.sh /root/start.sh  
  
# Install nginx from dotdeb (already enabled on base image)  
RUN echo "--> Installing Nginx" && \  
apk --update add --no-cache nginx && \  
echo "--> Fixing permissions" && \  
mkdir /var/run/nginx && \  
chmod +x /root/start.sh  
  
# Application directory  
WORKDIR "/var/www/app"  
  
# Expose webserver port  
EXPOSE 80  
# Define the entry point that tries to enable newrelic  
ENTRYPOINT ["/tini", "--", "/root/start.sh"]  

