FROM php:7-alpine  
RUN mkdir /Behat  
WORKDIR Behat  
RUN curl -s http://getcomposer.org/installer | php  
RUN php composer.phar require --dev behat/behat=3.1.0 behat/mink-extension=2.2
behat/mink-selenium2-driver=1.3.1  
ENV PATH $PATH:/Behat/vendor/bin  
RUN mkdir /app  
WORKDIR /app  
VOLUME /app  
ENTRYPOINT ["behat"]

