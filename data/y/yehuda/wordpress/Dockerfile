FROM wordpress:php5.6-apache  
  
MAINTAINER Yehuda Deutsch <yeh@uda.co.il>  
  
RUN apt-get update -q \  
&& apt-get install -y -q zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install zip pdo pdo_mysql  

