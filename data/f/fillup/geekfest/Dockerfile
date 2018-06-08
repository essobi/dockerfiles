FROM silintl/apache2:latest  
COPY ./geekfest.conf /etc/apache2/sites-enabled/geekfest.conf  
COPY ./www /www  
EXPOSE 80  
CMD ["apache2ctl","-D","FOREGROUND"]  

