FROM busybox  
  
RUN mkdir -p /music /playlist /syncthing /var/lib/mpd  
  
RUN chmod 777 /music /playlist  
RUN chown 800:800 /syncthing  
RUN chown 105:107 /var/lib/mpd  
  
VOLUME /music  
VOLUME /playlist  
VOLUME /syncthing  
VOLUME /var/lib/mpd  
  
CMD ["true"]  

