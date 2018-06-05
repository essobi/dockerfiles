# Download wordpress to /thinkbright/wordpress  
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
  
RUN mkdir /thinkbright  
RUN chown www-data /thinkbright  
  
# Install wordpress cli  
RUN wordpress-cli-install.sh  
  
# Download wordpress with bedrock stack  
RUN wordpress-download.sh  
# Display version  
RUN head /thinkbright/wordpress/CHANGELOG.md  
  
WORKDIR /thinkbright  
CMD nginx-node-entrypoint.sh  

