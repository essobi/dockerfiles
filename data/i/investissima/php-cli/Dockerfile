FROM otassel/php-cli:ubuntu-15.10  
MAINTAINER Olivier TASSEL  
  
RUN apt-get -qq update  
RUN apt-get -qqy install \  
php-pear \  
php5-dev  
  
RUN pecl -q channel-update pecl.php.net  
RUN pecl -q install trader stats  
RUN echo "extension = trader.so" > /etc/php5/mods-available/trader.ini && \  
echo "trader.real_round_mode = HALF_UP" >> /etc/php5/mods-available/trader.ini
&& \  
echo "trader.real_precision = 2" >> /etc/php5/mods-available/trader.ini  
RUN echo "extension=stats.so" > /etc/php5/mods-available/stats.ini  
  
RUN php5enmod trader stats

