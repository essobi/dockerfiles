FROM alpine:latest  
  
MAINTAINER atomney <atomney+docker@gmail.com>  
  
ADD start-nginx.sh /start-nginx.sh  
  
RUN apk update && \  
apk add bash wget nginx php5-common php5-fpm php5-ctype php5-json php5-gd
php5-curl php5-openssl php5-xml php5-zip php5-dom && \  
chmod +x /start-nginx.sh && \  
sed -i 's/user\ \=\ nobody/user\ \=\ nginx/' /etc/php5/php-fpm.conf && \  
sed -i 's/group\ \=\ nobdoy/group\ \=\ www-data/' /etc/php5/php-fpm.conf && \  
mkdir -p /run/nginx  
  
CMD ["./start-nginx.sh"]  

