FROM thruio/docker-webapp  
  
ADD . /app  
RUN composer install  
  
RUN sed -i "s/newrelic.appname.*/newrelic.appname = \"Automate Everything
Webapp\"/g" /etc/php5/cli/conf.d/newrelic.ini  
RUN sed -i "s/newrelic.appname.*/newrelic.appname = \"Automate Everything
Webapp\"/g" /etc/php5/apache2/conf.d/newrelic.ini

