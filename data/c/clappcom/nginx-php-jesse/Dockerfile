# Itt választjuk ki, hogy melyik legyen az alap image fájl, amire szeretnénk
építeni  
FROM nginx:1.11.10  
# Ezt szerintem ne változtassuk  
MAINTAINER CLAPP hi@clapp.eu  
  
# Frissítjük az apt-get-et és telepítjuk a php7.1-FPM-et és még egy jópár
dolgot. Ide kell felvenni ha esetleg még kell valamilyen PHP extension.  
RUN apt-get update \  
&& apt-get install -y wget \  
&& apt-get install -y apt-transport-https lsb-release ca-certificates \  
&& wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list \  
&& apt-get update && apt-get install -y php7.1-fpm php7.1-mcrypt
php7.1-mbstring php7.1-mysql php7.1-gd php7.1-zip php7.1-xml \  
&& apt-get install -y vim  
  
  
# Pár konfigutáció, amit elvégzünk. Ezzel érdemes a config fájlokat
módosítani, de meg kell majd próbálni ha csak simán felülírjuk őket egy saját
fájlal, amiben csak a változtatni kívánt paraméterek vannak, akkor működik-e.  
  
RUN sed -i -e "s@;cgi.fix_pathinfo=1@cgi.fix_pathinfo=0@g"
/etc/php/7.1/fpm/php.ini && \  
sed -i -e "s@listen = /run/php/php7.1-fpm.sock@listen = 127.0.0.1:9000@g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s@;clear_env\s*=\s*no@clear_env = no@g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s@upload_max_filesize\s*=\s*2M@upload_max_filesize = 100M@g"
/etc/php/7.1/fpm/php.ini && \  
sed -i -e "s@post_max_size\s*=\s*8M@post_max_size = 100M@g"
/etc/php/7.1/fpm/php.ini && \  
sed -i -e "s@;daemonize\s*=\s*yes@daemonize = no@g" /etc/php/7.1/fpm/php-
fpm.conf && \  
sed -i -e "s@;catch_workers_output\s*=\s*yes@catch_workers_output = yes@g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s@pm.max_children = 5@pm.max_children = 9@g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s@pm.start_servers = 2@pm.start_servers = 3@g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s@pm.min_spare_servers = 1@pm.min_spare_servers = 2@g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s@pm.max_spare_servers = 3@pm.max_spare_servers = 4@g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s@pm.max_requests = 500@pm.max_requests = 200@g"
/etc/php/7.1/fpm/pool.d/www.conf  
  
# PID file-t ilyenkor hozza létre, erre később nem lenne joga.  
RUN service php7.1-fpm start  
  
# átmásoljuk a vhost.conf fájlunk, hogy az NGINX tudja használni.  
COPY vhosts /vhosts  
  
# Ez pedig már a legvége, itt állítjuk be, hogy milyen legyen az a script, ami
a docker run parancsnál lefut.  
  
ADD scripts/start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# 80-as portot fogjuk használni  
EXPOSE 80  
#Ezzel fut le a start.sh script. /bin/bash futtatja a /start.sh scriptet.  
CMD ["/bin/bash", "/start.sh"]  

