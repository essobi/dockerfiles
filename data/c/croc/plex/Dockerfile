FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y net-tools unzip less tar vim curl  
  
RUN curl -L -o /tmp/plex.deb "https://downloads.plex.tv/plex-media-
server/1.10.1.4602-f54242b6b/plexmediaserver_1.10.1.4602-f54242b6b_amd64.deb"
&& dpkg -i /tmp/plex.deb  
  
COPY files/start.sh /opt/start.sh  
RUN chmod 755 /opt/start.sh  
  
# not necessary for templates  
ENTRYPOINT /opt/start.sh  
#ENTRYPOINT /bin/bash  

