FROM yieldr/apache  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
git \  
php5 \  
php5-cli \  
php5-curl \  
php5-dev \  
php5-intl \  
php5-memcached \  
php5-mongo \  
php5-mysql \  
php5-pgsql \  
php5-ssh2 \  
php5-xdebug \  
&& apt-get clean  
  
ONBUILD RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin --filename=composer  

