FROM php:7.1  
MAINTAINER Bruce Li (bli@copyright.com.au)  
# based on https://hub.docker.com/r/jimmybeats/php7-mysql-python-aws-
bitbucketpipelines/~/dockerfile/  
# Install Composer Dependencies  
RUN apt-get -y update \  
&& apt-get -y install git unzip zlib1g-dev tofrodos yui-compressor ruby2.1-dev
tree dos2unix  
  
# Valuable Extensions  
RUN apt-get install -y libicu-dev \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install zip  
  
RUN apt-get install -y libxml2-dev \  
&& docker-php-ext-install dom  
  
RUN apt-get install -y libfreetype6-dev libgd-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr \  
&& docker-php-ext-install gd exif  
  
RUN docker-php-ext-install mysqli pdo pdo_mysql  
  
RUN apt-get install -y libmcrypt-dev \  
&& docker-php-ext-install mcrypt  
  
# Install XDebug  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_connect_back=on" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini  
  
# Install Redis  
RUN pecl install -o -f redis-3.1.1 \  
&& rm -rf /tmp/pear \  
&& docker-php-ext-enable redis  
  
# Install Xsl  
RUN apt-get install libxslt1.1 libxslt1-dev \  
&& docker-php-ext-install xsl  
  
# Install Composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar /usr/local/bin/composer  
  
# Install PHPUnit  
RUN COMPOSER_HOME="/opt/.composer" composer global require
"phpunit/phpunit=6.1.*" \  
&& ln -s /opt/.composer/vendor/bin/phpunit /usr/local/bin/  
  
# Install Migration ByJG  
RUN COMPOSER_HOME="/opt/.composer" composer global require
"byjg/migration=1.0.*" \  
&& ln -s /opt/.composer/vendor/bin/migrate /usr/local/bin/  
  
# Install Daemonize ByJG  
RUN COMPOSER_HOME="/opt/.composer" composer global require "byjg/php-
daemonize=1.2.*" \  
&& ln -s /opt/.composer/vendor/bin/daemonize /usr/local/bin/  
  
RUN COMPOSER_HOME="/opt/.composer" composer global require
"squizlabs/php_codesniffer=*" \  
&& ln -s /opt/.composer/vendor/bin/phpcs /usr/local/bin/ \  
&& ln -s /opt/.composer/vendor/bin/phpcbf /usr/local/bin/  
  
RUN COMPOSER_HOME=/opt/.composer composer global require "phpmd/phpmd:@stable"
\  
&& ln -s /opt/.composer/vendor/bin/phpmd /usr/local/bin/  
  
# Install MySQL  
RUN echo 'mysql-server-5.5 mysql-server/root_password password password' |
debconf-set-selections  
RUN echo 'mysql-server-5.5 mysql-server/root_password_again password password'
|debconf-set-selections  
RUN apt-get install -y mysql-server-5.5  
  
# Install Python-Pip, Ruby and Sass  
RUN apt-get -y install ruby wget python  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN gem install sass  
  
# Install AWS CLI  
RUN pip install awscli  
  
# Install Bitbucket/Snippet CLI tools  
RUN pip install pybitbucket  
RUN pip install git+https://bitbucket.org/atlassian/snippet.git  
  
# Install Node/NPM/nvm/gulp  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install nodejs  
RUN npm install -g gulp-cli  
RUN npm install -g coffee-script  
RUN npm install -g grunt-cli  
  
# Symlink node to nodejs as most things are expecting this name  
RUN ln -s "$(which nodejs)" /usr/local/bin/node  
  
# Install Wordpress CLI  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar  
RUN chmod +x wp-cli.phar  
RUN mv wp-cli.phar /usr/local/bin/wp  
  
# Set Tar compression to maximum  
RUN export GZIP=-9  
  
# Clear all unnecessary files  
RUN apt-get autoremove -y \  
&& apt-get clean all  

