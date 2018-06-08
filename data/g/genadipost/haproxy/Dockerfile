FROM python:2.7  
MAINTAINER Genadi Postrilko <genadipost@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
apache2 \  
&& pip install mako \  
&& git clone https://github.com/cbonte/haproxy-dconv \  
&& git clone http://git.haproxy.org/git/haproxy-1.5.git/ \  
&& git clone http://git.haproxy.org/git/haproxy-1.6.git/ \  
&& git clone http://git.haproxy.org/git/haproxy-1.7.git/ \  
&& mkdir -p /var/www/html/1.5 \  
&& mkdir -p /var/www/html/1.6 \  
&& mkdir -p /var/www/html/1.7 \  
&& python2.7 /haproxy-dconv/haproxy-dconv.py
/haproxy-1.5/doc/configuration.txt \  
-g /haproxy-1.5 \  
-o /var/www/html/1.5 \  
-b /var/www/html/1.5 \  
&& python2.7 /haproxy-dconv/haproxy-dconv.py /haproxy-1.6/doc/intro.txt \  
/haproxy-1.6/doc/configuration.txt \  
/haproxy-1.6/doc/management.txt \  
-g /haproxy-1.6 \  
-o /var/www/html/1.6 \  
-b /var/www/html/1.6 \  
&& python2.7 /haproxy-dconv/haproxy-dconv.py /haproxy-1.7/doc/intro.txt \  
/haproxy-1.7/doc/configuration.txt \  
/haproxy-1.7/doc/management.txt \  
-g /haproxy-1.7 \  
-o /var/www/html/1.7 \  
-b /var/www/html/1.7 \  
&& rm /var/www/html/index.html \  
&& echo '<IfModule dir_module>' >> /etc/apache2/apache2.conf \  
&& echo ' DirectoryIndex intro.html configuration.html' >>
/etc/apache2/apache2.conf \  
&& echo '</IfModule>' >> /etc/apache2/apache2.conf  
  
EXPOSE 80  
  
CMD apachectl -DFOREGROUND  

