FROM ubuntu  
MAINTAINER Christian Lück <christian@lueck.tv>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
php5-cli git curl  
  
RUN useradd -m -d /home/psocksd psocksd  
USER psocksd  
WORKDIR /home/psocksd  
  
RUN git clone https://github.com/clue/psocksd.git  
RUN cd psocksd && curl -s https://getcomposer.org/installer | php && php
composer.phar install  
CMD php psocksd/bin/psocksd *:9050  
  
EXPOSE 9050  

