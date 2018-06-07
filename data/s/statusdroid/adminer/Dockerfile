FROM adminer:latest  
MAINTAINER Lukas Pour <lukaspour@gmail.com>  
  
# change to root to edit files  
USER root  
  
# tune PHP settings for uploading large dumps  
RUN echo "upload_max_filesize = 2000M" >>
/usr/local/etc/php/conf.d/upload_large_dumps.ini \  
&& echo "post_max_size = 2000M" >>
/usr/local/etc/php/conf.d/upload_large_dumps.ini \  
&& echo "memory_limit = -1" >>
/usr/local/etc/php/conf.d/upload_large_dumps.ini \  
&& echo "max_execution_time = 0" >>
/usr/local/etc/php/conf.d/upload_large_dumps.ini  
  
# change back to user adminer  
USER adminer  

