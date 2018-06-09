FROM wordpress  
  
RUN apt-get update && apt-get install -y wget vim zip jq && rm -rf
/var/lib/apt/lists/* \  
&& echo 'opcache.enable=0' > /usr/local/etc/php/conf.d/opcache-recommended.ini
\  
&& curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
  
# cargo culted from wordpress dockerfile  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

