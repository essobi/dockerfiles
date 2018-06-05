# Pull base image.  
FROM bradegler/base-ubuntu  
  
# Install Nginx.  
RUN \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
# Configure supervisord to run nginx  
RUN echo "[program:nginx]" > /etc/supervisor/conf.d/nginx.conf && \  
echo "command = /usr/sbin/nginx" >> /etc/supervisor/conf.d/nginx.conf && \  
echo "user = root" >> /etc/supervisor/conf.d/nginx.conf && \  
echo "autostart = true" >> /etc/supervisor/conf.d/nginx.conf  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/usr/share/nginx/html"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command.  
CMD ["/usr/bin/supervisord"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443

