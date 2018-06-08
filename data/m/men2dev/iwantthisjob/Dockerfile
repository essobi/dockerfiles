FROM ubuntu:16.04  
  
#Actualizacion del sistema e instalacion de paquetes necesarios para php,
apache y composer  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends netcat net-tools curl git vim
zip unzip php-zip \  
&& apt-get install -y --no-install-recommends apache2 php libapache2-mod-php
php-xml php-mysql composer  
  
# Definir variables de entorno para el arranque de apache y la ejecucion de
composer  
  
ARG APACHE_PORT  
  
ENV APACHE_RUN_USER=default \  
APACHE_RUN_GROUP=root \  
APACHE_LOG_DIR=/var/log/apache2 \  
APACHE_LOCK_DIR=/var/lock/apache \  
APACHE_PID_FILE=/var/run/apache.pid \  
APACHE_PORT=${APACHE_PORT:-8888} \  
SYMFONY_ENV=prod  
  
# Clonado del repositorio de codigo, copia del codigo de backend al
documentroot de apache  
# Copia de el script de arranque de apache y de su configuracion  
RUN cd /tmp \  
&& git clone https://github.com/men2dev/iwantthisjob.git \  
&& cd iwantthisjob \  
&& cp httpd-foreground /etc/apache2/ \  
&& cp -R www/backend/* /var/www/html/ \  
&& cp 000-default.conf /etc/apache2/sites-available \  
&& cd / \  
&& rm -Rf /tmp/iwantthisjob  
  
# Cambios de permisos para poder ejecutar apache con un usuario diferente de
root (recomendación de seguridad)  
# Configuracion de Listen port de apache y redireccion de logs al stdout  
RUN chmod -R a+rwx /var/run/apache2 \  
&& chmod -R a+rwx /var/lock/apache2 \  
&& chown -R 1001:0 /etc/apache2 \  
&& chmod -R ug+rwx /etc/apache2 \  
&& chmod 755 /etc/apache2/httpd-foreground \  
&& a2enmod rewrite \  
&& a2enmod headers \  
&& phpenmod pdo_mysql \  
&& sed -i 's/Listen 80/Listen ${APACHE_PORT}/g' /etc/apache2/ports.conf \  
&& find /etc/apache2 -type f -print0 | xargs -0 sed -i "s/ErrorLog.*/ErrorLog
\/dev\/stdout/g" \  
&& find /etc/apache2 -type f -print0 | xargs -0 sed -i
"s/CustomLog.*/CustomLog \/dev\/stdout combined/g"  
  
# Ejecucion del composer para resolver las dependencias del proyecto  
# Cambio de permisos de los directorios del proyecto para que el usuario 1001
pueda escribir en la cache  
RUN cd /var/www/html/api \  
&& composer install --no-dev --optimize-autoloader \  
&& chown -R 1001:0 /var/www/html/api \  
&& chmod -R g+w /var/www/html/api  
  
#Se expone el puerto de apache configurado  
EXPOSE ${APACHE_PORT}  
  
USER 1001  
  
ENTRYPOINT ["/etc/apache2/httpd-foreground"]  
  

