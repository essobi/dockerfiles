# From https://www.drupal.org/requirements/php#drupalversions  
# Based on Dockerfile for drupal:7-apache https://github.com/docker-
library/drupal/blob/master/7/apache/Dockerfile  
FROM eugenesia/phpfarm:wheezy  
  
LABEL maintainer="Eugene Sia <eugene@eugenesia.co.uk>" \  
description="PHP5/Apache environment using PHPFarm for developing a Drupal 7
site."  
  
# Configure Apache.  
RUN a2enmod rewrite  
COPY phpfarm.conf /etc/apache2/conf.d/  
  
# install the PHP extensions we need  
RUN apt-get update \  
&& apt-get install -y \  
# For drupal_http_request() to reach SSL sites.  
ca-certificates \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure PHP.  
COPY php.ini /usr/local/etc/php/  
  

