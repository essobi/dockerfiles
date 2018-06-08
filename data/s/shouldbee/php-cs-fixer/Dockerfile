FROM ubuntu:14.04  
RUN apt-get update -qq && apt-get install -y php5 php5-mysql php5-curl  
  
ADD http://get.sensiolabs.org/php-cs-fixer.phar /usr/local/bin/php-cs-fixer  
RUN chmod a+x /usr/local/bin/php-cs-fixer  
  
# A simple testing  
RUN php -v | grep "PHP 5.5"  
  
ENTRYPOINT ["php-cs-fixer"]  
CMD ["--help"]  

