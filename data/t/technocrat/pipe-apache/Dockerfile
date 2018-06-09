FROM ubuntu:14.04  
  
RUN sudo apt-get -y update && \  
sudo apt-get -y install apache2 && \  
a2enmod proxy proxy_fcgi rewrite && \  
# Make www-data user uid/gid 1000 since this is the uid that boot2docker  
# will use for mounted directories.  
usermod -u 1000 www-data && \  
groupmod -g 1000 www-data  
  
ADD default /etc/apache2/sites-available/000-default.conf  
ADD entrypoint.sh /entrypoint.sh  
  
RUN chmod u+x /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  
EXPOSE 80  

