# Set the base image to Ubuntu  
FROM centos:latest  
  
# File Author / Maintainer  
MAINTAINER Thomas ILLIET <Contact@thomas-illiet.fr>  
  
# Add the ngix and PHP dependent repository  
ADD conf/nginx.repo /etc/yum.repos.d/nginx.repo  
  
# Installing nginx  
RUN yum -y install nginx  
  
# Installing PHP  
RUN yum -y --enablerepo=remi,remi-php56 install nginx php-fpm php-common  
  
# Installing supervisor  
RUN yum install -y python-setuptools  
RUN easy_install pip  
RUN pip install supervisor  
  
# Adding the configuration file of the nginx  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
ADD conf/default.conf /etc/nginx/conf.d/default.conf  
  
# Adding the configuration file of the Supervisor  
ADD conf/supervisord.conf /etc/  
  
# Adding the site files  
ADD www /var/www  
  
# Set the port to 80  
EXPOSE 80  
# Executing supervisord  
CMD ["supervisord", "-n"]

