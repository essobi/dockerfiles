FROM ubuntu:latest  
  
MAINTAINER Nate Christianson "natetc95@email.arizona.edu"  
#update repositories  
RUN apt-get update  
  
#install basic admin tools  
RUN apt-get -y install nano  
RUN apt-get -y install git  
RUN apt-get -y install sudo  
  
#install webserver components  
RUN apt-get -y install nginx  
RUN apt-get -y install php-fpm  
  
#configure php  
RUN rm /etc/php/7.0/fpm/php.ini  
COPY ./nginx/php.ini /etc/php/7.0/fpm  
RUN rm /etc/php/7.0/fpm/pool.d/www.conf  
COPY ./nginx/www.conf /etc/php/7.0/fpm/pool.d/www.conf  
  
#configure nginx  
RUN rm /etc/nginx/sites-enabled/default  
COPY ./nginx/default /etc/nginx/sites-enabled  
RUN rm /var/www/html -r -f  
  
#begin final configs and pull webapp from bitbucket repository  
RUN mkdir /var/vijilis  
COPY ./www/script.sh /var/vijilis  
RUN chmod +x /var/vijilis/script.sh  
CMD /var/vijilis/script.sh  

