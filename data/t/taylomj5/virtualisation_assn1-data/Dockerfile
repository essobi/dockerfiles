FROM ubuntu:14.04  
MAINTAINER Matthew Taylor <taylomj5@student.op.ac.nz>  
ENV REFRESHED_AT 2014-06-01  
RUN apt-get -yqq update  
RUN mkdir -p /var/www/html  
  
COPY index.html /var/www/html/index.html  
  
VOLUME ["/var/www/html"]  
  

