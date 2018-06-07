FROM php:7.1-cli  
LABEL description="A simple image for check PHP project for known security
issues with SensioLabs"  
LABEL version="1.0"  
  
ADD http://get.sensiolabs.org/security-checker.phar /usr/local/bin/security-
checker  
RUN chmod +x /usr/local/bin/security-checker  
CMD ["/usr/local/bin/security-checker","security:check","/composer.lock"]  
  

