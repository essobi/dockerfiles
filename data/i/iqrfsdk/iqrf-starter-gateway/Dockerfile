# IQRF GW image for the UP board  
# Authors: JotioTech s.r.o. && IQRFTech s.r.o.  
FROM resin/up-board-debian:stretch  
  
MAINTAINER Rostislav Spinar <rostislav.spinar@iqrf.com>  
LABEL maintainer="rostislav.spinar@iqrf.com"  
  
# add iqrf repo  
RUN echo "deb http://repos.iqrfsdk.org/debian stretch stable" | sudo tee -a
/etc/apt/sources.list.d/iqrf-daemon.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
9C076FCC7AB8F2E43C2AB0E73241B9B7B4BD8F8E  
  
# install supervisor && mosquitto && iqrf-daemon && php && nginx && node.js  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y apt-utils apt-transport-https
build-essential composer curl git iqrf-daemon lsb-release mosquitto php7.0
php7.0-common php7.0-curl php7.0-fpm php7.0-json php7.0-mbstring php7.0-sqlite
php7.0-zip nginx-full supervisor unzip wget \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install --no-install-recommends -y nodejs \  
&& mkdir -p /var/run/sshd /var/log/supervisor \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# install iqrf-webapp  
WORKDIR /var/www/iqrf-daemon-webapp  
RUN composer create-project iqrfsdk/iqrf-daemon-webapp . dev-master \  
&& sed -i 's/sudo\:\ true/sudo\:\ false/g' app/config/config.neon \  
&& sed -i 's/iqrf-gw\:\ false/iqrf-gw\:\ true/g' app/config/config.neon \  
&& sed -i "s/initDaemon: 'systemd'/initDaemon: 'docker-supervisor'/g"
app/config/config.neon \  
&& chmod 777 log/ \  
&& chmod 777 temp/  
  
# setup php-fpm  
RUN mkdir /run/php/ \  
&& sed -i 's/user\ =\ www-data/user\ =\ root/g'
/etc/php/7.0/fpm/pool.d/www.conf \  
&& sed -i 's/group\ =\ www-data/group\ =\ root/g'
/etc/php/7.0/fpm/pool.d/www.conf  
  
# install node-red dashboard  
RUN npm install -g --unsafe-perm node-red \  
&& npm install -g --unsafe-perm node-red/node-red-dashboard  
  
# copy custom configuration  
WORKDIR /etc/nginx/sites-available  
COPY config/nginx/localhost .  
RUN ln -s /etc/nginx/sites-available/localhost /etc/nginx/sites-
enabled/localhost \  
&& rm /etc/nginx/sites-enabled/default  
WORKDIR /etc/supervisor/conf.d  
COPY config/supervisor/supervisord.conf .  
WORKDIR /etc/iqrf-daemon  
COPY config/iqrf-daemon/. .  
RUN mkdir -p /node-red  
WORKDIR /node-red  
COPY config/node-red/. .  
  
# expose ports  
EXPOSE 80 1880 1883 8080 9001 55000/udp 55300/udp  
  
# run the supervisor service  
CMD ["/usr/bin/supervisord"]  

