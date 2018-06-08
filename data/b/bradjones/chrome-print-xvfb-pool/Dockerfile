# Chrome Print - xvfb-pool  
#
==============================================================================  
# Because it takes a few seconds for Chrome to start and become ready to print  
# PDF documents. This container managers a pool of xvfb containers much like  
# nginx or php-fpm.  
# Extend the php-fpm container  
FROM bradjones/chrome-print-php-fpm  
  
# Add our container files  
ADD ["container-files","/"]  
  
# Define some config for the pool manager  
ENV START_WORKERS 5  
ENV MAX_WORKERS 50  
ENV MIN_SPARE_WORKERS 5  
ENV MAX_SPARE_WORKERS 35  
# Start our pool manager  
CMD ["/usr/bin/php", "/var/www/html/pool.php"]  

