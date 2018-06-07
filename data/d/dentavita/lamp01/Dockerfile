FROM tutum/lamp:latest  
MAINTAINER Alexey Bogdanenko <abogdanenko@dentavita.ru>  
  
# Configure mysql server to use utf8 charset  
ADD my1.cnf /etc/mysql/conf.d/  
  
# Remove pre-installed symlink  
RUN rm /var/www/html  
  
# Add apache default config  
ADD 000-default.conf /etc/apache2/sites-available/  
  
# Setup wiki.dv.ru website  
# Install packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php5-gd php5-intl  
  
# Fix PHP Warning "Failed to write session data"  
RUN chgrp www-data /var/lib/php5  
RUN chmod 775 /var/lib/php5  
  
# Add Apache virtual host file  
ADD wiki.dv.ru.conf /etc/apache2/sites-available/  
RUN a2ensite wiki.dv.ru.conf  
  
# Add script which installs wiki  
ADD check_install_wiki.sh /  
  
# Download mediawiki  
ADD http://releases.wikimedia.org/mediawiki/1.23/mediawiki-1.23.2.tar.gz
/downloads/mediawiki.tar.gz  
  
# Add custom settings file  
ADD LocalSettings.php.append /  
  
ADD run1.sh /  
RUN chmod 755 /run1.sh  
  
CMD ["/run1.sh"]  

