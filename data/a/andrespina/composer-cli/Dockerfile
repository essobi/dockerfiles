  
FROM composer/composer:latest  
  
RUN composer global require hirak/prestissimo:0.3.4  
RUN composer global require squizlabs/php_codesniffer:2.9.1  
RUN composer global require drupal/coder:dev-8.x-2.x  
  
RUN phpcs --config-set colors 1  
RUN phpcs --config-set installed_paths
/composer/vendor/drupal/coder/coder_sniffer  
  
RUN ln -s
/composer/vendor/drupal/coder/coder_sniffer/Drupal/composer/vendor/squizlabs/php_codesniffer/CodeSniffer/Standards/Drupal  
RUN ln -s
/composer/vendor/drupal/coder/coder_sniffer/DrupalPractice/composer/vendor/squizlabs/php_codesniffer/CodeSniffer/Standards/Drupal/Practice  

