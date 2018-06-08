FROM wordpress:4-apache  
MAINTAINER Florian Bender <fb+dockerhub@quantumedia.de>  
  
# set PHP config to recommended values for Wordpress Uncode Theme  
RUN { \  
echo 'max_execution_time=120'; \  
echo 'max_input_vars=3000'; \  
echo 'post_max_size=42M'; \  
echo 'upload_max_filesize=40M'; \  
} > /usr/local/etc/php/conf.d/wp-uncode-reqs.ini  
  
#EOF  

