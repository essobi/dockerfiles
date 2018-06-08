# Builds docker image for minidlna  
FROM zoxi/container-debian:latest  
  
MAINTAINER zoxi  
  
# Installation des prérequis  
RUN apt-get install -qy curl  
  
# Installation de btsync  
RUN mkdir -p /opt/btsync  
RUN curl -s -k -L "https://download-
cdn.getsyncapp.com/stable/linux-x64/BitTorrent-Sync_x64.tar.gz" | tar -xzf -
-C /opt/btsync  
  
# Ajout du script de configuration  
#ADD btsync.conf /tmp/btsync.conf  
ADD config.sh /config.sh  
RUN chmod +x /*.sh && \  
/bin/bash /config.sh  
  
# Montage des volumes  
VOLUME /config  
VOLUME /sync  
  
# Ajout des droits à "/opt/btsync"  
RUN chown -R nobody:users /opt/btsync /config  
RUN chmod -R 775 /opt/btsync /config  
  
# Ajout du script de démarrage  
ADD start.sh /start.sh  
RUN chmod +x /*.sh  
  
# Passage en user "nobody"  
USER nobody  
  
ENTRYPOINT ["/start.sh"]  

