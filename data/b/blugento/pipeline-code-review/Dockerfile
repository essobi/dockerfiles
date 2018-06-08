FROM php:7.0  
RUN apt-get update && apt-get install -y unzip git python3 python3-pip
libyaml-dev phpmd  
RUN pip3 install awscli  
RUN pear install pear/PHP_CodeSniffer  
RUN git clone https://github.com/magento-ecg/coding-standard  

