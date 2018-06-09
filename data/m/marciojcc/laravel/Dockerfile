FROM php:latest  
LABEL maintainer="marciojcc <marcio@gen.pt>"  
  
RUN apt-get update -yqq && apt-get install -my wget gnupg  
  
# Install PHP extensions  
ADD install-php.sh /usr/sbin/install-php.sh  
RUN /usr/sbin/install-php.sh  
  
# Download and install NodeJS  
ADD install-node.sh /usr/sbin/install-node.sh  
RUN /usr/sbin/install-node.sh  

