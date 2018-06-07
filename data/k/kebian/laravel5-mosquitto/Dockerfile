FROM kebian/laravel5  
MAINTAINER robs@codexsoftware.co.uk  
  
ADD http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key /root/  
ADD http://repo.mosquitto.org/debian/mosquitto-jessie.list
/etc/apt/sources.list.d/  
RUN apt-key add /root/mosquitto-repo.gpg.key  
  
RUN apt-get update && apt-get install -y libmosquitto1  
  
ADD mosquitto.so /usr/lib/php5/20131226/  
ADD mosquitto.ini /etc/php5/mods-available/  
  
RUN ln -s /etc/php5/mods-available/mosquitto.ini /etc/php5/cli/conf.d/  
RUN ln -s /etc/php5/mods-available/mosquitto.ini /etc/php5/fpm/conf.d/  

