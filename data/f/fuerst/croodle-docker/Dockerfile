# Croodle Dockerfile.  
#  
# https://github.com/fuerst/croodle-docker  
#  
# Version 1.0  
  
FROM php:7-apache  
MAINTAINER Bernhard Fürst, bernhard.fuerst@fuerstnet.de  
  
# You may overwrite the version.  
# Use a release tag from https://github.com/jelhan/croodle/releases.  
ENV CROODLE_VERSION v0.4.0-alpha4  
  
WORKDIR /var/www/html  
  
# Grab and expand release files.  
RUN rm -rf * \  
&& curl -SL -o croodle.tgz
https://github.com/jelhan/croodle/releases/download/${CROODLE_VERSION}/croodle-${CROODLE_VERSION}.tar.gz
\  
&& tar zxf croodle.tgz \  
&& rm croodle.tgz  
  
# v0.3.0 is zipped.  
# RUN rm -rf * \  
# && apt-get update && apt-get install -y unzip \  
# && curl -SL -o croodle.zip
https://github.com/jelhan/croodle/releases/download/v0.3.0/croodle-v0.3.0.zip
\  
# && unzip croodle.zip \  
# && rm croodle.zip  

