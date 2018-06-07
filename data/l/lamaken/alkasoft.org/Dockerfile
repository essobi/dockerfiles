# Docker file for python simple webservice build  
FROM ubuntu  
  
RUN apt-get -y update  
RUN apt-get -y install apache2  
  
RUN apt-get install -qy python  
RUN apt-get install -qy python-pip  
  
RUN apt-get -y install vim  
RUN apt-get -y install python-setuptools python  
  
RUN apt-get -y install libapache2-mod-python  
RUN pip install --upgrade pip  
  
RUN pip install image  
RUN pip install Pillow  
  
# Http settings  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
COPY index.html /var/www/html  
COPY mypys /var/www/html/mypys  
RUN rm -f /etc/apache2/sites-available/000-default.conf  
RUN unlink /etc/apache2/sites-enabled/000-default.conf  
ADD settings/000-default.conf /etc/apache2/sites-available  
RUN ln -s /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-
enabled/000-default.conf  
RUN mkdir -p /var/www/html/mypys/out  
RUN chmod 777 /var/www/html/mypys/out  
RUN a2ensite 000-default.conf  
RUN a2enmod python  
RUN a2enmod cgi  
  
EXPOSE 80  
ENTRYPOINT [ "/usr/sbin/apache2" ]  
CMD ["-D", "FOREGROUND"]  

