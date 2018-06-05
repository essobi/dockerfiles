# CHOSING DEBIAN  
FROM creios/laravel5  
  
MAINTAINER Tim Tegeler <tegeler@creios.net>  
  
## PHP  
RUN apt-get install -y php5-xdebug  
RUN echo "xdebug.remote_enable=true" >> /etc/php5/apache2/conf.d/20-xdebug.ini  
RUN echo "xdebug.remote_connect_back=true" >>
/etc/php5/apache2/conf.d/20-xdebug.ini  
RUN echo "xdebug.profiler_enable=true" >>
/etc/php5/apache2/conf.d/20-xdebug.ini  
RUN echo "xdebug.profiler_enable_trigger=true" >>
/etc/php5/apache2/conf.d/20-xdebug.ini  
RUN echo "xdebug.profiler_output_dir=/var/www/profiling" >>
/etc/php5/apache2/conf.d/20-xdebug.ini  

