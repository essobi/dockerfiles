FROM webdevops/php-apache-dev:debian-8  
RUN /usr/local/bin/apt-install curl  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --version=1.5.0 --filename=composer  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash  
  
RUN /usr/local/bin/apt-install nodejs  
  
RUN /usr/bin/npm install -g bower grunt-cli  

