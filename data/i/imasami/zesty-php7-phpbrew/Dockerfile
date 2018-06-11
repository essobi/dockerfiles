# docker build -t imasami/zesty-php7-phpbrew:5.3.29 .  
FROM imasami/zesty-php7-phpbrew:latest  
  
RUN set -x && \  
phpbrew install php-5.3.29 +default +pdo +mysql +pgsql && \  
source ~/.phpbrew/bashrc && \  
phpbrew switch 5.3.29 && \  
php -v  
  

