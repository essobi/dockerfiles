# Steps to load mysqli modules and git and place the website  
#  
FROM php:7.1-apache  
MAINTAINER Gabrie van Zanten <thegabeman@gmail.com>  
# Needed to be able to download other apt-get packages  
RUN apt-get update  
  
# Are the next two lines realy needed?  
RUN apt-get install -y mysql-client libmysqlclient-dev  
RUN docker-php-ext-install mysqli  
  
# We need git to be installed so the code of the website is downloaded from
github  
RUN apt-get -y install git-core  
RUN git clone https://github.com/TheGabeMan/NestReporter.git /var/www/html  
ENV nest_user=thegabeman@gmail.com  
ENV nest_pass=N35tG@b  
  

