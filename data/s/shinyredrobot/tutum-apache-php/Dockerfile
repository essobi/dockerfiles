FROM shinyredrobot/tutum-apache  
MAINTAINER Shawn McElroy  
  
RUN apt-get update \  
&& apt-get -y install \  
php5 \  
php5-curl \  
php5-gd \  
php5-imagick \  
php5-mcrypt \  
php5-mysqlnd \  
&& apt-get clean \  
&& apt-get autoclean \  
&& apt-get autoremove  

