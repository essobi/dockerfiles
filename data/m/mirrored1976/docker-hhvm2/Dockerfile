FROM ubuntu:16.04  
MAINTAINER takeshi.hirosue@bigtreetc.com  
  
#httpd  
RUN apt-get update  
RUN apt-get install -y apache2 \  
&& a2enmod proxy_http \  
&& a2enmod proxy_fcgi  
  
#hhvm  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449 \  
&& add-apt-repository "deb http://dl.hhvm.com/ubuntu $(lsb_release -sc) main"  
RUN apt-get update \  
&& apt-get install -y hhvm  
  
#supervisor  
RUN apt-get install -y supervisor  
  
#config  
ADD conf/supervisord.conf /etc/supervisord.conf  
ADD conf/hhvm_proxy_fcgi.conf /etc/apache2/mods-available/  
RUN rm /etc/apache2/sites-enabled/000-default.conf \  
&& ln -s /etc/apache2/mods-available/hhvm_proxy_fcgi.conf /etc/apache2/sites-
enabled/  
  
ADD .hhconfig /var/www/html/  
ADD sample/phpinfo.php /var/www/html/  
RUN chmod -R 755 /var/www/html/  
  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord", "-n"]  

