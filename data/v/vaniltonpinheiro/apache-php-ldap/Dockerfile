FROM tutum/apache-php  
MAINTAINER Vanilton Pinheiro vanilton18@gmail.com  
RUN apt-get update  
RUN apt-get install -y php5-ldap  
RUN sed -i "s/AllowOverride None/AllowOverride All/g"
/etc/apache2/apache2.conf  
RUN sed -i "s/Require all granted/#Require all granted/g"
/etc/apache2/apache2.conf  
RUN sed -i "s/Require all denied/#Require all denied/g"
/etc/apache2/apache2.conf  
ADD . /app

