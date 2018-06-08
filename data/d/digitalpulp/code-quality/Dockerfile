FROM php:7.1-cli-jessie  
LABEL maintainer="digitalpulp"  
  
COPY .pre-commit-config.yaml /root/pre-commit/.pre-commit-config.yaml  
COPY nodesource.sh /usr/local/bin/  
COPY pre-commit.sh /usr/local/bin/  
  
RUN chmod ugo=rx /usr/local/bin/pre-commit.sh \  
&& bash nodesource.sh \  
&& apt-get install -y nodejs build-essential \  
&& apt-get install -y bash bash-doc bash-completion \  
&& apt-get install -y git zip \  
&& apt-get install -y python python-pip python-virtualenv ca-certificates \  
&& apt-get -y clean \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer global require drupal/coder \  
&& ln -s /root/.composer/vendor/squizlabs/php_codesniffer/scripts/phpcs
/usr/local/bin/phpcs \  
&& ln -s /root/.composer/vendor/squizlabs/php_codesniffer/scripts/phpcbf
/usr/local/bin/phpcbf \  
&& pip install \--upgrade pip setuptools \  
&& pip install pre-commit \  
&& cd /root/pre-commit \  
&& git init \  
&& pre-commit install-hooks  
  
  
CMD ["tail", "-f", "/dev/null"]  

