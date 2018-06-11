FROM wow73611/ubuntu  
MAINTAINER wow73611 <wow73611@gmail.com>  
  
RUN \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
mkdir -p /var/www/html && \  
chown -R www-data:www-data /var/www/html  
  
EXPOSE 80  
CMD ["nginx","-c","/etc/nginx/nginx.conf"]  

