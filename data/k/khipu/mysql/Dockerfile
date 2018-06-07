FROM mysql:5.7.12  
MAINTAINER developers@khipu.com  
  
RUN groupmod -g 2000 mysql && \  
usermod -u 2000 -g 2000 mysql && \  
chown mysql /var/run/mysqld  

