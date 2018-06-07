# VERSION 1.0.1  
FROM keboola/base-php  
MAINTAINER Ondrej Hlavacek <ondrej.hlavacek@keboola.com>  
  
WORKDIR /home  
  
# Initialize  
RUN git clone https://github.com/keboola/docker-config-encrypt-verify.git ./  
RUN git checkout tags/0.1.1  
RUN composer install --no-interaction  
  
ENTRYPOINT php ./src/run.php --data=/data  

