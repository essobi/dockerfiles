FROM ubuntu:trusty  
  
MAINTAINER dmitry@feedvisor.com  
  
RUN apt-get update \  
&& apt-get -y install \  
apache2 \  
fontconfig-config \  
fonts-dejavu-core \  
javascript-common \  
libapache2-mod-php5 \  
php5-cli \  
php5-common \  
php5-gd \  
php5-json \  
php5-mysql \  
php5-readline \  
ssl-cert \  
awscli \  
&& a2enmod \  
rewrite \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /opt  
  
ADD entrypoint.sh /entrypoint.sh  
  
CMD bash /entrypoint.sh  

