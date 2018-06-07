# VERSION 1.0.0  
FROM keboola/base-php  
MAINTAINER Radek Tomasek <radek.tomasek@gmail.com>  
  
WORKDIR /tmp  
  
# Install NPM & Node 7.x packages on CentOS  
RUN curl -sL https://rpm.nodesource.com/setup_7.x | bash - && yum install -y
nodejs --nogpgcheck  

