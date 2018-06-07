FROM mcuyar/docker-alpine-nginx-php7:latest  
MAINTAINER Matthew Cuyar <matt@enctypeapparel.com>  
##/  
# Install Luminary  
#/  
RUN cd /var \  
&& rm -rf www \  
&& composer create-project \--prefer-dist \--stability dev \--no-dev engage-
php/luminary www \  
&& composer clearcache \  
&& rm -rf www/composer.lock  
  
##/  
# Add composer vendor/bin to path  
#/  
ENV PATH="/var/www/vendor/bin:${PATH}"  
##/  
# Copy files  
#/  
COPY rootfs /  
  
EXPOSE 8000

