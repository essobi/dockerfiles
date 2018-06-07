FROM owncloud:9.0  
ENV HOSTNAME owncloud  
  
#RUN apt-get update && apt-get install -y \  
# less \  
# vim \  
#&& rm -rf /var/lib/apt/lists/*  
VOLUME /etc/apache2/cert  
VOLUME /var/apache2/log  
  
EXPOSE 443  
COPY start-apache.sh /usr/local/bin/  
  
COPY owncloud.conf /etc/apache2/conf-available/  
RUN a2enconf owncloud.conf && a2enmod ssl  
  
CMD "start-apache.sh"  

