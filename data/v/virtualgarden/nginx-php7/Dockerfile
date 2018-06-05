# PHP 7 docker environement with alpine, nginx, php7  
# Alpine base  
FROM alpine:latest  
MAINTAINER Olivier Blunt <contact@gmail.com>  
  
# Application file directory  
ARG APP_DIR=/app  
  
# Document root in the APP_DIR  
ARG STATIC_DIR  
  
# Service user  
ARG USER=app  
  
# Enable https (possible values: on, off, or force. Default off)  
# Certificates must be stored as /etc/nginx/ssl/fullchain.pem and
/etc/nginx/ssl/privkey.pem  
ARG HTTPS=off  
  
# Allowed domains, required for https (space separated)  
ARG DOMAINS  
  
# Server RAM (in MB) (default calculated at build time)  
ARG RAM  
  
# Maximum upload size (in MB)  
ARG UPLOAD_MAX=10  
# Install  
COPY install /install  
RUN /bin/sh /install/install.sh  
  
# App files  
WORKDIR /app  
COPY index.php /app/index.php  
  
# Setup  
COPY setup /setup  
RUN /bin/sh /setup/setup.sh  
  
# Run  
EXPOSE 80  
CMD ["runsvdir", "/etc/service"]

