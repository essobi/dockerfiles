FROM php:apache  
MAINTAINER NOSPAM <nospam@nnn.nnn>  
  
RUN apt-get update  
RUN apt-get install -y ffmpeg git libmagickwand-dev --no-install-recommends  
RUN rm -rf /var/lib/apt/lists/*  
RUN pecl install imagick && docker-php-ext-enable imagick  
  
COPY init.sh /init.sh  
RUN chmod a+x /init.sh  
  
CMD ["/init.sh"]  
  
EXPOSE 80  

