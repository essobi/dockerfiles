FROM webvariants/php-sally:5.6  
  
MAINTAINER Martin Schnabel <martin@webvariants.de>  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get install -y \  
nodejs \  
&& rm -r /var/lib/apt/lists/* \  
  
&& npm install --quiet -g grunt-cli bower \  
&& npm cache clean  

