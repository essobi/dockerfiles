FROM ubuntu:14.04  
MAINTAINER Yannick Pereira-Reis <yannick.pereira.reis@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y --force-yes \  
wget \  
php5 \  
php5-cli \  
php5-common  
  
RUN wget http://get.sensiolabs.org/php-cs-fixer.phar -O php-cs-fixer  
RUN sudo chmod a+x php-cs-fixer  
RUN sudo mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
VOLUME ["/app"]  
  
WORKDIR /app  
  
ENTRYPOINT ["php-cs-fixer"]  
  
CMD ["--help"]  

