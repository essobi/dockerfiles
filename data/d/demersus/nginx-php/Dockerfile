FROM demersus/nginx:latest  
MAINTAINER Nik Petersen (demersus@gmail.com)  
RUN apt-get update  
RUN apt-get install -y php5-cli php5-curl php5-fpm php5-gd php5-mcrypt
php5-mysql php5-pgsql php5-sqlite  
RUN rm -rf /etc/php5/fpm/pool.d  
RUN mkdir -p /etc/php5/fpm/pool.d  
ADD etc /etc  
ADD supervisor.conf /etc/supervisor/conf.d/php-fpm.conf  

