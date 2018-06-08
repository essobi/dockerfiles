ARG PROJECT_PHP_VERSION=7.1  
FROM php:$PROJECT_PHP_VERSION-apache  
  
WORKDIR /opt/project  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update  
RUN apt-get install -y apt-utils  
  
COPY install-locale /usr/local/bin/  
RUN chmod +x /usr/local/bin/install-locale  
RUN apt-get install -y locales\  
&& install-locale en_US.UTF-8  
ENV LC_MESSAGES=en_US.UTF-8\  
LANG=en_US.UTF-8  
RUN apt-get install -y apt-transport-https gnupg  
  
COPY apache.conf /etc/apache2/conf-available/custom.conf  
COPY apache_default_site.conf /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite\  
&& a2enconf custom  
  
RUN rm -fr /var/www\  
&& ln -s /opt/project /var/www  
  
COPY install-php-ext /usr/local/bin/  
RUN chmod +x /usr/local/bin/install-php-ext  
RUN for EXT in intl zip; do install-php-ext $EXT; done  
  
ARG PROJECT_COMPOSER_VERSION=1.6.4  
COPY install-composer /usr/local/bin/  
RUN chmod +x /usr/local/bin/install-composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN install-composer $PROJECT_COMPOSER_VERSION  
  
ARG PROJECT_NODEJS_VERSION=8.x  
COPY install-nodejs /usr/local/bin/  
RUN chmod +x /usr/local/bin/install-nodejs  
  
COPY install-yarn /usr/local/bin/  
RUN chmod +x /usr/local/bin/install-yarn  
  
COPY install-grunt /usr/local/bin/  
RUN chmod +x /usr/local/bin/install-grunt  

