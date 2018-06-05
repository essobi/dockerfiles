FROM wordpress:latest  
  
# add hostname to the view in order to know which host is serving the page  
# ugly attempt, but it works.  
RUN echo "<?php echo 'hostname:' . gethostname() ?>" >> /usr/src/wordpress/wp-
admin/install.php  
RUN echo "<?php echo 'hostname:' . gethostname() ?>" >> /usr/src/wordpress/wp-
admin/setup-config.php  
  
CMD ["apache2-foreground"]  

