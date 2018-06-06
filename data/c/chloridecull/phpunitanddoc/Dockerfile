FROM ubuntu:precise  
  
RUN apt-get -y update && apt-get -y install php5-cli php-pear ca-certificates
curl  
RUN pear channel-discover pear.phpdoc.org && pear install phpdoc/phpDocumentor  
RUN curl -L https://phar.phpunit.de/phpunit-old.phar > /usr/local/bin/phpunit
&& chmod +x /usr/local/bin/phpunit  

