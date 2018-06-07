FROM ubuntu:14.04  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN locale-gen en_AU.UTF-8  
RUN update-locale  
  
RUN apt-get update  
RUN apt-get -qq install php5 mysql-server curl git wget npm libxml2-dev
libbz2-dev libreadline6-dev libxslt-dev libcurl4-gnutls-dev libpng-dev
libgmp3-dev libicu-dev  
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h  
  
RUN curl -L -O https://github.com/phpbrew/phpbrew/raw/master/phpbrew  
RUN chmod +x phpbrew  
RUN mv phpbrew /usr/bin/phpbrew  
RUN phpbrew init  
RUN source /root/.phpbrew/bashrc  
RUN phpbrew install 5.6 as 5.6-dev +iconv +curl +icu +intl +mysql +opcache
+phar +xmlrpc +json  
RUN phpbrew use 5.6-dev  
RUN phpbrew install 7.0 as 7.0-dev like 5.6-dev  
RUN phpbrew app get composer  
RUN phpbrew app get phpunit  
RUN mv /root/.phpbrew/bin/composer /usr/bin  
  
RUN update-rc.d mysql defaults  
  
RUN composer create-project -n --no-dev --prefer-dist moodlerooms/moodle-
plugin-ci ci  
RUN chmod 777 /ci/bin/*  
RUN echo 'export PATH=$PATH:/ci/bin:/ci/vendor/bin' > /root/.bashrc  
RUN mv /root/.phpbrew/bin/phpunit /usr/bin  
  
RUN apt-get install php5-curl  
  
RUN touch /root/.bashrc && echo "[[ -e ~/.phpbrew/bashrc ]] && source
~/.phpbrew/bashrc" >> /root/.bashrc && source /root/.bashrc  

