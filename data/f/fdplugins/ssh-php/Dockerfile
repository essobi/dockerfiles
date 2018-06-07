FROM php:5  
MAINTAINER thangtd90@gmail.com  
  
RUN apt-get update && apt-get install -y ca-certificates openssh-client && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY entrypoint.php /scripts/entrypoint.php  
  
ENTRYPOINT ["php", "/scripts/entrypoint.php"]  

