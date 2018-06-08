FROM sylvaindeloux/php7-cli:latest  
MAINTAINER Sylvain Deloux <docker@eax.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y libmagickwand-dev jpegoptim && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pecl install imagick && \  
docker-php-ext-enable imagick && \  
pecl clear-cache && \  
rm -rf /tmp/*  
  
RUN docker-php-ext-install exif  
  

