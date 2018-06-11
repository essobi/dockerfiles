FROM ubuntu:12.04  
MAINTAINER WizardCXY version: 0.1  
ENTRYPOINT echo "WizardCXY is Awesome!"  
  
RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -rf
/var/lib/apt/lists/*  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
ENTRYPOINT ["apache2"]  
EXPOSE 80  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

