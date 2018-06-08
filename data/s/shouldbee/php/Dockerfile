FROM phusion/baseimage  
  
RUN apt-get update -qq && apt-get install -y php5 php5-mysql php5-curl php5-gd
php5-memcache apache2 libapache2-mod-php5  
  
ADD php/general.ini /etc/php5/mods-available/general.ini  
ADD php/mbstring.ini /etc/php5/mods-available/mbstring.ini  
ADD php/cli.ini /etc/php5/mods-available/cli.ini  
RUN php5enmod general mbstring  
RUN php5enmod -s cli cli  
RUN mkdir /var/log/php  
  
ADD apache/apache.conf /etc/apache2/sites-available/sites.conf  
RUN a2enmod rewrite && a2ensite sites && a2dissite 000-default  
ADD apache/security.conf /etc/apache2/conf-available/security.conf  
ADD apache/ports.conf /etc/apache2/ports.conf  
  
RUN mkdir /etc/service/apache2  
ADD apache2.sh /etc/service/apache2/run  

