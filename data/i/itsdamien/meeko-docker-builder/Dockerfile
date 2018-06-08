FROM php:7-alpine3.7  
LABEL maintainer="itsDamien <damien@itsdamien.com>"  
RUN apk update && apk upgrade && apk add bash git rsync gcc make  
  
# Install PHP Extensions  
ADD install-php.sh /usr/sbin/install-php.sh  
RUN /usr/sbin/install-php.sh  
  
# Install Python + NodeJS + Yarn  
ADD install-node.sh /usr/sbin/install-node.sh  
RUN /usr/sbin/install-node.sh  

