FROM php:5.6-apache  
  
COPY sources.list /etc/apt/sources.list  
RUN apt-get update -y --force-yes && \  
apt-get install -y git && \  
apt-get install -y --force-yes libapache2-mod-authnz-external && \  
rm -rf /var/lib/apt/lists/*  
  
RUN a2enmod rewrite  
  
ENV GITLIST_VERSION 0.5.0  
RUN mkdir -p /home/git/repositories/ \  
&& cd /home/git/repositories/ \  
&& git --bare init foo  
  
RUN curl -o /tmp/gitlist.tar.gz -SL
https://s3.amazonaws.com/gitlist/gitlist-${GITLIST_VERSION}.tar.gz \  
&& tar -xzf /tmp/gitlist.tar.gz -C /tmp/ \  
&& mv /tmp/gitlist/.htaccess /tmp/gitlist/* /var/www/html/ \  
&& rm -rf /tmp/gitlist /tmp/gitlist.tar.gz \  
&& chown -R www-data:www-data /var/www/html/ \  
&& cd /var/www/html/ \  
&& mkdir cache \  
&& chmod 777 cache \  
&& cp /var/www/html/config.ini-example /var/www/html/config.ini  
  
VOLUME /var/www/html  
WORKDIR /var/www/html/  
  
RUN a2enmod actions ;\  
a2enmod authnz_ldap ;\  
a2enmod authnz_external ;\  
a2enmod ldap ;\  
a2enmod setenvif  
  
RUN sed -i 's|LogLevel warn|LogLevel debug|g' /etc/apache2/apache2.conf  
  
# Listen on port 10080 instead of 80  
RUN sed -i 's|Listen 80|Listen 10080|g' /etc/apache2/apache2.conf  
EXPOSE 10080  
ENTRYPOINT ["apache2ctl", "-D", "FOREGROUND"]  

