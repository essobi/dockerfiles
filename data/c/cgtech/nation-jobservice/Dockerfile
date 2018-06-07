FROM ubuntu:14.04  
MAINTAINER probalazs <dwamian@campgladiator.com>  
  
RUN apt-get update && apt-get install -y curl \  
php5 \  
php5-mysql \  
php5-curl \  
php5-dev \  
php5-gd \  
php5-intl \  
php-pear \  
php5-imagick \  
php5-imap \  
php5-mcrypt \  
php5-memcache \  
php5-memcached \  
php5-ming \  
php5-ps \  
php5-pspell \  
php5-recode \  
php5-sqlite \  
php5-tidy \  
php5-xmlrpc \  
php5-xsl \  
php5-pgsql \  
libpcre3-dev \  
procps \  
python \  
python-dev \  
rsyslog \  
git \  
mcrypt \  
libssh2-php \  
telnet \  
vim \  
wget  
  
ONBUILD COPY docker-php-ext-* /usr/local/bin/  
COPY docker/docker-php-ext-rdkafka-install /usr/local/bin/  
  
#clone CGNation git repo  
RUN mkdir /src  
RUN mkdir /src/cg-nation  
  
#DEV command  
#RUN git clone https://db1c79c436a4305063f454d636e4a5d4b11634ba:x-oauth-
basic@github.com/CampGladiator/CGNation.git /src/cg-nation/  
#PROD command  
RUN git clone -b jobservice_kafka_http_proxy
https://db1c79c436a4305063f454d636e4a5d4b11634ba:x-oauth-
basic@github.com/CampGladiator/CGNation.git /src/cg-nation/  
  
RUN php5enmod mcrypt  
  
#Install rdkafka  
RUN /usr/local/bin/docker-php-ext-rdkafka-install  
  
RUN chmod 777 /src/cg-nation/public_html/assets /src/cg-
nation/protected/runtime /src/cg-nation/public_html/uploads  
RUN chmod 777 /src/cg-nation/protected/extensions/hubspot/oauth_keys.json  
  
EXPOSE 22  
#Set Timezone  
RUN echo "America/Chicago" | sudo tee /etc/timezone && sudo dpkg-reconfigure
--frontend noninteractive tzdata  
  
#Cron stuff  
ADD docker/crontab /src/crontab  
RUN crontab /src/cg-nation/docker/crontab  
ADD docker/start-cron.sh /usr/bin/start-cron.sh  
RUN chmod +x /usr/bin/start-cron.sh  
RUN touch /var/log/cron.log  
  
CMD /usr/bin/start-cron.sh

