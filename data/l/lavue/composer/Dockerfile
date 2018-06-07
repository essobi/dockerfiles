###  
# LaVue  
#  
# Repository: LaVue  
# Image: Composer  
# PHP Version: 7.2.x  
# Strategy: Composer from LaVue PHP-FPM-Alpine  
# Base distro: Alpine 3.7  
#  
FROM lavue/php  
  
LABEL description="Composer for LaVue"  
LABEL maintainer="4ngo.ru@gmail.com"  
  
COPY \--from=composer /usr/bin/composer /usr/bin/composer  
  
COPY \--from=composer /docker-entrypoint.sh /docker-entrypoint.sh  
#ToDo: set timezone  
#COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["composer"]  
  
LABEL version="0.1.0"  

