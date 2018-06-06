FROM php:5.6-cli  
ADD http://get.sensiolabs.org/security-checker.phar /usr/local/bin/security-
checker  
RUN chmod +x /usr/local/bin/security-checker  
CMD ["/usr/local/bin/security-checker","security:check","/composer.lock"]  

