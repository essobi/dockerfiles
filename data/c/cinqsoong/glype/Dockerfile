FROM php:7.1.12-apache-jessie  
  
MAINTAINER ci.song@aliyun.com  
  
RUN apt update \  
&& apt -y --no-install-recommends install wget unzip \  
&& wget https://jaist.dl.sourceforge.net/project/glypeproxy/glype-1.1/web-
proxy-glype-1.1.zip -O /tmp/glype.zip \  
&& unzip /tmp/glype.zip -d /var/www/html/ \  
&& rm /tmp/glype.zip \  
&& chown -R www-data:www-data /var/www/html/  
  
COPY ./default.conf /etc/apache2/sites-available/000-default.conf  
  
RUN rm /etc/apache2/sites-enabled/000-default.conf \  
&& ln -s /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-
enabled/  

