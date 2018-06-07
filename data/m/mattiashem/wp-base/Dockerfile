#Base docker file for lifeandshell.com  
FROM ubuntu  
MAINTAINER "Mattias Hemmingsson" <matte.hemmingsson@gmail.com>  
  
  
  
#Install deps  
RUn apt-get update  
RUN apt-get -y install nginx  
RUN apt-get install php-fpm php-mysql php-cli php-xml -y  
RUN apt-get install wget curl -y  
#Setup db  
#Wordpress  
ADD wordpress.conf /etc/nginx/nginx.conf  
ADD php.ini /etc/php/7.0/fpm/php.ini  
ADD php-fpm.conf /etc/php/7.0/fpm/conf.d/www.conf  
ADD php-fpm.conf_demon /etc/php/7.0/fpm/php-fpm.conf  
WORKDIR /var/www  
RUN wget http://wordpress.org/latest.tar.gz  
RUN tar -zxvf latest.tar.gz  
#RUN chown nginx:nginx -R wordpress  
RUN chown www-data:www-data -R wordpress  
RUN chmod 755 -R wordpress  
RUN chown www-data:www-data -R /var/www/wordpress/wp-content  
RUN chmod 775 -R /var/www/wordpress/wp-content  
  
#Setup Healthx  
RUN mkdir /var/www/wordpress/healthz/  
RUN echo "<html><head><title>All fine</title></head></html>" >
/var/www/wordpress/healthz/index.html  
RUN chmod 755 /var/www/wordpress/healthz/index.html  
  
#Setup php  
RUN mkdir /var/lib/php/session  
RUN chown www-data:www-data /var/lib/php/session  
RUN chmod 770 /var/lib/php/session  
  
ADD start.sh /  
RUN chmod 700 /start.sh  
  
#Start service  
#RUN systemctl start nginx.service  
#RUN systemctl start php-fpm.service  
CMD /start.sh  

