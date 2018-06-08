FROM php:7-alpine  
  
RUN ln -s /opt/php-parallel-lint/parallel-lint /bin/parallel-lint  
  
ENV VERSION=v0.9.2  
RUN mkdir -p /opt/php-parallel-lint/ && \  
curl -L https://github.com/JakubOnderka/PHP-Parallel-
Lint/archive/$VERSION.tar.gz | \  
tar xfz - --strip-components=1 -C /opt/php-parallel-lint/  
  
RUN cd /opt/php-parallel-lint/ && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php && \  
php composer.phar install && \  
rm composer-setup.php  
  
RUN parallel-lint --help  

