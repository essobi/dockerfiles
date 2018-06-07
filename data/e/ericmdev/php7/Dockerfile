# Debian: PHP 7  
#  
# VERSION 0.0.1  
# Pull the base image.  
FROM ericmdev/essentials-common  
  
# Set the author.  
MAINTAINER Eric Mugerwa <dev@ericmugerwa.com>  
  
# Set environment variables.  
ENV FILES config/  
  
# Install packages.  
RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list  
RUN wget https://www.dotdeb.org/dotdeb.gpg  
RUN apt-key add dotdeb.gpg  
RUN apt-get update && apt-get install -y \  
php7.0-common \  
php7.0-cli \  
php7.0-curl \  
php7.0-gd \  
php7.0-imagick \  
php7.0-intl \  
php7.0-json \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-opcache  
  
# Configure executable.  
ENTRYPOINT ["/bin/bash"]  
  
# Define default command.  
CMD []

