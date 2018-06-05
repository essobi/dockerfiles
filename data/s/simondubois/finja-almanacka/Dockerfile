FROM php:7.1-apache  
  
MAINTAINER Simon Dubois <simon@dubandubois.com>  
  
RUN sed -i 's!/var/www/html!/var/www/html/public!g' /etc/apache2/sites-
enabled/000-default.conf  
  
RUN a2enmod rewrite  
  
RUN apt-get update && apt-get install -my wget gnupg  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs build-essential  
  
RUN apt-get install -y locales \  
&& echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen \  
&& echo "sv_SE.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
RUN apt-get install -y bash-completion  
  
RUN apt-get install -y nano  
  
RUN apt-get install -y git  
  
RUN apt-get install -y mysql-client \  
&& docker-php-ext-install pdo pdo_mysql  
  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
RUN apt-get install -y zlib1g-dev \  
&& docker-php-ext-install zip  
  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& echo "xdebug.var_display_max_depth = 5" >> /usr/local/etc/php/php.ini \  
&& echo "xdebug.max_nesting_level = 500" >> /usr/local/etc/php/php.ini  
  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& php /tmp/composer-setup.php -- --install-dir=/usr/local/bin
--filename=composer \  
&& rm /tmp/composer-setup.php  
  
RUN pear install PHP_CodeSniffer  
  
RUN echo "log_errors = On" >> /usr/local/etc/php/php.ini \  
&& echo "error_reporting = E_ALL" >> /usr/local/etc/php/php.ini \  
&& echo "error_log = /dev/stderr" >> /usr/local/etc/php/php.ini \  
&& echo "upload_max_filesize = 16M" >> /usr/local/etc/php/php.ini \  
&& echo "post_max_size = 16M" >> /usr/local/etc/php/php.ini  
  
ADD https://raw.githubusercontent.com/jamesob/desk/master/desk
/usr/local/bin/desk  
RUN chmod a+rx /usr/local/bin/desk  
  
ADD
https://raw.githubusercontent.com/jamesob/desk/master/shell_plugins/bash/desk
/usr/share/bash-completion/completions/desk  
RUN chmod a+r /usr/share/bash-completion/completions/desk  
  
RUN groupadd -r -g 1000 docker \  
&& useradd -r -u 1000 -g 1000 -d /home/docker -s /bin/bash docker \  
&& mkdir /home/docker \  
&& chmod 755 /home/docker \  
&& chown 1000:1000 /home/docker  
  
ADD https://raw.githubusercontent.com/git/git/master/contrib/completion/git-
prompt.sh /home/docker/.bash_gitprompt  
RUN chmod a+r /home/docker/.bash_gitprompt  
  
ENV APACHE_RUN_USER docker  
ENV APACHE_RUN_GROUP docker  

