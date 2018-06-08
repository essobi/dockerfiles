FROM ubuntu:trusty  
  
ADD https://downloads.plex.tv/plex-media-
server/0.9.15.6.1714-7be11e1/plexmediaserver_0.9.15.6.1714-7be11e1_amd64.deb /  
#ADD plexmediaserver_0.9.15.6.1714-7be11e1_amd64.deb /  
RUN dpkg -i plexmediaserver_0.9.15.6.1714-7be11e1_amd64.deb && rm
plexmediaserver_0.9.15.6.1714-7be11e1_amd64.deb  
  
EXPOSE 32400  
VOLUME /var/lib/plexmediaserver /media /usr/sbin/plexmediaserver  
  
CMD /usr/sbin/start_pms

