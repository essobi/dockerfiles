FROM jenkins/jenkins:lts  
# debian 9.2  
# if we want to install via apt  
USER root  
  
RUN apt-get update && apt-get install -y php7.0 php7.0-gd php7.0-apcu php-
xmlrpc php7.0-cli php7.0-geoip php7.0-mongodb php7.0-mysqli php7.0-redis
php7.0-sqlite3 php7.0-zip php7.0-curl php7.0-mbstring  
  
RUN apt-get install -y aptitude \  
ant \  
ant-contrib \  
curl  
  
RUN ln -sf /var/jenkins_home/ /var/lib/jenkins  
  
RUN cd /usr/local/bin/ && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# package  
RUN apt-get install -y build-essential debhelper devscripts  
  
# drop back to the regular jenkins user - good practice  
USER jenkins  

