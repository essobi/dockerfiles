FROM yieldr/apache  
  
RUN set -x \  
&& mkdir -p /home/code \  
&& chown www-data:www-data -R /home/code \  
&& mkdir -p /etc/apache2/sites-available/extra \  
&& ln -sf /home/code/dist /var/www/code  
  
COPY vhost.conf /etc/apache2/sites-available/000-default.conf  
  
ONBUILD ADD dist /home/code  
  
CMD ["apachectl", "-D", "FOREGROUND"]  

