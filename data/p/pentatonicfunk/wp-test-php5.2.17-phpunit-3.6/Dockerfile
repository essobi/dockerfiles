FROM debian:stretch-slim  
#docker build --rm --memory=1g --memory-swap=1g -t wp-tests:latest .  
MAINTAINER Hendrawan Kuncoro "pentatonicfunk@gmail.com"  
ENV HOME="/root"  
RUN apt update -y && \  
apt install \  
build-essential \  
ssh \  
curl \  
git \  
subversion \  
wget \  
gnupg \  
php-cli \  
php-dev \  
php-pear \  
autoconf \  
automake \  
libcurl3-openssl-dev \  
libxslt1-dev \  
mcrypt \  
libmcrypt-dev \  
libmhash-dev \  
re2c \  
libxml2 \  
libxml2-dev \  
bison \  
libbz2-dev \  
libreadline-dev \  
libicu-dev \  
libpng-dev \  
gettext \  
libmcrypt-dev \  
libmcrypt4 \  
libmhash-dev \  
libmhash2 \  
libmariadbclient-dev-compat \  
libmariadbclient-dev \  
mysql-client \  
mysql-server -y \  
\--no-install-recommends && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash && \  
apt install -y nodejs && \  
apt install -y sass --no-install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
curl -L -O https://github.com/phpbrew/phpbrew/raw/1.23.1/phpbrew && \  
chmod +x phpbrew && \  
mv phpbrew /usr/local/bin  
  
#add repos to known hosts  
RUN mkdir -p ~/.ssh  
RUN ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts  
RUN ssh-keyscan -t rsa bitbucket.org >> ~/.ssh/known_hosts  
  
#phpbrew install  
RUN phpbrew init \  
&& /bin/bash -c "source ~/.phpbrew/bashrc"; exit 0  
  
#get older php  
RUN phpbrew known --old  
  
#curl symlink  
RUN ln -s /usr/include/x86_64-linux-gnu/curl /usr/include/curl  
  
#php xml node patch  
COPY patches/php/php5.2.17.node.patch /root/php5.2.17.node.patch  
  
#PHP 5.2  
RUN phpbrew install --patch $HOME/php5.2.17.node.patch 5.2.17 \  
+bcmath +bz2 +calendar \  
+cli +ctype +curl \  
+dom +fileinfo +filter \  
+gd +gettext +icu \  
+imap +ipc +json \  
+mbregex +mbstring +mcrypt \  
+mhash +mysql +opcache \  
+pcntl +pcre +pdo \  
+pear +phar +posix \  
+readline +soap +sockets +tokenizer \  
+xml +zip \  
\-- --with-mysqli=/usr/bin/mysql_config \  
\--with-mysql=/usr/bin/mysql_config \  
\--with-pdo-mysql=/usr/bin/mysql_config \  
\--enable-spl  
  
ENV PHP_52_PATH="/root/.phpbrew/php/php-5.2.17"  
RUN cd $PHP_52_PATH/lib/php && \  
git clone \--depth=1 --branch=1.1
git://github.com/sebastianbergmann/dbunit.git && \  
git clone \--depth=1 --branch=1.1 git://github.com/sebastianbergmann/php-code-
coverage.git && \  
git clone \--depth=1 --branch=1.3.2 git://github.com/sebastianbergmann/php-
file-iterator.git && \  
git clone \--depth=1 --branch=1.1.1 git://github.com/sebastianbergmann/php-
invoker.git && \  
git clone \--depth=1 --branch=1.1.2 git://github.com/sebastianbergmann/php-
text-template.git && \  
git clone \--depth=1 --branch=1.0.3 git://github.com/sebastianbergmann/php-
timer.git && \  
git clone \--depth=1 --branch=1.1.4 git://github.com/sebastianbergmann/php-
token-stream.git && \  
git clone \--depth=1 --branch=1.1 git://github.com/sebastianbergmann/phpunit-
mock-objects.git && \  
git clone \--depth=1 --branch=1.1 git://github.com/sebastianbergmann/phpunit-
selenium.git && \  
git clone \--depth=1 --branch=1.0.0
git://github.com/sebastianbergmann/phpunit-story.git && \  
# and the version of phpunit that we expect to run with php 5.2  
git clone --depth=1 \--branch=3.6
git://github.com/sebastianbergmann/phpunit.git && \  
# fix up the version number of phpunit  
sed -i 's/@package_version@/3.6-git/g' phpunit/PHPUnit/Runner/Version.php  
  
# now set up an ini file that adds all of the above to include_path for the
PHP5.2 install  
RUN mkdir -p ${PHP_52_PATH}/var/db  
RUN echo
"include_path=.:${PHP_52_PATH}/lib/php:${PHP_52_PATH}/lib/php/dbunit:${PHP_52_PATH}/lib/php/php-
code-coverage:${PHP_52_PATH}/lib/php/php-file-
iterator:${PHP_52_PATH}/lib/php/php-invoker:${PHP_52_PATH}/lib/php/php-text-
template:${PHP_52_PATH}/lib/php/php-timer:${PHP_52_PATH}/lib/php/php-token-
stream:${PHP_52_PATH}/lib/php/phpunit-mock-
objects:${PHP_52_PATH}/lib/php/phpunit-
selenium:${PHP_52_PATH}/lib/php/phpunit-story:${PHP_52_PATH}/lib/php/phpunit"
> ${PHP_52_PATH}/var/db/path.ini  
  
#phpunit-4 PHP 5.3, PHP 5.4, or PHP 5.5  
RUN wget -O phpunit-4 https://phar.phpunit.de/phpunit-4.phar  
RUN chmod +x phpunit-4  
  
RUN rm -rf $HOME/.phpbrew/build/*  
  
#reset mysql password  
COPY scripts/reset_mysql.sql /root/reset_mysql.sql  
RUN service mysql start && \  
mysql -u root < $HOME/reset_mysql.sql  
  
#phpunit-multi script  
COPY scripts/phpunit.sh /root/phpunit.sh  
RUN chmod +x $HOME/phpunit.sh && \  
mv $HOME/phpunit.sh /usr/local/bin/phpunit  
  
COPY entrypoint.sh /root/entrypoint.sh  
ENTRYPOINT ["/root/entrypoint.sh"]  

