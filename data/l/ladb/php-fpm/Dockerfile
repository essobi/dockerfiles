FROM debian:jessie  
  
MAINTAINER Christoph Kraemer "infra@ladb.de"  
RUN apt-get update && \  
apt-get install -y php5-fpm php5-mysql php5-apcu php5-gd php5-imagick
php5-curl php5-intl  
  
ADD ladb.ini /etc/php5/fpm/conf.d/  
ADD ladb.ini /etc/php5/cli/conf.d/  
  
ADD ladb.pool.conf /etc/php5/fpm/pool.d/  
  
RUN usermod -u 1000 www-data  
  
CMD ["php5-fpm", "-F"]  
  
EXPOSE 9000

