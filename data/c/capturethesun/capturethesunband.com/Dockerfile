FROM nginx  
  
ADD https://github.com/YOURLS/YOURLS/archive/1.7.tar.gz /var/  
RUN mkdir -p /var/www && tar --strip-components=1 -xzf /var/1.7.tar.gz -C
/var/www  
  
RUN apt-get update  
RUN apt-get -y install php5-fpm php5-mysql ruby  
RUN usermod -a -G www-data nginx  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
ADD conf/nginx.conf /etc/nginx/conf.d/default.conf  
ADD conf/config-template.php.erb /var/www/user/config-template.php.erb  
ADD site /var/www/  
  
EXPOSE 80  
CMD erb /var/www/user/config-template.php.erb > /var/www/user/config.php &&
chmod a+rw /var/www/user/config.php && service php5-fpm start && service nginx
start  
  

