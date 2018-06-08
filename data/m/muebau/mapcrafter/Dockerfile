FROM ubuntu:17.04  
MAINTAINER muebau <hb1c@gmx.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /  
  
VOLUME ["/config"]  
VOLUME ["/output"]  
VOLUME ["/world"]  
  
RUN apt-get update && \  
apt-get -y install python curl wget apt-transport-https cron imagemagick&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "deb https://packages.mapcrafter.org/ubuntu zesty main" | tee
"/etc/apt/sources.list.d/mapcrafter.list" && \  
wget -O "/etc/apt/trusted.gpg.d/mapcrafter.gpg"
"https://packages.mapcrafter.org/ubuntu/keyring.gpg"  
  
RUN apt-get update && \  
apt-get -y install mapcrafter && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD crontab /etc/cron.d/mapcrafter-cron  
RUN chmod 0644 /etc/cron.d/mapcrafter-cron  
RUN touch /var/log/cron.log  
  
ADD render.sh /render  
RUN chmod 0777 /render  
ADD render.conf /  
  
CMD cron && tail -f /var/log/cron.log  

