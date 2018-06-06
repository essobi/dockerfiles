FROM jenkins/jenkins:lts  
MAINTAINER Dmitry Medvedev <dvmedvedev@gmail.com>  
  
USER root  
  
RUN apt-get update && apt-get install -y apt-transport-https lsb-release ca-
certificates rsync ntp sudo  
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg && echo "deb
https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
RUN apt-get update && apt-get install -y php7.1-dev git zlib1g-dev zip unzip
php7.1-cli php7.1-curl php7.1-xml php7.1-intl php7.1-mbstring php7.1-json
php7.1-bcmath php7.1-mysql php7.1-sqlite  
  
RUN (cd /tmp && \  
wget -O php-7.1.12.tar.gz
http://de2.php.net/get/php-7.1.12.tar.gz/from/this/mirror && \  
tar -xzvf php-7.1.12.tar.gz && \  
cd php-7.1.12/ext/pcntl/ && \  
phpize && ./configure && make install && \  
#echo "extension=pcntl.so" >> /etc/php/7.1/cli/conf.d/10-pcntl.ini && \  
cd /tmp && rm -rf php-7.1.12 \  
)  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g newman grunt-cli gulp gulp-cli uglify-js uglifycss webpack  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN curl -LsS http://codeception.com/codecept.phar -o /usr/local/bin/codecept
&& chmod a+x /usr/local/bin/codecept  
  
RUN curl -LO http://www.phing.info/get/phing-latest.phar && mv phing-
latest.phar /usr/local/bin/phing && chmod +x /usr/local/bin/phing  
  
RUN apt-get install -y rsync  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN useradd -ms /bin/bash web1  
  
RUN echo "jenkins ALL=(ALL) NOPASSWD: /usr/sbin/service, /usr/sbin/ntpd" >>
/etc/sudoers  
  
USER jenkins  
  
RUN composer global require hirak/prestissimo  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/bin/bash", "--", "/usr/local/bin/entrypoint.sh"]  

