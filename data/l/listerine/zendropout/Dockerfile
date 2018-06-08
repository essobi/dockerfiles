FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y apache2  
  
WORKDIR /var/www/html  
RUN rm -rf /var/www/html*  
RUN mkdir css js  
ADD affirmations.json index.html ./  
ADD js ./js  
ADD css ./css  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

