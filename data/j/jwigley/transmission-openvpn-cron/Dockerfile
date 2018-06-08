FROM haugene/transmission-openvpn:latest  
  
RUN apt-get update \  
&& apt-get install -y python \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD torrentcontrol /usr/bin/  
  
ADD default-cron /etc/cron.d/torrent-sched-cron  
  
ADD start.sh /etc/start.sh  
  
CMD ["dumb-init", "/etc/start.sh"]  
  

