FROM wordpress  
  
RUN apt-get -q update && apt-get -y upgrade && apt-get -y install nfs-common  
  
ADD wp-content /usr/src/wordpress/wp-content  
RUN chown -R www-data /usr/src/wordpress/wp-content  
  
ADD docker-entrypoint.sh /entrypoint.sh  
RUN chmod a+rwx /entrypoint.sh  

