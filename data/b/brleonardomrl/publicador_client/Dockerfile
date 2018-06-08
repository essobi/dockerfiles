FROM ubuntu:latest  
  
MAINTAINER TMMIDIA  
  
# Instalando bibliotecas na nova imagem  
RUN apt-get update && apt-get install -y \  
sudo \  
nano \  
apt-utils \  
iputils-ping \  
curl \  
wget \  
git \  
apache2 \  
apache2-doc \  
apache2-utils \  
php7.0 \  
php7.0-fpm \  
libapache2-mod-php7.0 \  
php7.0-cli \  
php7.0-curl \  
php7.0-gd \  
php7.0-json \  
php7.0-mysql \  
php7.0-mbstring \  
php7.0-intl \  
php-gettext  
  
RUN sudo a2enmod rewrite  
  
RUN cd /etc/apache2 && sed -i '155s/None/All/' apache2.conf && sed -i
'160s/None/All/' apache2.conf && sed -i '166s/None/All/' apache2.conf  
  
# Expondo / habilitando a imagem para escutar na porta 80  
EXPOSE 80 3001 4200 9000 9060  
  
# Comandos que executam ao iniciar um container com esta imagem  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

