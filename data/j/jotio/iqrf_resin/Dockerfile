#IQRF GW daemon image for the UP board  
FROM resin/up-board-debian:stretch  
  
MAINTAINER Vojtěch Novák <vojta.novak@jotio.tech>  
LABEL maintainer="vojta.novak@jotio.tech"  
  
# update repos  
RUN echo "deb http://repos.iqrfsdk.org/debian stretch testing" | sudo tee -a
/etc/apt/sources.list.d/iqrf-daemon.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F973CFCE6B3BE25C  
  
# install daemon  
RUN apt-get update \  
&& apt-get install -y supervisor \  
&& apt-get install -y iqrf-daemon \  
&& mkdir -p /var/run/sshd /var/log/supervisor \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# install webapp  
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
  
# install nodered  
RUN apt-get update && \  
apt-get install -y apt-utils  
RUN apt-get install -y wget curl unzip build-essential i2c-tools golang python
python-pip  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g --unsafe-perm node-red  
RUN npm install --prefix /node-red/.node-red node-red-contrib-i2c node-red-
contrib-influxdb ina226  
  
ADD settings.js /node-red/  
ADD flows.json /node-red/.node-red/  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
# copy custom configuration  
# udp ports for iqrf ide  
EXPOSE 9001 80 8080 55000/udp 55300/udp  
  
# run the daemon service  
CMD ["/usr/bin/supervisord"]  

