FROM php:7-cli  
  
MAINTAINER Fred Cox "mcfedr@gmail.com"  
RUN apt-get update && apt-get install -y \  
unzip \  
curl \  
git \  
&& apt-get autoremove -y \  
&& apt-get clean all  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV PATH /root/.composer/vendor/bin:$PATH  
ADD composer.json /root/.composer/composer.json  
RUN composer global require sensiolabs-de/deprecation-detector  
  
CMD ["deprecation-detector", "check", "--fail", "src/", "vendor/"]  

