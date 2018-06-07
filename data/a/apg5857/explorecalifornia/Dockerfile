#Example from https://github.com/kstaken/dockerfile-
examples/blob/master/apache/Dockerfile  
# A basic apache server. To use either add or bind mount content under
/var/www  
FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y apache2 git && apt-get clean && rm
-rf /var/lib/apt/lists/*  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 80  
#Get website  
run cd /var/www/html  
run git clone https://github.com/AndrewGarbutt/explorecalifornia.git  
run cd explorecalifornia  
run rm -f Dockerfile  
run rm -f README.md  
  
CMD ["apachectl", "-D", "FOREGROUND"]

