FROM ubuntu:14.04  
RUN apt-get update  
  
# Install Nginx and Apache utils to generate the Basic HTTP Auth password file  
RUN apt-get -y install \  
nginx \  
apache2-utils  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
COPY doxy /etc/nginx/sites-available/doxy  
RUN ln -s /etc/nginx/sites-available/doxy /etc/nginx/sites-enabled/doxy  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Copy the init script  
COPY run-doxy /var/run/  
  
# Create a volume to place SSL certificate and key  
VOLUME ["/ssl"]  
  
EXPOSE 443  
ENTRYPOINT ["/var/run/run-doxy"]

