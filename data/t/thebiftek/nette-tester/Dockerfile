# Based on Debian Jessie  
FROM debian:jessie  
  
# Environment  
ENV TESTER_PATH /srv/tester/  
ENV TESTER_BIN /srv/tester/vendor/bin/tester  
ENV APP_PATH /srv/app/  
  
ADD dotdeb.gpg /root/dotdeb.gpg  
RUN apt-key add /root/dotdeb.gpg  
RUN echo 'deb http://packages.dotdeb.org jessie all' >>
/etc/apt/sources.list.d/dotdeb.list  
  
# Install PHP, cURL, Git  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
php7.0-cli \  
php7.0-cgi \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-mcrypt \  
php7.0-curl \  
php7.0-json \  
php7.0-xml \  
curl \  
git \  
unzip  
  
# Install Composer, Nette Tester  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
mkdir $TESTER_PATH && mkdir $APP_PATH && \  
composer require nette/tester:~1.6.0 -d $TESTER_PATH  
  
# Clean image  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Volumes  
VOLUME $APP_PATH  
  
# Default command  
COPY ./run-tester.sh /srv/run-tester.sh  
RUN chmod 755 /srv/run-tester.sh  
CMD ["/srv/run-tester.sh"]  

