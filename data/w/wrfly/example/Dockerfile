# Micro docker  
FROM wrfly/supervisor-nginx-php:latest  
MAINTAINER wrfly mr.wrfly@gmail.com  
  
COPY app /app  
COPY app/php.ini /etc/php5/conf.d/dvwa.ini  
COPY fc-init.py /  
  
CMD ["/usr/bin/python", "/fc-init.py"]  

