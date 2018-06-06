FROM thinkbright/nginx-node:latest  
MAINTAINER "Jacco Meijer" <jacco@thinkbright.nl>  
  
# Npm and composer complain about this if we leave it out (either this, or run
as root)  
RUN mkdir -p /var/www  
RUN chown -R www-data /var/www  
  
# Copy usr-local-bin into container  
COPY ./usr-local-bin/ /usr/local/bin/  
  
# Copy nginx config  
COPY ./config-nginx/ /etc/nginx/  
  
RUN mkdir -p /build  
WORKDIR /build  
RUN chown -R www-data /build  
USER www-data  
  
# Download Craftcms  
RUN /usr/local/bin/craftcms-install.sh  
RUN /usr/local/bin/craftcms-plugins-install.sh  
RUN /usr/local/bin/set-permissions.sh  
  
# Display version  
RUN cat /build/craft/app/Info.php  

