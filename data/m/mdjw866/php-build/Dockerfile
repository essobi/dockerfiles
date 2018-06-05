FROM mdjw866/php-cli:latest  
MAINTAINER M.D.Ward <dev@mattdw.co.uk>  
  
RUN pecl install xdebug-2.4.0 \  
&& echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20151012/xdebug.so" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& curl -o /usr/local/bin/apigen -L http://apigen.org/apigen.phar && chmod +x
/usr/local/bin/apigen \  
&& curl -o /usr/local/bin/phpunit -L https://phar.phpunit.de/phpunit.phar &&
chmod +x /usr/local/bin/phpunit \  
&& curl -o /usr/local/bin/phpcs -L
https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar && chmod +x
/usr/local/bin/phpcs \  
&& curl -o /usr/local/bin/phpcbf -L
https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar && chmod +x
/usr/local/bin/phpcbf \  
&& curl -o /usr/local/bin/phpmd -L
http://static.phpmd.org/php/latest/phpmd.phar && chmod +x /usr/local/bin/phpmd
\  
&& curl -o /usr/local/bin/phpcpd -L https://phar.phpunit.de/phpcpd.phar &&
chmod +x /usr/local/bin/phpcpd \  
&& curl -o /usr/local/bin/phploc -L https://phar.phpunit.de/phploc.phar &&
chmod +x /usr/local/bin/phploc \  
&& curl -o /usr/local/bin/pdepend -L
http://static.pdepend.org/php/latest/pdepend.phar && chmod +x
/usr/local/bin/pdepend  
  
RUN apt-get update &&\  
apt-get install -y git &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/*  

