FROM mageinferno/magento2-php:7.0-fpm-1  
MAINTAINER Dmitry Schegolikhin <d.shegolihin@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y git-core bzip2 nano  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& npm install -g grunt-cli  

