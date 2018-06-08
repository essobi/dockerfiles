FROM ingeus/php-base:latest  
MAINTAINER Stephen Masters <steve@scattercode.co.uk>  
  
WORKDIR /var/www/limesurvey  
  
ADD https://www.limesurvey.org/en/stable-
release?download=1309:limesurvey206plus-build150629targz limesurvey.tar.gz  
RUN tar -xvf limesurvey.tar.gz  
RUN rm -f limesurvey.tar.gz  
  
RUN mkdir upload && mkdir tmp && chown -R www-data:www-data . && chmod -R 755
. && chmod -R 770 upload && chmod -R 770 tmp  
  
COPY apache-limesurvey.conf /etc/apache2/sites-available/limesurvey.conf  
  
RUN a2dissite 000-default  
RUN a2ensite limesurvey  
  
RUN supervisorctl restart apache2  

