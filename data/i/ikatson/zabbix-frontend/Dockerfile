FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install -y \  
zabbix-frontend-php nginx php5-fpm supervisor postgresql-client  
  
# Make nginx run in non-daemon mode, and disable the default site.  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
  
# Add suggested PHP options.  
ENV PHP5_FPM_INI /etc/php5/fpm/php.ini  
RUN sed -i 's/max_execution_time = .*/max_execution_time = 300/'
"${PHP5_FPM_INI}"  
RUN sed -i 's/post_max_size = .*/post_max_size = 16M/' "${PHP5_FPM_INI}"  
RUN sed -i 's/max_input_time = .*/max_input_time = 300/' "${PHP5_FPM_INI}"  
  
ADD nginx.conf /etc/nginx/sites-enabled/zabbix.conf  
ADD start.sh /start.sh  
ADD supervisor.conf /supervisor.conf  
  
EXPOSE 80  
ENTRYPOINT ["/start.sh"]  

