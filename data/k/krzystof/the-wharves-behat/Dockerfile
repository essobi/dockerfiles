FROM debian:jessie  
  
# Thanks to the great qualiboo/behat-testing by Jean-François Lépine  
MAINTAINER Christophe Graniczny  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y -q libicu52 wget php5-cli curl php5-curl git  
  
WORKDIR /var/work  
VOLUME /var/work  
  
RUN wget https://getcomposer.org/composer.phar -O /usr/local/bin/composer  
RUN chmod +x /usr/local/bin/composer  
  
# Tools for test  
RUN mkdir -p /var/tools  
RUN cd /var/tools && composer require \  
behat/behat ^3.0 \  
behat/mink-extension 2.1.0 \  
behat/mink-selenium2-driver ^1.3 \  
behat/mink ^1.7 \  
behat/mink-goutte-driver ^1.2 \  
laracasts/behat-laravel-extension ^1.0  
  
# "behat/mink-browserkit-driver:~1.2" \  
# "fabpot/goutte:~1.0"  
RUN ln -s /var/tools/vendor/bin/behat /usr/bin/behat  
  
ENTRYPOINT ["/var/tools/vendor/bin/behat", "-c", "/var/work/behat.yml"]  

