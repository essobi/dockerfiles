FROM yappabe/php:7.1  
  
ENV ENVIRONMENT ci  
  
RUN apt-get install -y php-xdebug  
  
RUN wget -c http://www.phpdoc.org/phpDocumentor.phar \  
-P /usr/local/bin/ && \  
ln -s /usr/local/bin/phpDocumentor.phar /usr/local/bin/phpDocumentor && \  
chmod a+x /usr/local/bin/phpDocumentor  
  
RUN wget -c https://phar.phpunit.de/phpcpd.phar \  
-P /usr/local/bin/ && \  
ln -s /usr/local/bin/phpcpd.phar /usr/local/bin/phpcpd && \  
chmod a+x /usr/local/bin/phpcpd  
  
RUN wget -c https://phar.phpunit.de/phploc.phar \  
-P /usr/local/bin/ && \  
ln -s /usr/local/bin/phploc.phar /usr/local/bin/phploc && \  
chmod a+x /usr/local/bin/phploc  
  
RUN wget -c http://static.phpmd.org/php/latest/phpmd.phar \  
-P /usr/local/bin/ && \  
ln -s /usr/local/bin/phpmd.phar /usr/local/bin/phpmd && \  
chmod a+x /usr/local/bin/phpmd  
  
RUN wget -c http://static.pdepend.org/php/latest/pdepend.phar \  
-P /usr/local/bin/ && \  
ln -s /usr/local/bin/pdepend.phar /usr/local/bin/pdepend && \  
chmod a+x /usr/local/bin/pdepend  
  
RUN wget -c https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
-P /usr/local/bin/ && \  
ln -s /usr/local/bin/phpcs.phar /usr/local/bin/phpcs && \  
chmod a+x /usr/local/bin/phpcs  
  
RUN wget -c https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar \  
-P /usr/local/bin/ && \  
ln -s /usr/local/bin/phpcbf.phar /usr/local/bin/phpcbf && \  
chmod a+x /usr/local/bin/phpcbf  
  
RUN wget -c https://github.com/bytepark/php-phar-qatools/raw/master/phpcb.phar
\  
-P /usr/local/bin/ && \  
ln -s /usr/local/bin/phpcb.phar /usr/local/bin/phpcb && \  
chmod a+x /usr/local/bin/phpcb  
  
RUN wget -c https://github.com/bytepark/php-phar-
qatools/raw/master/phpdcd.phar \  
-P /usr/local/bin/ && \  
ln -s /usr/local/bin/phpdcd.phar /usr/local/bin/phpdcd && \  
chmod a+x /usr/local/bin/phpdcd  
  
RUN wget -c https://github.com/bytepark/php-phar-
qatools/raw/master/phpdox.phar \  
-P /usr/local/bin/ && \  
ln -s /usr/local/bin/phpdox.phar /usr/local/bin/phpdox && \  
chmod a+x /usr/local/bin/phpdox  
  
RUN wget -c https://phar.phpunit.de/phpunit.phar \  
-P /usr/local/bin/ && \  
ln -s /usr/local/bin/phpunit.phar /usr/local/bin/phpunit && \  
chmod a+x /usr/local/bin/phpunit  
  
ADD http://get.sensiolabs.org/php-cs-fixer.phar /usr/local/bin/php-cs-fixer  
RUN chmod a+x /usr/local/bin/php-cs-fixer  
  
RUN mkdir -p /etc/phpcs && \  
git clone git://github.com/escapestudios/Symfony2-coding-standard.git
/etc/phpcs/Symfony2-coding-standard && \  
/usr/local/bin/phpcs \--config-set installed_paths /etc/phpcs/Symfony2-coding-
standard  
  
COPY php-ci.ini /etc/php/7.1/fpm/conf.d/20-php-ci.ini  
COPY php-ci.ini /etc/php/7.1/cli/conf.d/20-php-ci.ini  
  
RUN \  
#phpDocumentor \--version && \  
phpcpd \--version && \  
phploc \--version && \  
phpmd \--version && \  
pdepend \--version && \  
phpcs \--version && \  
phpcbf \--version && \  
phpcb \--version && \  
phpunit \--version && \  
php-cs-fixer \--version && \  
phpdox \--version && \  
phpdcd \--version  
  
ENTRYPOINT []  

