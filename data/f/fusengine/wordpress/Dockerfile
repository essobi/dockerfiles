FROM fusengine/nginx  
LABEL maintainer="Fusengine <info@fusengine.ch>"  
  
# Env Version and language  
ENV WORDPRESS_VERSION 4.9.4  
ENV WORDPRESS_LANG fr_FR  
  
# nginx default  
ADD nginx/default /etc/nginx/sites-enabled/default  
  
# /wordpress/ so this gives us /usr/src/wordpress  
ADD
https://fr.wordpress.org/wordpress-${WORDPRESS_VERSION}-${WORDPRESS_LANG}.zip
/  
RUN unzip wordpress-${WORDPRESS_VERSION}-${WORDPRESS_LANG}.zip && \  
rm -fr wordpress-${WORDPRESS_VERSION}-${WORDPRESS_LANG}.zip && \  
mv wordpress /var/www/wordpress && \  
chown -R www-data:www-data /var/www/wordpress  
  
# To configur host  
# VOLUME /etc/nginx/sites-enabled/  
# VOLUME  
VOLUME /var/www/wordpress  
  
# Wordpress Directory  
WORKDIR /var/www/wordpress  
  
# expose port  
EXPOSE 80  

