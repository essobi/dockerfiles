FROM hitsumabushi/ubuntu  
  
MAINTAINER hitsumabushi  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install PHP5 & SQLite(development use)  
RUN \  
apt-get update && \  
apt-get install -y php5 php5-sqlite unzip wget && \  
service apache2 restart  
  
# Install Kanboard  
RUN \  
cd /var/www/html && \  
wget http://kanboard.net/kanboard-latest.zip && \  
unzip kanboard-latest.zip && \  
chown -R www-data:www-data kanboard/data && \  
rm kanboard-latest.zip  
  
EXPOSE 80  
ENTRYPOINT /etc/init.d/apache2 start && /bin/bash  
  

