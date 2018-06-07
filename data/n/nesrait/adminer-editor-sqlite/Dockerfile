FROM php:5-alpine  
  
RUN apk --update add php5-sqlite3  
  
COPY . /usr/src/myapp  
  
WORKDIR /usr/src/myapp  
  
CMD php -S 0.0.0.0:80  

