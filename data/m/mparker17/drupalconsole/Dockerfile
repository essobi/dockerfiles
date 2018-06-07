FROM drupal:8  
MAINTAINER M Parker "mparker17@536298.no-reply.drupal.org"  
RUN php -r "readfile('https://drupalconsole.com/installer');" > drupal.phar &&
\  
mv drupal.phar /usr/local/bin/drupal && \  
chmod +x /usr/local/bin/drupal && \  
/usr/local/bin/drupal check  
  
VOLUME [ "/var/www/html" ]  
WORKDIR "/var/www/html"  
ENTRYPOINT [ "/usr/local/bin/drupal" ]  
CMD [ "list" ]  

