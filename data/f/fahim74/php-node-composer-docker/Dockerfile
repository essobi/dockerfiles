FROM php:7-jessie  
  
ADD php.ini /usr/local/etc/php/  
# Install node.js for api docs  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - && \  
apt-get install -y zip unzip automake nodejs git libreadline-dev \  
&& apt-get install -y dh-autoreconf libpng-dev autoconf automake make g++
libtool nasm \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Install Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get -y install yarn  
  
# Install pngquant-bin  
RUN npm install apidoc -g  
  
RUN npm install pngquant-bin --save  
  
# Install Composer  
RUN curl --silent --show-error https://getcomposer.org/installer | php --
--install-dir=/usr/local/bin --filename=composer  
  
#Install Docker  
RUN curl -fsSL https://get.docker.com/ | sh  
  
RUN php -v  
RUN node -v  
RUN docker -v

