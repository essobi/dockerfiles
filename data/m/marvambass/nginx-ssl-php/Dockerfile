FROM marvambass/nginx-ssl-secure  
MAINTAINER MarvAmBass  
  
RUN apt-get update; apt-get install -y \  
php5-fpm  
  
# fix pathinfo see: (https://www.digitalocean.com/community/tutorials/how-to-
install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-14-04)  
RUN sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php5/fpm/php.ini  
  
# add 'service php5-fpm start' to entrypoint.sh  
RUN sed -i 's/#!\/bin\/bash/#!\/bin\/bash\n\/etc\/init.d\/php5-fpm
start\nchmod a+rwx \/var\/run\/php5-fpm.sock/g' /opt/entrypoint.sh  

