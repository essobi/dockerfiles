FROM ubuntu:xenial  
MAINTAINER Chilio  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
#ENV LANG="en_US.UTF-8"  
#ENV LC_CTYPE="en_US.UTF-8"  
#ENV LANGUAGE="en_US.UTF-8"  
ENV TMPDIR=/tmp  
  
RUN apt-get update -y  
RUN apt-get install -yq apt-utils  
#RUN locale  
RUN apt-get install -yq language-pack-en-base  
RUN apt-get install -yq openssl  
RUN apt-get install -yq zip unzip  
  
# RUN locale  
ENV LC_ALL="en_US.UTF-8"  
# RUN locale  
RUN apt-get install -yq software-properties-common curl wget  
RUN add-apt-repository ppa:ondrej/php  
RUN sed -i'' 's/archive\\.ubuntu\\.com/us\\.archive\\.ubuntu\\.com/'
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -yq  
RUN apt-get install -yq libgd-tools  
RUN apt-get install -yq --fix-missing php7.1-fpm php7.1-cli php7.1-xml
php7.1-zip php7.1-curl php7.1-bcmath php7.1-json \  
php7.1-mbstring php7.1-pgsql php7.1-mysql php7.1-mcrypt php7.1-gd php-xdebug
php-imagick imagemagick nginx  
  
RUN apt-get install -yq mc lynx mysql-client bzip2 make g++  
  
ENV COMPOSER_HOME /usr/local/share/composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV PATH "$COMPOSER_HOME:$COMPOSER_HOME/vendor/bin:$PATH"  
RUN \  
mkdir -pv $COMPOSER_HOME && chmod -R g+w $COMPOSER_HOME \  
&& curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) \  
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); \  
echo 'Invalid installer' . PHP_EOL; exit(1); }" \  
&& php /tmp/composer-setup.php --filename=composer --install-
dir=$COMPOSER_HOME  
  
ADD commands/start-nginx-ci-project.sh /usr/bin/start-nginx-ci-project  
  
ADD configs/.bowerrc /root/.bowerrc  
  
RUN chmod +x /usr/bin/start-nginx-ci-project  
ADD commands/configure-laravel.sh /usr/bin/configure-laravel  
  
RUN chmod +x /usr/bin/configure-laravel  
  
RUN apt-get install -yq apt-transport-https  
RUN apt-get install -yq python-software-properties  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update  
RUN apt-get install -yq nodejs  
RUN apt-get install -yq git  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -yq yarn  
RUN yarn global add bower --network-concurrency 1  
RUN wget https://phar.phpunit.de/phpunit.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
  
RUN npm install -g node-gyp  
RUN npm install -g node-sass  
RUN npm install -g gulp  
  
#ADD configs/supervisord.conf /etc/supervisor/supervisord.conf  
ADD configs/nginx-default-site /etc/nginx/sites-available/default  
ADD configs/nginx-build-site /etc/nginx/sites-available/build  
  
RUN apt-get install -y supervisor  
  
ADD configs/supervisor-nginx.conf /etc/supervisor/conf.d/supervisor-nginx.conf  
ADD configs/supervisor-phpfpm.conf /etc/supervisor/conf.d/supervisor-
phpfpm.conf  
  
ADD commands/gitpull.sh /usr/bin/gitpull  
RUN chmod +x /usr/bin/gitpull  
  
ADD commands/start-build-site.sh /usr/bin/start-build-site  
RUN chmod +x /usr/bin/start-build-site  
  
ADD commands/start-live-site.sh /usr/bin/start-live-site  
RUN chmod +x /usr/bin/start-live-site  
  
ADD build-site/index.php /var/www/html_build/index.php  
RUN chmod +x /var/www/html_build/index.php  
  
ADD commands/laravel-set-up-permissions.sh /usr/bin/laravel-set-up-permissions  
RUN chmod +x /usr/bin/laravel-set-up-permissions  
ADD configs/gitconfig /root/.gitconfig  
  
RUN service php7.1-fpm start  
RUN service php7.1-fpm stop  
RUN service nginx start  
RUN service nginx stop  
# RUN systemctl enable supervisor  
# RUN sleep 5s  
# RUN service supervisor start  
# RUN sleep 5s  
# RUN supervisorctl status  
RUN apt-get -yq clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get upgrade  
RUN apt-get autoremove  
  
ENV DOCKER_REPO_LABEL 1.0.2  
ENV LARAVEL_ENV_SOURCE .env.example  
  
EXPOSE 80 443  
ENTRYPOINT gitpull && /bin/bash  

