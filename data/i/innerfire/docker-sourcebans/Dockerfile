FROM eboraas/apache-php  
RUN apt-get update && apt-get install -yq git && rm -rf /var/lib/apt/lists/*  
RUN rm -fr /var/www/html/  
RUN mkdir /var/www/html/  
RUN git clone https://github.com/sbpp/sourcebans-pp /tmp/sourcebans  
RUN cp -R /tmp/sourcebans/web/* /var/www/html/  
ADD /config.php /var/www/html/config.php  
RUN chmod -R 777 /var/www/html/themes_c/  
RUN rm -rf /var/www/html/install/  
RUN rm -rf /var/www/html/updater/  
  

