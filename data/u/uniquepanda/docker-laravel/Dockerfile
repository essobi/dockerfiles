FROM uniquepanda/docker-laravel:node_composer  
  
# Add chrome repo and install google-chrome-stable  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'  
RUN apt-get update \  
&& apt-get install -y google-chrome-stable  
  
# Install imagick  
RUN pecl install imagick && docker-php-ext-enable imagick  

