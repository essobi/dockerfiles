FROM kamilwojciech/apache-php55  
  
MAINTAINER Kamil Wojciech "wojciech.kamil@gmail.com"  
ADD files/apache/000-default /etc/apache2/sites-enabled/000-default  
  
RUN mkdir /var/www/web  
RUN mkdir /var/www/cache  
run chmod 777 /var/www/cache  
  
ADD files/run.sh /usr/bin/run.sh  
RUN chmod 755 /usr/bin/run.sh  
  
EXPOSE 80  
CMD ["/usr/bin/run.sh"]  
  

