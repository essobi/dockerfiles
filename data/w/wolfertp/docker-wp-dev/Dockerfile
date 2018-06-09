FROM hgezim/wp-nocache  
  
# Enable mbstring php module  
RUN docker-php-ext-install mbstring  
  
# Install Git  
RUN apt-get update \  
&& apt-get install git -y --force-yes  
  
# Download and install Composer  
RUN curl -sSL "https://getcomposer.org/installer" | php \  
&& mv composer.phar /usr/local/bin/composer  

