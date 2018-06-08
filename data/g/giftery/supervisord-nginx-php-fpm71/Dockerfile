FROM giftery/supervisord-nginx-php-fpm71:latest  
  
# Устанавливаем дополнительные пакеты для работы приложения:  
# - poppler-utils содержит pdftotext  
RUN yum -y install poppler-utils && \  
yum clean all && \  
rm -rf /etc/yum.repos.d/* /var/cache/*  

