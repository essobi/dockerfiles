FROM ubuntu:16.04  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN LC_ALL=C.UTF-8 apt-add-repository -y ppa:ondrej/php  
RUN apt-get update  
RUN apt-get install -y php5.6-cli  
  
CMD php -v  

