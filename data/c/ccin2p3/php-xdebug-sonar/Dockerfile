FROM php:5.6  
  
RUN apt-get update -yqq \  
&& apt-get install git wget unzip zlibc zlib1g zlib1g-dev libxml2-dev libssl-
dev mongodb-server -yqq  
RUN docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install opcache  
RUN pecl install xdebug \  
&& echo '' | pecl install mongo  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-2.8.zip \  
&& unzip sonar-scanner-2.8.zip \  
&& rm sonar-scanner-2.8.zip  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get install oracle-java8-installer -yqq  

