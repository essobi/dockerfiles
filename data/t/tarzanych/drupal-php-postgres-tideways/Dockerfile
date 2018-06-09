FROM tarzanych/drupal-php-postgres  
  
RUN wget -Otideways-php.tar.gz "https://s3-eu-
west-1.amazonaws.com/tideways/extension/4.0.8/tideways-
php-4.0.8-x86_64.tar.gz" \  
&& tar xzvf tideways-php.tar.gz \  
&& cd tideways-php-4.0.8 \  
&& bash install.sh  
  
RUN wget -Otideways-daemon.tar.gz "https://s3-eu-west-1.amazonaws.com/qafoo-
profiler/downloads/tideways-daemon_linux_amd64-1.3.7.tar.gz" \  
&& tar xzvf tideways-daemon.tar.gz \  
&& cd tideways-daemon_1.3.7 \  
&& bash install.sh  

