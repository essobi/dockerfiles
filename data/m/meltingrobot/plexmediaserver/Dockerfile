# Version 0.0.1  
FROM fedora:latest  
MAINTAINER Roy P "meltingrobot@gmail.com"  
RUN echo "[PlexRepo]" > /etc/yum.repos.d/plex.repo  
RUN echo "name=PlexRepo" >> /etc/yum.repos.d/plex.repo  
RUN echo "baseurl=https://downloads.plex.tv/repo/rpm/x86_64/" >>
/etc/yum.repos.d/plex.repo  
RUN echo "enabled=1" >> /etc/yum.repos.d/plex.repo  
RUN echo "gpgkey=https://downloads.plex.tv/plex-keys/PlexSign.key" >>
/etc/yum.repos.d/plex.repo  
RUN echo "gpgcheck=1" >> /etc/yum.repos.d/plex.repo  
RUN dnf -y update  
RUN dnf -y install plexmediaserver  
CMD [ "/bin/bash", "-c", "PLEX_MEDIA_SERVER_HOME=/usr/lib/plexmediaserver
LD_LIBRARY_PATH=/usr/lib/plexmediaserver /usr/lib/plexmediaserver/Plex\ Media\
Server" ]  
EXPOSE 32400/tcp 3005/tcp 8324/tcp 32469/tcp 1900/udp 32410/udp 32412/udp
32413/udp 32414/udp  

