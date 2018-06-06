#FROM php:5.6-apache  
#COPY src/ /var/www/html/  
FROM centurylink/apache-php:latest  
MAINTAINER CenturyLink  
  
# Install packages  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor pwgen && \  
apt-get -y install mysql-client && \  
apt-get -y install postgresql-client  
  
# Download v7.34 of Drupal into /app  
RUN rm -fr /app && mkdir /app && cd /app && \  
curl -O http://ftp.drupal.org/files/projects/drupal-7.34.tar.gz && \  
tar -xzvf drupal-7.34.tar.gz && \  
rm drupal-7.34.tar.gz && \  
mv drupal-7.34/* drupal-7.34/.htaccess ./ && \  
mv drupal-7.34/.gitignore ./ && \  
rmdir drupal-7.34  
COPY test.html /app/test.html  
  
#Config and set permissions for setting.php  
RUN cp app/sites/default/default.settings.php app/sites/default/settings.php
&& \  
chmod a+w app/sites/default/settings.php && \  
chmod a+w app/sites/default  
  
EXPOSE 80  
CMD exec supervisord -n  

