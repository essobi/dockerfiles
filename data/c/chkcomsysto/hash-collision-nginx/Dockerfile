#  
# Nginx Dockerfile  
#  
# based on:  
# https://github.com/dockerfile/nginx  
#  
# Pull base image.  
FROM dockerfile/ubuntu  
  
# Install Nginx.  
RUN \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/* && \  
chown -R www-data:www-data /var/lib/nginx  
  
# Add nginx config and data  
ADD nginx.conf /etc/nginx/nginx.conf  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command.  
# insert address and port of routing service in nginx.conf start nginx  
CMD \  
sed -i s/__ROUTING_ADDR__/$ROUTING_PORT_5555_TCP_ADDR/g /etc/nginx/nginx.conf
&& \  
sed -i s/__ROUTER_PORT__/$ROUTING_PORT_5555_TCP_PORT/g /etc/nginx/nginx.conf
&& \  
nginx  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443

