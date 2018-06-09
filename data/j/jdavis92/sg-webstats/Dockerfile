FROM php:5-apache  
  
MAINTAINER Joshua Davis <tubabassist@gmail.com>  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="sg-webstats" \  
org.label-schema.description="Webstats for Survival Games" \  
org.label-schema.vcs-url="https://github.com/jdavis92/Webstats.git" \  
org.label-schema.docker.cmd="docker run -d -e DB_HOST=Host_name -e
DB_USER=Mysql_username -e DB_PASS=Mysql_password -e DB_NAME=Database_name -e
DB_PREFIX=Table_Prefix -p 80:80 jdavis92/sg-webstats" \  
org.label-schema.docker.param="DB_HOST=Host name" \  
org.label-schema.docker.param="DB_USER=Mysql username" \  
org.label-schema.docker.param="DB_PASS=Mysql password" \  
org.label-schema.docker.param="DB_NAME=Database name" \  
org.label-schema.docker.param="DB_PREFIX=Table Prefix"  
  
COPY SurvivalGames /var/www/html  
  
RUN docker-php-ext-install mysql  

