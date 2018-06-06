#  
# coomy/apache2:php5  
#  
FROM reinblau/php-apache2  
  
MAINTAINER Coomy Chang <coomysky@gmail.com>  
  
  
##### Adjust time zone  
RUN echo "Asia/Taipei" > /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
  
##### System update and install  
RUN apt-get update -qq && apt-get upgrade -qq  
RUN apt-get install -qqy libapache2-mod-auth-mysql php5-mysql libapache2-mod-
php5 php5-mcrypt php5-gd php5-curl  

