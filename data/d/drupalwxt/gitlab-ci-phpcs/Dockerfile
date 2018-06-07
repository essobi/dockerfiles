FROM drupalwxt/gitlab-ci  
MAINTAINER William Hearn <sylus1984@gmail.com>  
  
# Custom additions for test runner.  
RUN composer global require "squizlabs/php_codesniffer=*" && \  
composer global require drupal/coder && \  
ln -s ~/.composer/vendor/bin/phpcs /usr/local/bin && \  
phpcs --config-set installed_paths
~/.composer/vendor/drupal/coder/coder_sniffer && \  
wget
https://gist.githubusercontent.com/sylus/8532f7973b6d519f97e63f47dd010389/raw/2fe52fb83a97fee3cd520022bbc484de62f9bd81/phpcs.xml  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["sh"]  

