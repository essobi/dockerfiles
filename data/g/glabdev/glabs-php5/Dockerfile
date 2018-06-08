FROM ubuntu:14.04.3  
RUN apt-get update && apt-get install -y apache2 php5-mysql  
RUN apt-get update && yes | apt-get install -y libapache2-mod-php5  
  
RUN a2enmod rewrite  
  
ADD apache2.conf /etc/apache2/apache2.conf  
  
RUN apt-get clean  
RUN apt-get clean all  
RUN apt-get autoclean  
RUN apt-get autoremove  
RUN rm -rf /var/cache/apt/archive/*  
RUN rm -rf /var/www/html/*  
  
CMD ["-f","/etc/apache2/apache2.conf","-e","info","-DFOREGROUND"]  
  
ENTRYPOINT ["apachectl"]  

