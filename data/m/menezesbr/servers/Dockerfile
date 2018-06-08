FROM menezesbr/servers:u14.04a  
MAINTAINER André Menezes <menezesbr@gmail.com>  
  
# set some environment variables  
ENV APP_NAME Server_Apache_PHP  
  
# upgrade the container  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
# install Apache2  
RUN apt-get install -y --force-yes apache2 p7zip-full  
  
# install PHP 5.6  
RUN apt-get install -y --force-yes php5.6 php5.6-mysql php5.6-xml php5.6-fpm
php5.6-mcrypt php5.6-common php5.6-cli libapache2-mod-php5.6  
  
RUN a2enmod php5.6  
  
RUN service apache2 restart  
  
VOLUME ["/var/www/html"]  
VOLUME ["/etc/apache2"]  
VOLUME ["/etc/php/5.6/apache2/"]  
  
RUN usermod -u 1000 www-data && \  
chown -Rf www-data.www-data /var/www/html/  
  
RUN phpenmod mcrypt && \  
mkdir -p /run/php/ && chown -Rf www-data.www-data /run/php  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
printf "\nPATH=\"~/.composer/vendor/bin:\$PATH\"\n" | tee -a ~/.bashrc  
  
# install supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
VOLUME ["/etc/supervisor/conf.d/"]  
VOLUME ["/var/log/supervisor"]  
  
# clean up our mess  
RUN apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
# expose ports  
EXPOSE 80 443  
RUN service apache2 restart  
  
RUN a2enmod php5.6  
  
RUN service apache2 restart  
  
# set container entrypoints  
ENTRYPOINT ["/bin/bash","-c"]  
CMD ["/usr/bin/supervisord"]  
  
#RUN update-rc.d apache2 enable  

