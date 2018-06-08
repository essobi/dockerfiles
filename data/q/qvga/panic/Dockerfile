FROM webdevops/php-apache:debian-9  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& curl -sL https://deb.nodesource.com/setup_9.x | bash - \  
&& apt-get install -y nodejs \  
&& apt-get clean && apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

