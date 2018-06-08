FROM ubuntu:16.04  
MAINTAINER mamor <mamor.dev@gmail.com>  
  
#  
# initialize  
#  
RUN mv /bin/sh /bin/sh.original && ln -s /bin/bash /bin/sh  
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
RUN apt-get update  
COPY conf/ssh/config /root/.ssh/config  
  
#  
# utilities  
#  
RUN apt-get install -y curl dnsutils fonts-migmix git iputils-ping vim  
COPY conf/fonts/local.conf /etc/fonts/local.conf  
  
#  
# java  
#  
RUN apt-get install -y default-jre  
  
#  
# npm  
#  
ENV SELENIUM_VERSION 3.4.0  
RUN apt-get install -y npm  
RUN npm install -g n && n stable && apt-get purge -y nodejs npm  
RUN npm install -g gulp@4 phantomjs-prebuilt webdriver-manager yarn --unsafe-
perm  
RUN webdriver-manager update --versions.standalone=${SELENIUM_VERSION}  
  
#  
# nginx  
#  
RUN apt-get install -y nginx  
COPY conf/nginx /etc/nginx  
  
#  
# mariadb  
#  
RUN apt-get install -y mariadb-server  
COPY conf/mysql/mariadb.cnf /etc/mysql/mariadb.cnf  
  
#  
# supervisor  
#  
RUN apt-get install -y supervisor  
COPY conf/supervisor/program.conf /etc/supervisor/conf.d/program.conf  
  
#  
# capistrano  
#  
RUN apt-get install -y ruby  
RUN gem install capistrano -v "~> 3.8"  
  
#  
# phpbrew  
#  
RUN apt-get install -y autoconf libbz2-dev libcurl4-openssl-dev libmcrypt-dev
libpng-dev libreadline-dev libxml2-dev libxslt1-dev php  
RUN curl https://github.com/phpbrew/phpbrew/raw/master/phpbrew -L -o
/usr/local/bin/phpbrew  
RUN chmod +x /usr/local/bin/phpbrew  
  
ENV PHP_VERSION 7.2.3  
RUN phpbrew init  
RUN phpbrew install ${PHP_VERSION} +default +fpm +mysql +opcache +pdo +phpdbg
+sqlite  
RUN source /root/.phpbrew/bashrc && \  
phpbrew switch php-${PHP_VERSION} && \  
phpbrew app get composer && \  
phpbrew app get phpunit && \  
composer global require hirak/prestissimo:^0.3  
  
RUN ln -s /root/.phpbrew/bin/composer /usr/local/bin/  
RUN ln -s /root/.phpbrew/bin/phpunit /usr/local/bin/  
  
RUN echo "source /root/.phpbrew/bashrc" >> /root/.bashrc  
COPY conf/php/php.ini /root/.phpbrew/php/php-${PHP_VERSION}/etc/php.ini  
COPY conf/php-fpm/www.conf /root/.phpbrew/php/php-${PHP_VERSION}/etc/php-
fpm.d/www.conf  
  
# TODO: @see https://github.com/phpbrew/phpbrew/issues/761  
RUN source /root/.phpbrew/bashrc && phpbrew ext install opcache  
RUN source /root/.phpbrew/bashrc && phpbrew ext install gd  
  
RUN echo "" >> /root/.phpbrew/php/php-${PHP_VERSION}/var/db/opcache.ini  
RUN echo "opcache.enable_cli=1" >>
/root/.phpbrew/php/php-${PHP_VERSION}/var/db/opcache.ini  
RUN echo "opcache.revalidate_freq=3600" >>
/root/.phpbrew/php/php-${PHP_VERSION}/var/db/opcache.ini  
RUN echo "" >> /root/.phpbrew/php/php-${PHP_VERSION}/var/db/opcache.ini  
  
RUN echo "" >> /etc/supervisor/conf.d/program.conf  
RUN echo "[program:php-fpm]" >> /etc/supervisor/conf.d/program.conf  
RUN echo "command=/root/.phpbrew/php/php-${PHP_VERSION}/sbin/php-fpm
--nodaemonize" >> /etc/supervisor/conf.d/program.conf  
RUN echo "autorestart=true" >> /etc/supervisor/conf.d/program.conf  
RUN echo "" >> /etc/supervisor/conf.d/program.conf  
  
RUN echo "[program:webdriver]" >> /etc/supervisor/conf.d/program.conf  
RUN echo "command=webdriver-manager start
--versions.standalone=${SELENIUM_VERSION}" >>
/etc/supervisor/conf.d/program.conf  
RUN echo "autorestart=true" >> /etc/supervisor/conf.d/program.conf  
RUN echo "" >> /etc/supervisor/conf.d/program.conf  

