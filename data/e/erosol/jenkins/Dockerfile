# Jenkins for PHP Laravel builds using Envoy  
FROM jenkins/jenkins:lts  
MAINTAINER Kai Hempel <dev@kuweh.de>  
  
# Switch to user "root" to install the dependencies  
USER root  
  
# Install PHP 7.1  
RUN apt-get -y update \  
&& apt-get install -y apt-transport-https ca-certificates \  
&& wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg \  
&& echo "deb https://packages.sury.org/php/ stretch main" >
/etc/apt/sources.list.d/php.list \  
&& apt-get -y update \  
&& apt-get install -y php7.1-common php7.1-readline php7.1-cli php7.1-gd
php7.1-mysql php7.1-mcrypt php7.1-curl php7.1-mbstring php7.1-opcache
php7.1-json php7.1-xml build-essential  
  
# Install composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_VERSION 1.5.6  
ENV PATH "$PATH:/tmp/vendor/bin"  
RUN curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/b107d959a5924af895807021fcef4ffec5a76aa9/web/installer
\  
&& php -r " \  
\$signature =
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}" \  
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& composer --ansi --version --no-interaction \  
&& rm -rf /tmp/* \  
&& chmod -R 0777 /tmp  
  
# Install PHPUnit  
RUN wget -O phpunit https://phar.phpunit.de/phpunit-6.phar \  
&& chmod +x phpunit \  
&& mv phpunit /usr/bin/phpunit \  
&& phpunit --version  
  
# Install Laravel Envoy  
RUN composer global require laravel/envoy \  
&& chown -R jenkins /tmp  
  
# Install Node.js  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - \  
&& apt-get install -y nodejs  
  
# Switch back to "jenkins"  
USER jenkins  
  
# Generate SSH Key on startup  
COPY keygen.sh /usr/local/bin/keygen.sh  
ENTRYPOINT ["/usr/local/bin/keygen.sh", "/bin/tini", "--",
"/usr/local/bin/jenkins.sh"]

