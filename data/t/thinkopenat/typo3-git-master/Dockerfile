FROM tutum/apache-php:latest  
MAINTAINER Bernhard Kraft  
  
# add source for newer CURL version that has many bugfixes required for some
operations  
ADD apt-source-costamagnagianfranco_ettercap-stable-backports
/etc/apt/sources.list.d/costamagnagianfranco-ettercap-stable-backports-
trusty.list  
  
# Install packages  
RUN apt-get update && \  
apt-get -yq --force-yes install mysql-client git curl imagemagick php5-imagick
vim && \  
rm -rf /var/lib/apt/lists/*  
  
RUN a2enmod rewrite  
ADD typo3.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Adjust some php settings  
ADD typo3.php.ini /etc/php5/conf.d/  
  
# Install dependencies defined in composer.json  
RUN rm -fr /app && mkdir /app  
VOLUME ["/app/typo3temp", "/app/uploads", "/app/fileadmin"]  
  
ADD AdditionalConfiguration.php /app/typo3conf/  
ADD composer.json /app/  
RUN composer install && cp typo3conf/ext/typo3_console/Scripts/typo3cms .  
  
# Add script to create 'typo3' DB  
ADD run-typo3.sh /run-typo3.sh  
RUN chmod 755 /*.sh  
  
# Expose environment variables  
ENV DB_HOST **LinkMe**  
ENV DB_PORT **LinkMe**  
ENV DB_NAME typo3  
ENV DB_USER admin  
ENV DB_PASS **ChangeMe**  
ENV INSTALL_TOOL_PASSWORD password  
  
# Enable composer autoloader in TYPO3  
ENV TYPO3_COMPOSER_AUTOLOAD 1  
EXPOSE 80  
CMD ["/bin/bash", "-c", "/run-typo3.sh"]  

