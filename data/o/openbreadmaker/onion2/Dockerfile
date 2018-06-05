FROM php:alpine  
  
EXPOSE 8000  
ADD root/usr /usr  
RUN chmod 0777 /usr/share/breadmaker/breadmaker.sh  
  
ADD root/etc /etc  
ADD root/www /www  
  
ENV PHP php  
ENV EMULATION true  
WORKDIR /www/api  
CMD /usr/share/breadmaker/breadmaker.sh & /usr/local/bin/php -S 0.0.0.0:8000  

