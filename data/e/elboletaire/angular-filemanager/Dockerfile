FROM php:7-apache  
  
MAINTAINER Òscar Casajuana <elboletaire@underave.net>  
  
RUN apt-get update && apt-get install -y curl && apt-get clean && \  
# install nodejs  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs  
  
RUN cd /tmp && \  
# download angular-filemanager  
curl -sL https://github.com/joni2back/angular-
filemanager/archive/master.tar.gz > master.tar.gz && \  
tar xvzf master.tar.gz && \  
rm -frv /var/www/html && \  
mv -fv angular-filemanager-master /var/www/html && \  
mkdir /var/www/files && \  
# add user with current uid (this would be much better in the entrypoint)  
adduser --quiet --no-create-home --uid 1000 me && \  
# install required node modules  
cd /var/www/html && \  
npm install --only=production  
  
ENV APACHE_RUN_USER me  
ENV APACHE_RUN_GROUP me  
  
COPY entrypoint.sh /  
  
COPY templates /templates  
  
COPY templates/index.html /var/www/html/index.html  
  
VOLUME /var/www/files  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
CMD ["apache2-foreground"]

