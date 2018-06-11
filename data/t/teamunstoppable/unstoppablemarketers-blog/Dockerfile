FROM tutum/wordpress-stackable:latest  
MAINTAINER Antony John <antojk@gmail.com>  
  
# Add ioncube plugin to php  
ADD ioncube_loader/ /usr/lib/php5/20121212/  
RUN chmod -x /usr/lib/php5/20121212/ -R  
#ADD 20-ioncube.ini /etc/php5/apache2/conf.d/  
# Add custom themes, plugins and/or uploads  
ADD wp-content/plugins/ /app/wp-content/plugins/  
RUN chown www-data:www-data /app/wp-content -R  
  

