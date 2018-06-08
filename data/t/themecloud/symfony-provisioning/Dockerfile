FROM themecloud/symfony:latest  
  
ENV PHP_MEMORY_LIMIT=128M  
  
RUN apt-get update -q \  
&& apt-get install -y git default-jre-headless nodejs node-less unzip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& chmod +x /usr/local/bin/composer  

