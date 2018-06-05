FROM aerth/php:latest  
MAINTAINER aerth@sdf.org  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
ADD ./src /var/www/  
RUN cd /var/www && composer config github-oauth.github.com
10dabe4a56abd30d894ed9214aaefaa83a178c25 && composer update -v  
RUN chmod -R 0777 /var/www/app  
RUN cd /var/www/ && vendor/bin/nut database:update  
RUN cd /var/www/ && vendor/bin/nut user:add admin Admin support@isupon.us
password root  
EXPOSE 80 443  
RUN ln -sf /var/www/vendor/bolt/bolt/theme/base-2014
/var/www/public/theme/base-2014  
RUN ln -sf /var/www/vendor/bolt/bolt/theme /var/www/theme  
RUN chown -R nginx:nginx /var/www  
CMD ["/run.sh"]  

