FROM debian:jessie  
LABEL "maintainer"="Philippe Maladjian <flipflip[at]free.fr>" \  
"web"="https://www.blogoflip.fr" \  
"description"="Image contenant apache et pluxml, à utiliser pour le dev" \  
"version.os"="debian jessie" \  
"version.apache"="2.4.10" \  
"version.php"="5.6.30" \  
"version.pluxml"="5.6"  
  
RUN apt-get -y update \  
&& apt-get -y install apache2 php5 libapache2-mod-php5 php5-gd vim unzip \  
&& apt-get clean  
  
ADD info.php /var/www/html  
ADD pluxml-latest.zip /tmp  
ADD 000-default.conf /tmp  
RUN /usr/bin/unzip /tmp/pluxml-latest.zip \  
&& mv /tmp/000-default.conf /etc/apache2/sites-available \  
&& mv PluXml/* /var/www/html \  
&& /bin/chown -R www-data:www-data /var/www/html \  
&& /usr/sbin/a2enmod rewrite \  
&& rm -rf /tmp/*  
ENTRYPOINT service apache2 restart && bash  

