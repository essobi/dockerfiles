FROM linuxconfig/lamp  
MAINTAINER CoGe <xbian99@gmail.com>  
  
# Install prerequisites  
RUN \  
apt-get update && \  
apt-get install -y wget && \  
apt-get upgrade -y && \  
rm -rf /var/lib/apt/lists/*  
  
# Download Revive ad server  
RUN rm -fr /var/www/html/*  
RUN cd /var/www/html/; wget -q -O- https://download.revive-
adserver.com/revive-adserver-4.0.0.tar.gz | tar xz --strip 1  
  
# Create database  
RUN service mysql start; mysqladmin -uadmin -ppass create revive  
  
# Update file ownership  
RUN chown -R www-data.www-data /var/www/html  
  
# Allow ports  
EXPOSE 80  
CMD ["supervisord"]  

