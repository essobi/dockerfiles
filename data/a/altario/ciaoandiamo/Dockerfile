FROM centurylink/apache-php:latest  
  
RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee
/etc/apt/sources.list.d/newrelic.list \  
&& curl -sS https://download.newrelic.com/548C16BF.gpg | apt-key add - \  
&& apt-get update \  
&& apt-get -y install php5-curl newrelic-php5 \  
&& echo newrelic-php5 newrelic-php5/application-name string "Altar.io" |
debconf-set-selections \  
&& echo newrelic-php5 newrelic-php5/license-key string
"fc8201bbacbd2865d46d6a6cd53a5274b470b43d" | debconf-set-selections \  
&& newrelic-install install  
  
ADD . /app  
ADD ./wp-config.production.php /app/wp-config.php  
  
RUN chmod 644 /app/wp-config.php  
RUN chown -R www-data:www-data /app

