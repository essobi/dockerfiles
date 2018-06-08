FROM tutum/apache-php  
RUN apt-get update  
RUN apt-get upgrade -q -y ;  
RUN apt-get install -q -y curl php5-gd php5-ldap php5-imap  
RUN apt-get clean  
RUN php5enmod imap  
RUN rm -rf /app && mkdir -p /app  
RUN curl -L -o /app/limesurvey.tar.bz2 https://www.limesurvey.org/en/stable-
release?download=1378:limesurvey206plus-build151018tarbz2  
RUN tar -C /app -xvjf /app/limesurvey.tar.bz2  
RUN rm /app/limesurvey.tar.bz2  
RUN chown -R www-data:www-data /app  
RUN chown www-data:www-data /var/lib/php5  
RUN cp -r /app/limesurvey/application/config
/app/limesurvey/application/config-sample  
COPY apache_default /etc/apache2/sites-available/000-default.conf  
#COPY config.php /app/limesurvey/application/config/config.php  
COPY run.sh /run.sh  
EXPOSE 80 3306  
CMD ["/run.sh"]  

