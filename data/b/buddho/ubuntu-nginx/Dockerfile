#  
# Nginx Dockerfile  
#  
# https://github.com/buddho-io/docker-ubuntu-nginx  
#  
FROM buddho/ubuntu:14.04.2-1  
MAINTAINER llinder@buddho.io  
  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" >
/etc/apt/sources.list.d/nginx.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
8B3981E7A6852F782CC4951600A6F0A3C300EE8C && \  
apt-get update && \  
apt-get install curl nginx=1.8.0* -y && \  
curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 -o /usr/local/sbin/confd && \  
chmod 755 /usr/local/sbin/confd && \  
rm /etc/nginx/sites-enabled/default && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx && \  
mkdir -p /opt/etc/nginx/sites-enabled  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command.  
CMD ["service", "nginx", "start"]  
  
# Expose ports.  
EXPOSE 80 443  

