##################################  
# The Zen Garden :: Grav CMS #  
# Build Tag: 171122-1207 #  
##################################  
FROM alpine:latest  
MAINTAINER Chris Hammer <chris@thezengarden.net>  
  
  
# Update base and install required deps:  
########################################  
RUN apk update && apk upgrade && apk add bash apache2 apache2-ssl php7
php7-apache2 php7-memcached php7-pdo_mysql php7-pdo php7-xml php7-xmlrpc
php7-mcrypt php7-imap php7-mysqlnd php7-mbstring php7-json php7-phar php7-zlib
php7-curl php7-zip php7-gd php7-tokenizer php7-dom php7-ctype php7-fpm
php7-apcu php7-simplexml php7-snmp net-snmp wget tzdata  
  
  
# Copy init script:  
###################  
COPY init/init.sh /  
  
  
# Copy HTTPd configs:  
#####################  
COPY conf/* /etc/apache2/  
  
  
# Set default DIR:  
##################  
WORKDIR /var/www/localhost/htdocs  
  
  
# Define Volume:  
################  
VOLUME /var/www/localhost/htdocs  
  
  
# Expose port 80:  
#################  
EXPOSE 80  
  
  
# If we don't specify otherwise kickoff init:  
# ###########################################  
CMD ["/init.sh"]  

