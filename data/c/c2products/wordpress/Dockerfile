FROM wordpress:4  
RUN apt-get update && apt-get upgrade -y sendmail && rm -rf
/var/lib/apt/lists/*  
  
COPY ./apache2-pre_run.sh /usr/local/bin/apache2-pre_run.sh  
COPY ./php.ini /usr/local/etc/php/php.ini  
  
EXPOSE 80  
CMD ["apache2-pre_run.sh"]  

