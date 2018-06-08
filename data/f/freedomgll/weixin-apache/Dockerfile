FROM django:1.8.4-python2  
MAINTAINER Leilei Gu <freedomgll@163.com>  
  
RUN apt-get update && apt-get -y install apache2 libapache2-mod-wsgi libjpeg-
dev zlib1g-dev libpng12-dev && apt-get clean  
  
RUN mkdir -p /var/www/app  
WORKDIR /var/www/app  
  
COPY requirements.txt /var/www/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY 000-default.conf /etc/apache2/sites-enabled/  
RUN echo ServerName localhost >> /etc/apache2/apache2.conf  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 8000  
EXPOSE 80  
RUN chown -R www-data:www-data /var/www/app  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

