FROM ubuntu:15.10  
MAINTAINER takeshi.hirosue@bigtreetc.com  
  
RUN apt-get update  
RUN apt-get install -y apache2 \  
&& a2enmod proxy_http \  
&& a2enmod proxy_fcgi  
  
ADD conf/hhvm_proxy_fcgi.conf /etc/apache2/mods-available/  
  
RUN rm /etc/apache2/sites-enabled/000-default.conf \  
&& ln -s /etc/apache2/mods-available/hhvm_proxy_fcgi.conf /etc/apache2/sites-
enabled/  
  
EXPOSE 80  
CMD ["/usr/sbin/apachectl", "-DFOREGROUND"]  

