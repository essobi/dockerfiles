FROM wordpress:latest  
  
  
RUN apt-get update #&& apt-get install -yqq unzip sed  
RUN curl -o /tmp/wp-cli.phar https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar  
RUN cd /tmp && chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
  
COPY dataporten_oauth/ /usr/src/wordpress/wp-content/plugins/dataporten_oauth  
RUN chown -R www-data:www-data /usr/src/wordpress/wp-
content/plugins/dataporten_oauth  
RUN sed -i '$ d' /entrypoint.sh  
RUN echo 'wp plugin activate dataporten_oauth --allow-root' >> /entrypoint.sh  
RUN echo 'exec "$@"' >> /entrypoint.sh  
  
VOLUME volume/ /var/www/  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

