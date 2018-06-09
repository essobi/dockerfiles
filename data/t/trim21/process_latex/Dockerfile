############################################################  
# Dockerfile to build CentOS,Nginx installed Container  
# Based on CentOS  
############################################################  
  
# Set the base image to Ubuntu  
FROM centos:latest  
  
# File Author / Maintainer  
MAINTAINER Trim21 <Trim21me@gmail.com>  
  
# Add the ngix and PHP dependent repository  
ADD config/nginx.repo /etc/yum.repos.d/nginx.repo  
  
# Installing nginx  
RUN yum -y install nginx texlive dvipng ImageMagick texlive-preprint perl  
  
  
# Installing PHP  
RUN yum -y --enablerepo=remi,remi-php56 install nginx php-fpm php-common  
  
  
# Installing supervisor  
RUN yum install -y python-setuptools  
RUN easy_install pip  
RUN pip install supervisor  
  
  
# Adding the configuration file of the nginx  
ADD config/nginx.conf /etc/nginx/nginx.conf  
ADD config/default.conf /etc/nginx/conf.d/default.conf  
  
# Adding the configuration file of the Supervisor  
ADD config/supervisord.conf /etc/  
  
# Adding the default file  
COPY src/ /var/www/  
  
RUN chmod -R 777 /var/www  
  
# Set the port to 80  
EXPOSE 80  
  
# Executing supervisord  
CMD ["supervisord", "-c", "/etc/supervisord.conf"]  

