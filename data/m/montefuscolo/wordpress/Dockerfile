FROM montefuscolo/php:1.1  
MAINTAINER Fabio Montefuscolo <fabio.montefuscolo@gmail.com>  
  
RUN curl -s -o wp-cli.phar 'https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar?0.25' \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp \  
&& wp core download --path=/var/www/html/ --version=4.7.3 --locale=pt_BR
--allow-root  
  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY htaccess /var/www/html/.htaccess  
COPY wp-config.php /var/www/html/wp-config.php  
  
RUN chown -R www-data: /var/www/html/ \  
&& mkdir -p /docker-entrypoint-extra \  
&& echo "alias wp='/usr/local/bin/wp --allow-root'" >> /root/.bashrc  
  
ENV PAGER /bin/cat  
  
EXPOSE 80 443  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

