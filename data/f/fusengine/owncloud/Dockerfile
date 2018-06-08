FROM fusengine/nginx  
LABEL maintainer="Fusengine <info@fusengine.ch>"  
  
# Env owncloud  
ENV OWNCLOUD_VERSION 10.0.4  
ENV OWNCLOUD_LINKS
https://download.owncloud.org/community/owncloud-${OWNCLOUD_VERSION}.zip  
  
# Add default to owncloud  
ADD nginx/default /etc/nginx/sites-enabled/default  
  
# Download owncloud  
ADD ${OWNCLOUD_LINKS} /  
  
# Unzip file  
RUN unzip owncloud-${OWNCLOUD_VERSION}.zip && \  
rm -fr owncloud-${OWNCLOUD_VERSION}.zip  
  
# Move File to /var/www/  
RUN mv owncloud /var/www/owncloud && \  
chown -R www-data:www-data /var/www/owncloud  
  
#Volume  
VOLUME /var/www/owncloud  
  
# Workdir  
WORKDIR /var/www/owncloud  
  
# Port listen  
EXPOSE 80  

