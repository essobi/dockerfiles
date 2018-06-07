FROM debian:wheezy  
RUN apt-get update && apt-get install -y apache2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ADD index.html /var/www/index.html  
ADD scriptIntranet.sh /script.sh  
RUN chmod +x /script.sh  
EXPOSE 80  
ENTRYPOINT /script.sh  

