FROM ubuntu:16.04  
MAINTAINER Gas <gas.mailbox@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y vim htop wget git unzip fortune cowsay mc software-
properties-common curl cron apache2 python-letsencrypt-apache  
  
RUN a2enmod proxy proxy_ajp proxy_http rewrite deflate headers proxy_balancer
proxy_connect proxy_html  
  
ADD ./apache/* /etc/apache2/sites-available/  
  
WORKDIR /etc/apache2/sites-enabled/  
  
RUN ln -s ../sites-available/001-analytics.booktab.it.conf
001-analytics.booktab.it.conf  
RUN ln -s ../sites-available/002-mad.analytics.booktab.it.conf
002-mad.analytics.booktab.it.conf  
RUN ln -s ../sites-available/003-testanalytics.booktab.it.conf
003-testanalytics.booktab.it.conf  
RUN ln -s ../sites-available/004-mad.testanalytics.booktab.it.conf
004-mad.testanalytics.booktab.it.conf  
RUN ln -s ../sites-available/005-devanalytics.booktab.it.conf
005-devanalytics.booktab.it.conf  
RUN ln -s ../sites-available/006-mad.devanalytics.booktab.it.conf
006-mad.devanalytics.booktab.it.conf  
  
RUN mkdir letsencrypt  
WORKDIR /letsencrypt  
  
ADD ./letsencrypt/* /letsencrypt  
#RUN letsencrypt run --config lencrypt.conf --agree-tos  
RUN /etc/init.d/apache2 restart  
CMD ["tail", "-f", "/dev/null"]

