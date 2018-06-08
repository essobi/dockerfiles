FROM debian:jessie  
  
MAINTAINER Andrew Yager <andrew@rwts.com.au>  
  
#RUN apt-get update && apt-get install -y build-essential  
RUN apt-get update && apt-get install -y apache2 php5 php5-cli php5-gd
php5-mcrypt php5-mysql mysql-client cron  
RUN apt-get update && apt-get install -y freeradius freeradius-mysql
freeradius-utils  
  
EXPOSE 1812/udp  
EXPOSE 1813/udp  
  
RUN mkdir -p /usr/src/build  
RUN mkdir /usr/src/build/sql  
COPY ./sql/radius-structure.sql /usr/src/build/sql/radius-structure.sql  
COPY ./src/start-radius.sh /usr/src/build/start-radius.sh  
COPY ./src/test-radius.sh /usr/src/build/test-radius.sh  
COPY ./src/summarise_data.php /usr/local/bin/summarise_data.php  
  
COPY ./config/radiusd.conf /etc/freeradius/radiusd.conf  
COPY ./config/sql.conf /etc/freeradius/sql.conf  
COPY ./config/sites-available/default /etc/freeradius/sites-available/default  
COPY ./config/sites-available/sql /etc/freeradius/sites-available/sql  
COPY ./config/sql/mysql/dialup.conf /etc/freeradius/sql/mysql/dialup.conf  
RUN ln -s /etc/freeradius/sites-available/sql /etc/freeradius/sites-
enabled/sql  
  
COPY ./src/load-test-data.sh /usr/src/build/load-test-data.sh  
COPY ./sql/test-data.sql /usr/src/build/sql/test-data.sql  
RUN chmod 755 /usr/src/build/load-test-data.sh  
RUN chmod 755 /usr/local/bin/summarise_data.php  
RUN ln -s /usr/local/bin/summarise_data.php
/etc/cron.hourly/99.summarise_radius_data.php  
  
USER freerad  
CMD /bin/bash /usr/src/build/start-radius.sh

