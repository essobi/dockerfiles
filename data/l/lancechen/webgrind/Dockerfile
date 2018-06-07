FROM php:5.6-apache  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y php5-xdebug \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y python \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y graphviz  
  
RUN curl -L -O https://github.com/jokkedk/webgrind/archive/master.tar.gz \  
&& mkdir /var/www/html/webgrind \  
&& tar xf master.tar.gz -C /var/www/html/webgrind --strip-components=1 \  
&& rm master.tar.gz \  
&& sed 's/\/usr\/local\/bin\/dot/\/usr\/bin\/dot/g' -i
/var/www/html/webgrind/config.php \  
&& sed 's/\/tmp/\/data/g' -i /var/www/html/webgrind/config.php  

