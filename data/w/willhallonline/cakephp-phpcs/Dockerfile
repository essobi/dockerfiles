FROM willhallonline/phpcs  
MAINTAINER Will Hall "will@willhallonline.co.uk"  
# Install CakePHP Coding Standards  
RUN composer global require cakephp/cakephp-codesniffer  
  
# Set CakePHP as default CodeSniffer Standard  
RUN phpcs --config-set installed_paths /root/.composer/vendor/cakephp/cakephp-
codesniffer  
RUN phpcs --config-set default_standard CakePHP  
  
WORKDIR /app  
  
CMD ["phpcs"]  
CMD ["phpcbf"]  

