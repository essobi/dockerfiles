# Pull base image.  
FROM debian:squeeze  
MAINTAINER Decheng Zhang <killercentury@gmail.com>  
  
# Install essential tools  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install wget  
  
RUN \  
wget -O - http://www.dotdeb.org/dotdeb.gpg | apt-key add - && \  
echo "deb http://packages.dotdeb.org squeeze all" >
/etc/apt/sources.list.d/dotdeb.list && \  
echo "deb-src http://packages.dotdeb.org squeeze all" >>
/etc/apt/sources.list.d/dotdeb.list && \  
apt-get update  
  
# Install Nginx.  
RUN \  
apt-get install -y nginx && \  
echo "daemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
# Install PHP FPM  
RUN \  
DEBIAN_FRONTEND=noninteractive apt-get install -y php5-fpm php5-mysql
php5-curl php5-cli php5-memcache php-apc && \  
rm -rf /var/lib/apt/lists/*  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command.  
CMD service php5-fpm start && service nginx start  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

