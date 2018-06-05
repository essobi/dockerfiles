FROM php:7.1-cli  
  
ENV PROJECT_ROOT=/var/www/clean_branches  
  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
git \  
unzip \  
cron  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN mkdir -p $PROJECT_ROOT  
COPY ./ $PROJECT_ROOT  
WORKDIR $PROJECT_ROOT  
  
RUN composer require symfony/console  
  
CMD ["app/console app:search-branch /var/www/repository"]  
  

