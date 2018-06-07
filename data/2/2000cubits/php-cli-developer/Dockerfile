FROM 2000cubits/php-cli:7.2  
MAINTAINER Michal Moravec "michi.m@gmail.com"  
RUN apt-get update && \  
apt-get -y --no-install-recommends install git ssh-client gnupg && \  
apt-get -y -u dist-upgrade && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget -O /usr/local/bin/composer https://getcomposer.org/composer.phar &&
chmod +x /usr/local/bin/composer && \  
wget -O /usr/local/bin/phpmd http://static.phpmd.org/php/latest/phpmd.phar &&
chmod +x /usr/local/bin/phpmd && \  
wget -O /usr/local/bin/phpcpd https://phar.phpunit.de/phpcpd.phar && chmod +x
/usr/local/bin/phpcpd && \  
wget -O /usr/local/bin/phpunit6 https://phar.phpunit.de/phpunit-6.phar &&
chmod +x /usr/local/bin/phpunit6 && \  
wget -O /usr/local/bin/phpunit https://phar.phpunit.de/phpunit-5.phar && chmod
+x /usr/local/bin/phpunit && \  
wget -O /usr/local/bin/php7cc
https://github.com/sstalle/php7cc/releases/download/1.2.1/php7cc.phar && chmod
+x /usr/local/bin/php7cc && \  
wget -O /usr/local/bin/phpcs
https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar && chmod +x
/usr/local/bin/phpcs  
  
CMD ["/usr/local/bin/boot-debian-base"]  

