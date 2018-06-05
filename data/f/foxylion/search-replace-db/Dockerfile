FROM php:7.0-apache  
  
RUN apt-get update; apt-get install -y unzip  
RUN docker-php-ext-install mysqli  
RUN curl -o srdb.zip -L https://github.com/interconnectit/Search-Replace-
DB/archive/3.1.zip; \  
unzip srdb.zip; \  
rm srdb.zip; \  
mv Search-Replace-DB-3.1/* .; \  
rmdir Search-Replace-DB-3.1  

