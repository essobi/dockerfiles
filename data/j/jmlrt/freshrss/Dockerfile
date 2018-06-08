FROM php:5.6.25-apache  
  
VOLUME /var/www/html  
  
# Install unzip  
RUN apt-get update && apt-get install unzip && rm -rf /var/lib/apt/lists  
# Install PHP zip module  
RUN apt-get update && apt-get install -y zlib1g-dev \  
&& docker-php-ext-install zip && rm -rf /var/lib/apt/lists  
# Download and install FreshRSS  
WORKDIR /tmp  
RUN curl -fsSL 'https://github.com/FreshRSS/FreshRSS/archive/master.zip' \  
-o master.zip && mkdir -p /var/www/html/rss && unzip master.zip \  
&& mv FreshRSS-master/* /var/www/html/rss && rm -fr *  

