# Debian: PHP 5  
#  
# VERSION 0.0.1  
# Pull the base image.  
FROM ericmdev/essentials-common  
  
# Set the author.  
MAINTAINER Eric Mugerwa <dev@ericmugerwa.com>  
  
# Set environment variables.  
ENV FILES config/  
  
# Install packages.  
RUN apt-get update && apt-get install -y \  
php5-dev \  
php5-common \  
php5-cli \  
php5-mcrypt \  
php5-mysql \  
php5-gd \  
php5-imagick \  
php5-curl \  
php5-intl  
  
# Configure executable.  
ENTRYPOINT ["/bin/bash"]  
  
# Define default command.  
CMD []

