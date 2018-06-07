FROM dockerfile/ubuntu  
  
ENV NAME_LINK_NGINX php  
  
RUN apt-get update && \  
apt-get install -y php5-fpm php5-curl php5-gd php5-mcrypt php5-mysql
php5-pgsql php5-sqlite && \  
mkdir /data && mkdir /data/nginx && mkdir /data/config && mkdir /var/www  
  
ADD index.php /var/www/index.php  
ADD run.sh /phpfpm-run  
COPY nginx/ /tmp/nginx/  
  
WORKDIR /var/www  
  
VOLUME ["/var/www","/opt/nginx","/opt/config"]  
  
EXPOSE 9000  
CMD [ "bash", "/phpfpm-run" ]

