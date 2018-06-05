# agendav  
FROM janlo/apache_base  
  
MAINTAINER Jan Losinski <losinski@wh2.tu-dresden.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y install --no-install-recommends \  
php5-pgsql \  
php5-mcrypt \  
php5-curl && \  
apt-get clean  
  
COPY agendav.conf /etc/apache2/sites-available/agendav.conf  
  
RUN a2ensite agendav && \  
a2dissite 000-default && \  
a2enmod rewrite  
  
RUN cd /var/www && \  
apt-get -y install --no-install-recommends unzip curl git ca-certificates && \  
git clone \--branch develop https://github.com/adobo/agendav.git && \  
cd agendav/web && \  
curl -s https://getcomposer.org/installer | php && \  
php composer.phar install && \  
apt-get -y remove --purge ca-certificates unzip git curl && \  
apt-get -y autoremove --purge && \  
apt-get clean  
RUN chown -R www-data:www-data /var/www/agendav/web/var  
  
COPY settings.php /var/www/agendav/web/config/  
COPY run /usr/local/bin/run_container  
  
EXPOSE 80  
ENTRYPOINT ["/usr/local/bin/run_container"]  
CMD ["apache2"]  

