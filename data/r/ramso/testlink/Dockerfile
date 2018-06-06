FROM debian:jessie  
MAINTAINER José Juan Escudero  
  
RUN apt-get update && apt-get -y install apache2 php5 php5-ldap php5-mysql
php5-gd curl supervisor  
  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/conf /var/log/supervisor
/var/www/html/testlink  
  
RUN a2enmod authnz_ldap && a2enmod ldap && a2enmod php5  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN rm /var/www/html/index.html  
  
RUN curl -L
http://sourceforge.net/projects/testlink/files/latest/download?source=navbar >
testlink.tar.gz  
  
RUN tar xvzf testlink.tar.gz --directory /var/tmp && \  
mv /var/tmp/testlink*/* /var/www/html/testlink/ && \  
rm -r /var/tmp/* && rm testlink.tar.gz  
  
RUN mkdir -p /var/testlink/logs && mkdir -p /var/testlink/upload_area && chown
-R www-data /var/testlink  
  
RUN chown -R www-data /var/www/html  
  
ADD init.sh /usr/bin/  
  
RUN chmod +x /usr/bin/init.sh  
  
EXPOSE 80 443  
VOLUME /var/conf  
  
CMD ["/usr/bin/supervisord"]

