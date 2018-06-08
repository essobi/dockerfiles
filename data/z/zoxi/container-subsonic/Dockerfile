# Builds docker image for subsonic  
FROM zoxi/container-debian:latest  
  
RUN apt-get -q update && apt-get -qy install lame flac openjdk-7-jre-headless
ffmpeg  
RUN apt-get clean  
  
# Version de Subsonic  
ENV SUBSONIC_VERSION 6.0  
# Installation de Subsonic  
RUN wget
http://downloads.sourceforge.net/project/subsonic/subsonic/$SUBSONIC_VERSION/subsonic-$SUBSONIC_VERSION.deb
-O /tmp/subsonic.deb  
RUN dpkg -i /tmp/subsonic.deb && rm /tmp/subsonic.deb  
  
# Ports  
EXPOSE 4050  
# Montage des volumes  
VOLUME /subsonic  
VOLUME /music  
  
# Ajout des droits à "/subsonic"  
RUN chown -R nobody:users /subsonic  
  
# Ajout du script de démarrage  
ADD start.sh /start.sh  
RUN chmod +x /*.sh  
  
# Passage en user "nobody"  
USER nobody  
  
ENTRYPOINT ["/start.sh"]  

