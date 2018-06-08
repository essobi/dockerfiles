FROM debian:9.1  
MAINTAINER Adam Zheng adam.w.zheng@icloud.com  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV MOODLE_RELEASE MOODLE_34_STABLE  
ENV S6_RELEASE 1.21.4.0  
#Add S6 Overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v$S6_RELEASE/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xvfz /tmp/s6-overlay-amd64.tar.gz -C /  
  
#Install Moodle Required Packages  
RUN apt-get update \  
&& apt-get install nginx -y \  
&& apt-get install php7.0-fpm php7.0-xml php7.0-pgsql php7.0-mysql php7.0-curl
php7.0-zip php7.0-gd php7.0-mbstring php7.0-xmlrpc php7.0-soap php7.0-intl -y
\  
&& apt-get install git -y \  
&& apt-get install cron -y  
  
#Clone Moodle  
RUN rm -v /var/www/html/index.nginx-debian.html \  
&& git clone \--depth=1 -b $MOODLE_RELEASE git://git.moodle.org/moodle.git
/var/www/html/ \  
&& chown -R www-data:www-data /var/www/html \  
&& mkdir -p /var/www/moodledata  
  
#Configure webserver as per Moodle Docs  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& sed -i 's/index index.html index.htm index.nginx-debian.html;/\tindex
index.html index.htm index.php/g;' /etc/nginx/sites-enabled/default \  
&& sed -i 's/#location ~ \\\\.php\$ {/location ~ [^\/]\\\\.php(\/|\$)
{\n\t\tfastcgi_split_path_info ^(.+\\\\.php)(\/.+)\$;/g' /etc/nginx/sites-
enabled/default \  
&& sed -i 's=#\tinclude snippets/fastcgi-php.conf;=\n\t\tinclude
fastcgi_params;=g' /etc/nginx/sites-enabled/default \  
&& sed -i 's=#\tfastcgi_pass unix:/var/run/php/php7.0-fpm.sock;=\tfastcgi_pass
unix:/var/run/php/php7.0-fpm.sock;\n\t\tfastcgi_param PATH_INFO
\$fastcgi_path_info;\n\t\tfastcgi_param SCRIPT_FILENAME
\$document_root\$fastcgi_script_name;\n\t}=g' /etc/nginx/sites-enabled/default
\  
&& sed -i -e '/With php-cgi (or other tcp sockets):/,+2d' /etc/nginx/sites-
enabled/default  
  
#Redirect NGINX Logs  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
#Add Service NGINX to be Monitored by S6  
RUN mkdir -p /etc/services.d/nginx/ \  
&& touch /etc/services.d/nginx/run \  
&& echo '#!/usr/bin/execlineb -P' > /etc/services.d/nginx/run \  
&& echo 'nginx' >> /etc/services.d/nginx/run  
  
#Add Service PHP-FPM to be Monitored by S6  
RUN mkdir -p /etc/services.d/php7.0-fpm/ \  
&& touch /etc/services.d/php7.0-fpm/run \  
&& echo '#!/usr/bin/execlineb -P' > /etc/services.d/php7.0-fpm/run \  
&& echo 'service php7.0-fpm start' >> /etc/services.d/php7.0-fpm/run  
  
#Add Service Cron to be Monitored by S6  
RUN mkdir -p /etc/services.d/cron/ \  
&& touch /etc/services.d/cron/run \  
&& echo '#!/usr/bin/execlineb -P' > /etc/services.d/cron/run \  
&& echo 'exec /usr/sbin/cron cron -f' >> /etc/services.d/cron/run  
  
#Copy the Moodle CLI Install Script into the Container to be executed on
startup  
COPY install-moodle.sh /etc/cont-init.d/  
RUN chmod u+x /etc/cont-init.d/install-moodle.sh  
  
ENTRYPOINT ["/init"]  

