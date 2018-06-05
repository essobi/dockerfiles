FROM ubuntu:14.04  
MAINTAINER ANDRE LUIS <andre@netbits.com.br>  
  
RUN apt-get -y update && apt-get -y install lsb-release nscd curl php5
php5-mysql php5-cli php5-curl unzip php5-mcrypt openssh-server nano  
RUN php5enmod mcrypt  
RUN service apache2 restart  
  
COPY /sis/iptv_panel_pro.zip /tmp/  
COPY /sis/html/ /var/www/  
COPY /sis/xtreamcodes_pro_panel /etc/init.d/  
  
EXPOSE 8000  
EXPOSE 2200  
CMD ["/bin/sh"]  

