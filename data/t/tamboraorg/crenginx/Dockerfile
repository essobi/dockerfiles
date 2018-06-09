#  
# Nginx Dockerfile  
#  
# https://github.com/tamboraorg/docker/crenginx  
#  
# Pull base image.  
FROM tamboraorg/creubuntu:2010.0  
# Install Nginx.  
RUN \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
sed -i 's/worker_processes 1/worker_processes auto/' /etc/nginx/nginx.conf &&
\  
chown -R www-data:www-data /var/lib/nginx  
  
RUN mkdir -p /cre && touch /cre/versions.txt && \  
echo "$(date +'%F %R') \t creNginx \t $(/usr/sbin/nginx -v 2>&1 | sed -e
"s/^nginx version: nginx\///" )" >> /cre/versions.txt  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/conf.d", "/var/log/nginx",
"/var/www/html"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command.  
CMD ["nginx"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

