FROM anezi/php-dev-tools  
  
LABEL maintainer Hassan Amouhzi  
  
ENV PROJECT_DIR /var/www/project  
  
# Install nginx  
RUN apt-get update && apt-get install -y \  
nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY ./nginx-default /etc/nginx/sites-available/default  
RUN sed -i "s/\/var\/www\/project/${PROJECT_DIR}/g" /etc/nginx/sites-
available/default  
  
EXPOSE 80  
RUN chown -R www-data:www-data /var/www  
  
VOLUME /var/www/.composer  
VOLUME ${PROJECT_DIR}  
  
COPY ./entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
WORKDIR ${PROJECT_DIR}  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]

