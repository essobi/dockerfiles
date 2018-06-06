FROM codeception/codeception:2.2  
WORKDIR /repo  
RUN composer require -o --prefer-dist -n --no-progress ericmartel/codeception-
email-mailhog flow/jsonpath  
RUN docker-php-ext-install pdo_mysql  
WORKDIR /project  
  

