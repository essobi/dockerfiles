FROM primehost/ubuntu-core  
MAINTAINER Prime-Host <info@nordloh-webdesign.de>  
  
# php directory  
RUN mkdir /run/php  
  
# update before install  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# install nginx and php  
RUN apt-get -y install mysql-client nginx php-fpm php-mysql  
RUN apt-get -y install php-xml php-mbstring php-bcmath php-zip php-pdo-mysql
php-curl php-gd php-intl php-pear  
RUN apt-get -y install php-imagick php-imap php-mcrypt php-memcache php-apcu
php-pspell php-recode php-tidy php-xmlrpc  
  
# php-fpm config  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 10G/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 10G/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/memory_limit\s*=\s*128M/memory_limit = 1G/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/max_execution_time\s*=\s*30/max_execution_time = 300/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/max_input_time\s*=\s*60/max_input_time = 600/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/; max_input_vars\s*=\s*1000/max_input_vars = 100000/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-
fpm.conf  
RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/7.0/fpm/pool.d/www.conf  
RUN sed -i "/memory_limit/d" /etc/php/7.0/fpm/pool.d/www.conf  
RUN echo "php_admin_value[memory_limit] = 1G" >>
/etc/php/7.0/fpm/pool.d/www.conf  
RUN echo "php_admin_value[post_max_size] = 10G" >>
/etc/php/7.0/fpm/pool.d/www.conf  
RUN echo "php_admin_value[max_execution_time] = 300" >>
/etc/php/7.0/fpm/pool.d/www.conf  
RUN echo "php_admin_value[upload_max_filesize] = 10G" >>
/etc/php/7.0/fpm/pool.d/www.conf  
RUN echo "php_admin_value[max_input_time] = 600" >>
/etc/php/7.0/fpm/pool.d/www.conf  
  
# nginx site conf  
ADD ./nginx-main.conf /etc/nginx/nginx.conf  
ADD ./nginx-default.conf /etc/nginx/sites-available/default  
  
# Supervisor Config  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD ./supervisord.conf /etc/supervisord.conf  
  
# clean up unneeded packages  
RUN apt-get --purge autoremove -y  
  
# Create www folder and index.php  
RUN mkdir /usr/share/nginx/www  
ADD ./index.php /usr/share/nginx/www/index.php  
RUN chown -R $PRIMEHOST_USER:$PRIMEHOST_USER /usr/share/nginx/www  
  
# Startup Script  
ADD ./nginx-start.sh /root/container-scripts/prime-host/nginx-start.sh  
RUN chmod 755 /root/container-scripts/prime-host/nginx-start.sh  
  
#NETWORK PORTS  
EXPOSE 80  
CMD ["/bin/bash", "/root/container-scripts/prime-host/nginx-start.sh"]  

