FROM dsbaars/docker_gosu_php:5.6  
# Install node.js, bower, grunt-cli  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update  
RUN apt-get install -y nodejs  
RUN npm install -g bower grunt-cli  
  
COPY docker-entrypoint.sh /  
  
RUN cd /usr/local/etc/php && echo "date.timezone=\"Europe/Amsterdam\"" >
conf.d/environment.ini && echo "memory_limit=-1" >> conf.d/environment.ini  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["php-fpm"]  

