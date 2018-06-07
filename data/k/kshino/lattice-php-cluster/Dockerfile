FROM tutum/apache-php  
#RUN apt-get update && apt-get install -yq git && rm -rf /var/lib/apt/lists/*  
RUN rm -fr /app/*  
ADD index.php /app/index.php  
ADD phpinfo.php /app/phpinfo.php  
ADD styles.css /app/styles.css  
ADD logo.png /app/logo.png  
RUN apt-get update && apt-get install -y bridge-utils libcurl3-openssl-dev
php5-dev  
RUN pecl -q install raphf  
RUN pecl -q install propro  
RUN echo "extension=raphf.so" >> /etc/php5/apache2/php.ini  
RUN echo "extension=propro.so" >> /etc/php5/apache2/php.ini  
RUN pecl -q install pecl_http-1.7.6  
RUN echo "extension=http.so" >> /etc/php5/apache2/php.ini  
  

