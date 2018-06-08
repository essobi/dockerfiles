FROM wordpress:fpm  
MAINTAINER Shane Logsdon <shane@shanelogsdon.com>  
  
# Install extras  
RUN apt-get update && apt-get install -y \  
git-core \  
libmcrypt-dev \  
php5-redis  
&& docker-php-ext-install mbstring mcrypt  
  
CMD ["php-fpm"]  

