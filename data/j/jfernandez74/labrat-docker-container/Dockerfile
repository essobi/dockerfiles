FROM circleci/php:7.1-node-browsers  
MAINTAINER Julio Fernandez <jfernandez74@gmail.com>  
  
RUN sudo pecl install -f mongodb-1.4.2  
RUN echo -e "extension=mongodb.so" | sudo tee /usr/local/etc/php/php.ini >
/dev/null  
RUN sudo composer self-update  
RUN git clone https://github.com/LabRatGroup/LabRat-R-Server.git  
RUN npm start  

