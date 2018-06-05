FROM ubuntu  
MAINTAINER Cristián Rojas  
  
RUN apt-get install -y php5-cli curl git  
  
WORKDIR /phpcssec  
  
RUN curl -s http://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN git clone \  
https://github.com/FloeDesignTechnologies/phpcs-security-audit.git \  
/phpcssec  
RUN composer install  
  
WORKDIR /workdir  
  
CMD /phpcssec/vendor/bin/phpcs \  
\--extensions=php,inc,lib,module,info \  
\--standard=/phpcssec/example_base_ruleset.xml \  
.  

