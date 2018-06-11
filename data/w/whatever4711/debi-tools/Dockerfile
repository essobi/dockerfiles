FROM debian:latest  
MAINTAINER Marcel Grossmann <whatever4711@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y install net-tools iproute  
RUN apt-get -y install iputils-*  
RUN apt-get clean && rm -rf /var/cache/apt/* /var/lib/apt/lists/*  
  

