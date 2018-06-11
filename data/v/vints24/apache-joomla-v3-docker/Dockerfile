FROM gjong/apache  
  
MAINTAINER Vincent Moulene <vincentmoulene@gmail.com>  
  
RUN apt-get install -y git  
  
RUN git clone https://github.com/joomla/joomla-cms.git /tmp/www  
  
RUN rm -rf /var/www/html/*  
RUN cp -r /tmp/www/* /var/www/html/  
RUN chown www-data:www-data /var/www/html -R  
RUN a2enmod rewrite  
  
ADD ./docker/file_limit.conf /etc/apache2/conf-enabled/file_limit.conf  
ADD ./docker/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
ADD ./docker/htaccess /var/www/html/.htaccess  
  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  

