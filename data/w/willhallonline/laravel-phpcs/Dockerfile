FROM willhallonline/phpcs:2.9  
MAINTAINER Will Hall "will@willhallonline.co.uk"  
# Install Laravel Coding Standards
(https://github.com/antonioribeiro/laravelcs)  
RUN composer global require pragmarx/laravelcs  
  
# Set Laravel as default CodeSniffer Standard  
RUN phpcs --config-set installed_paths
/root/.composer/vendor/pragmarx/laravelcs/Standards/Laravel/  
RUN phpcs --config-set default_standard Laravel  
  
WORKDIR /app  
  
CMD ["phpcs"]  
CMD ["phpcbf"]  

