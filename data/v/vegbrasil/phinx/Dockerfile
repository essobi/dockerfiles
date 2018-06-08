FROM composer/composer  
MAINTAINER Angel Alvarado <eko3alpha>  
MAINTAINER Vinícius Santana <vinicius@vegbrasil.com>  
  
# PDO Extension  
RUN docker-php-ext-install pdo_mysql  
  
RUN composer global require 'robmorgan/phinx'  
  
ENTRYPOINT ["phinx"]  
CMD ["--help"]

