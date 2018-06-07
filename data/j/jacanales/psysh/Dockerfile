FROM composer:latest  
  
MAINTAINER Jesús Antonio Canales Diez <jacanalesdiez@gmail.com>  
  
RUN composer global require hirak/prestissimo && \  
composer global require psy/psysh  
  
RUN ln -s /tmp/vendor/bin/psysh /usr/local/bin/psysh  
  
VOLUME ["/bin"]  
WORKDIR /bin  
  
CMD ["/usr/local/bin/psysh"]  

