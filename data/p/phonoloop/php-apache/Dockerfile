FROM php:7.1.1-apache  
MAINTAINER phonoloop <phonoloop@spaceape.be>  
  
# Update  
RUN apt-get update  
  
# Make VHOST changes  
# Change docroot to /current/public instead of /current  
COPY ./vhost.conf /etc/apache2/sites-available/vhost.conf  
RUN a2dissite 000-default.conf \  
&& a2ensite vhost.conf  
  
# Enable Apache modules  
RUN a2enmod rewrite  
RUN a2enmod ssl  
  
# Download extension dependencies  
RUN apt-get install -y \  
libcurl3-dev \  
libxml2-dev \  
libzzip-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libicu-dev \  
libedit-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install extensions  
RUN docker-php-ext-install pdo \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install curl \  
&& docker-php-ext-install xml \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install bcmath \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install readline  
  
# Configure extension  
RUN docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/  
# Enable extension  
RUN docker-php-ext-enable readline

