FROM mrskensington/docker-php-with-ext:7-fpm  
MAINTAINER docker@mikeditum.co.uk  
  
RUN apt-get update && \  
apt-get install -y wget && \  
apt-get clean  
  
  
COPY php_lychee.ini /usr/local/etc/php/conf.d/lychee.ini  
  
RUN mkdir -p /code && \  
cd /code && \  
wget -O Lychee-master.tar.gz
https://github.com/electerious/Lychee/archive/master.tar.gz && \  
tar xvf Lychee-master.tar.gz && \  
rm -f Lychee-master.tar.gz && \  
mv Lychee-master lychee && \  
mv /code/lychee/uploads /uploads && \  
mv /code/lychee/data /data && \  
ln -s /uploads /code/lychee/uploads && \  
ln -s /data /code/lychee/data && \  
chmod -R 777 /uploads /code/lychee/uploads && \  
chmod -R 777 /data /code/lychee/data  
  
VOLUME ["/code/lychee", "/upload/", "/data"]  

