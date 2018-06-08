FROM simplyintricate/nginx-php  
MAINTAINER Stephen Liang "docker-maint@stephenliang.pw"  
# Download and install Mediawiki  
ENV MEDIAWIKI_MAJOR 1.27  
ENV MEDIAWIKI_MINOR 4  
ADD
http://releases.wikimedia.org/mediawiki/${MEDIAWIKI_MAJOR}/mediawiki-${MEDIAWIKI_MAJOR}.${MEDIAWIKI_MINOR}.tar.gz
/mediawiki.tar.gz  
  
# Move to the nginx install location and clean up the default items  
RUN rm -rf /usr/share/nginx/html/* && tar -xvzf /mediawiki.tar.gz -C
/usr/share/nginx/html --strip-components=1 && rm /mediawiki.tar.gz  
RUN chown -R www-data:www-data /usr/share/nginx/html  
  
# Remove the image directory, you should volume mount this from a docker
volume-only container  
RUN rm -rf /usr/share/nginx/html/images  
  
# Add the start script  
ADD start.sh /bin/start.sh  
  
CMD /bin/start.sh  
VOLUME ["/usr/share/nginx/html/images"]  

