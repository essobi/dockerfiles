FROM drupaldocker/php:cli  
MAINTAINER drupal-docker <info@drupaldocker.org>  
  
ADD run.sh .phpcs.yml /root/  
  
RUN composer global require drupal/coder \  
&& chmod +x /root/run.sh  
  
ENV PHPCS_CONFIG_FILE=".phpcs.yml" \  
DEBUG=FALSE  
  
CMD ["/root/run.sh"]  

