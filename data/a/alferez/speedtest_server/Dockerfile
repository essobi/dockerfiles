FROM debian:8  
MAINTAINER Jose A Alferez <correo@alferez.es>  
  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#### Configure TimeZone  
RUN echo "Europe/Madrid" > /etc/timezone  
RUN dpkg-reconfigure tzdata  
  
#### Instalamos dependencias, Repositorios y Paquetes  
RUN echo "deb http://httpredir.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list  
RUN apt-get update -y --fix-missing  
RUN apt-get -y upgrade  
  
RUN apt-get install -y --fix-missing wget curl nano apache2 apache2-mpm-
prefork libapache2-mod-php5 php5-cli php5  
  
#### Configuramos Apache  
RUN a2enmod cgi  
RUN a2enmod rewrite  
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf  
RUN ln -s /etc/apache2/conf-available/fqdn.conf /etc/apache2/conf-
enabled/fqdn.conf  
  
RUN mkdir /speedtest  
WORKDIR /speedtest  
RUN wget http://install.speedtest.net/ooklaserver/ooklaserver.sh  
RUN chmod a+x /speedtest/ooklaserver.sh  
RUN /speedtest/ooklaserver.sh install -f  
  
EXPOSE 80  
EXPOSE 8080  
EXPOSE 5060  
RUN apt-get install -y --fix-missing zip unzip  
  
WORKDIR /var/www/html  
RUN wget http://cdn.speedtest.speedtest.net/http_legacy_fallback.zip  
RUN unzip http_legacy_fallback.zip  
RUN mv /var/www/html/speedtest/* /var/www/html/  
RUN rm -rf /var/www/html/speedtest  
RUN rm http_legacy_fallback.zip  
COPY ./assets/crossdomain.xml /var/www/html/crossdomain.xml  
COPY ./assets/OoklaServer.properties /speedtest/OoklaServer.properties  
  
### Limpiamos  
RUN apt-get clean  
RUN rm -rf /tmp/* /var/tmp/*  
RUN rm -rf /var/lib/apt/lists/*  
  
### Add Entrypoing  
ADD ./assets/start.sh /start.sh  
RUN chmod +x /start.sh  
  
WORKDIR /root  
  
ENTRYPOINT "/start.sh"  
  

