FROM piwik:2.16.2  
  
RUN buildDeps=" \  
git \  
" \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& git clone --branch 2.2.8 https://github.com/phpredis/phpredis.git
/usr/src/php/ext/redis \  
&& docker-php-ext-configure opcache \  
&& docker-php-ext-install redis opcache  
  
RUN git clone -b "0.3.2" https://github.com/piwik/plugin-QueuedTracking/
/usr/src/piwik/plugins/QueuedTracking/ \  
&& php /usr/src/piwik/console plugin:activate QueuedTracking  

