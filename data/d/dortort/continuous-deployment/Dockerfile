FROM php:5.6-apache  
MAINTAINER Francis Dortort <francis@dortort.com>  
  
# copy php config  
COPY php.ini /usr/local/etc/php/  
  
# amend apache config  
RUN echo "\nRedirectMatch 404 /\\.git\n" >> /etc/apache2/apache2.conf  
  
# enable mod_rewrite  
RUN a2enmod rewrite  
  
# install git  
RUN apt-get update && apt-get install -y git --no-install-recommends && rm -rf
/var/lib/apt/lists/*  
  
# create app directory  
RUN mkdir -p /data/app  
  
# modify apache config  
RUN sed -e "s|/var/www/|/data/|" -i /etc/apache2/apache2.conf  
  
COPY ./docker-entrypoint.sh /  
  
RUN chmod 700 /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

