FROM nerones/simple-php-apache-dev:7.1  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get -y install bzip2 openjdk-7-jre  
RUN apt-get -y install openssh-client git nodejs curl chrpath libssl-dev
libxft-dev libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev
--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& npm install -g bower yarn gulp laravel-elixir@^6.0.0-9  
RUN rm /usr/local/etc/php/conf.d/xdebug.ini  
RUN mkdir /selenium \  
&& cd /selenium \  
&& curl -sL http://goo.gl/IHP6Qw -o selenium-standalone-server.jar \  
&& chmod +x selenium-standalone-server.jar \  
&& curl -sL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2
-o phantomjs-1.9.7-linux-x86_64.tar.bz2 \  
&& tar jxf phantomjs-1.9.7-linux-x86_64.tar.bz2 \  
&& chmod +x phantomjs-1.9.7-linux-x86_64/bin/phantomjs \  
&& mv phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs-bin
\  
&& echo "/usr/local/bin/phantomjs-bin \"\$@\" > /dev/null 2>&1" >
/usr/local/bin/phantomjs \  
&& chmod +x /usr/local/bin/phantomjs  

