FROM php:5.6-alpine  
  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
COPY . /xhgui  
RUN cd /xhgui && composer install --ignore-platform-reqs  
  
VOLUME /xhgui  

