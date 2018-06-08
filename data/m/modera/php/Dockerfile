FROM cravler/php:7.2-fpm  
  
LABEL maintainer "Sergei Vizel <http://github.com/cravler>"  
  
# Common environment variables  
ENV TZ Europe/Tallinn  
  
RUN \  
\  
# All our dependencies, in alphabetical order (to ease maintenance)  
apt-get update && apt-get install -y --no-install-recommends \  
cron \  
mysql-client \  
openssh-client \  
wget && \  
\  
# Remove cache  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
\  
# Install PHP Coding Standards Fixer  
curl -s http://get.sensiolabs.org/php-cs-fixer.phar -o php-cs-fixer && \  
chmod a+x php-cs-fixer && \  
mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
ADD cf-dry.sh /usr/local/bin/cf-dry  
ADD cf-fix.sh /usr/local/bin/cf-fix  

