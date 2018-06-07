FROM php:7-cli  
  
MAINTAINER Yannick PEREIRA-REIS <yannick.pereira.reis@gmail.com>  
  
ENV HOME /root  
WORKDIR /app  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
nano \  
git \  
curl \  
wget \  
ssh \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD ./composer.json /root/.composer/composer.json  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer global require sensiolabs-de/deprecation-detector  
  
ENTRYPOINT ["/root/.composer/vendor/sensiolabs-de/deprecation-
detector/bin/deprecation-detector"]  
  
CMD ["check", "src/", "vendor/"]  

