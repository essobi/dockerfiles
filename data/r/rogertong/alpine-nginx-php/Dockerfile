FROM alpine:latest  
  
ADD ./start.sh /run/  
  
RUN apk update && \  
apk add bash php5 php5-pdo php5-mysql php5-fpm php5-cgi php5-pdo_mysql
php5-json php5-xml php5-xmlrpc php5-zlib php5-mcrypt php5-imap php5-soap
openssl php5-openssl php5-cli php5-common curl php5-curl php5-gd nginx && \  
chmod a+x /run/start.sh && \  
mkdir -p /var/php/session && \  
mkdir -p /run/nginx && \  
chmod 777 /var/php/session && \  
rm -rf /var/cache/apk/* && \  
echo 'package load successed.'  
  
COPY ./nginx.conf /etc/nginx/nginx.conf  
COPY ./php.ini /etc/php/php.ini  
COPY ./info.php /var/www/info.php  
  
EXPOSE 80  
ENTRYPOINT ["/bin/bash", "/run/start.sh"]  

