FROM ubuntu:16.04  
MAINTAINER Christian R. Picone <ch.picone@gmail.com>  
  
ENV port=6397  
ENV version=0.1.0  
#------ INSTALL JMETER 3.1  
RUN cd /  
ADD http://apache.panu.it//jmeter/binaries/apache-jmeter-3.1.tgz /apache-
jmeter-3.1.tgz  
RUN tar -xf apache-jmeter-3.1.tgz  
RUN rm apache-jmeter-3.1.tgz  
  
#------ INSTALL PHP 5.6  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository ppa:ondrej/php  
RUN apt-get update && apt-get install -y --allow-unauthenticated unzip php5.6  
  
#------ INSTALL WEBAPP  
ADD https://github.com/clue/php-redis-server/archive/master.zip /php-redis-
server.zip  
RUN unzip php-redis-server.zip && mv php-redis-server-master php-redis-server  
RUN rm php-redis-server.zip  
WORKDIR php-redis-server  
  
#------ INSTALL WEBAPP  
#ADD https://github.com/chpicone/jmet-ain-er/archive/${version}.zip /jmet-ain-
er.zip  
#RUN unzip jmet-ain-er.zip && mv jmet-ain-er-${version} jmet-ain-er  
#RUN rm jmet-ain-er.zip  
#WORKDIR jmet-ain-er  
#------ INSTALL COMPOSER  
ADD https://getcomposer.org/composer.phar /php-redis-server/composer.phar  
RUN php composer.phar install  
  
USER root  
EXPOSE ${port}  
CMD php bin/redis-server.php  

