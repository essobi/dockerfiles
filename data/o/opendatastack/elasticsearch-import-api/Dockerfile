FROM opendatastack/docker-symfony:latest  
  
LABEL "maintainer"="Angry Cactus DevOps<devops@angrycactus.io>"  
  
# Pull source files.  
# Supervisor  
COPY ./config/supervisord/conf.d/ /etc/supervisor/conf.d/  
# Nginx  
COPY ./config/nginx/default.conf /etc/nginx/sites-available/default  
# PHP  
COPY ./config/php/fpm/pool.d/www.conf /etc/php/7.0/fpm/pool.d/www.conf  
# Symfony APP  
COPY ./ /var/www/project  
# Exec script.  
COPY ./scripts/start.sh /start.sh  
  
RUN chmod 755 /start.sh \  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/project_access.log \  
&& ln -sf /dev/stderr /var/log/nginx/project_error.log  
  
EXPOSE 80  
# Run the app  
CMD ["/bin/bash", "/start.sh"]  

