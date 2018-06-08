FROM blitznote/debootstrap-amd64:16.10  
RUN apt-get update  
RUN apt-get -y install apache2  
RUN echo “Hello Apache server on Ubuntu Docker” > /var/www/html/index.html  
EXPOSE 81  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

