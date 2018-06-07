FROM php:5.6-apache  
  
RUN apt-get update && apt-get -y upgrade && apt-get -y --force-yes install
unzip php5-mysqlnd  
  
RUN curl -o /q2a.zip http://www.question2answer.org/question2answer-latest.zip
&& unzip /q2a.zip -d /q2a && mv /q2a/*/* /var/www/html/ && rm /q2a.zip && rm
-rf /q2a  
  
RUN mv /var/www/html/qa-config-example.php /var/www/html/qa-config.php  
  
RUN sed -i -e 's/127.0.0.1/db/' /var/www/html/qa-config.php && \  
sed -i -e 's/your-mysql-username/q2a/' /var/www/html/qa-config.php && \  
sed -i -e 's/your-mysql-password/q2a/' /var/www/html/qa-config.php && \  
sed -i -e 's/your-mysql-db-name/q2a/' /var/www/html/qa-config.php  
  
RUN docker-php-ext-install mysqli  

