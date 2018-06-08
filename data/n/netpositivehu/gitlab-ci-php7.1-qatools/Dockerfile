FROM netpositivehu/gitlab-ci-php7.1  
  
MAINTAINER info@netpositive.hu  
  
RUN mkdir /opt/php-qa-tools && cd /opt/php-qa-tools \  
&& wget https://phar.phpunit.de/phpunit.phar -O phpunit \  
&& wget https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar -O phpcs \  
&& wget https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar -O phpcbf \  
&& wget https://phar.phpunit.de/phploc.phar -O phploc \  
&& wget http://static.pdepend.org/php/latest/pdepend.phar -O pdepend \  
&& wget http://static.phpmd.org/php/latest/phpmd.phar -O phpmd \  
&& wget https://phar.phpunit.de/phpcpd.phar -O phpcpd \  
&& wget
https://github.com/theseer/phpdox/releases/download/0.9.0/phpdox-0.9.0.phar -O
phpdox \  
&& wget http://get.sensiolabs.org/php-cs-fixer.phar -O php-cs-fixer \  
&& chmod a+x /opt/php-qa-tools/*  
  

