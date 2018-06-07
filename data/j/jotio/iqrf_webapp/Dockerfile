FROM debian:latest  
  
MAINTAINER Vojtěch Novák <vojta.novak@jotio.tech>  
LABEL maintainer="vojta.novak@jotio.tech"  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y composer git php7.0
php7.0-common php7.0-curl php7.0-fpm php7.0-json php7.0-mbstring php7.0-sqlite
php7.0-zip unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/www/iqrf-daemon-webapp  
  
RUN composer create-project iqrfsdk/iqrf-daemon-webapp .  
RUN sed -i 's/sudo\:\ true/sudo\:\ false/g' app/config/config.neon  
RUN sed -i "s/initDaemon: 'systemd'/initDaemon: 'docker'/g"
app/config/config.neon  
  
CMD [ "php", "-S", "[::]:8080", "-t", "/var/www/iqrf-daemon-webapp/www" ]  
  
EXPOSE 8080  

