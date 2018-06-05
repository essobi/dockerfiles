FROM cptactionhank/atlassian-bamboo:latest  
  
USER root  
  
# Install php  
RUN apk add --no-cache php7 php7-mcrypt php7-zip php7-json php7-openssl
php7-phar  
# Install composer  
RUN wget --output-document=/usr/local/bin/composer
https://getcomposer.org/composer.phar  
RUN chmod 755 /usr/local/bin/composer  
# Install maven  
RUN apk add --no-cache maven  
RUN mkdir -p /sbin/.m2/repository  
RUN chown daemon:daemon /sbin/.m2/repository  
# Install docker engine  
RUN apk add --no-cache docker  
  
# reset user  
# USER daemon:daemon

