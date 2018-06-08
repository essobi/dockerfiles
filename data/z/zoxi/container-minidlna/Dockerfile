# Builds docker image for minidlna  
FROM zoxi/container-debian:latest  
  
MAINTAINER zoxi  
  
# Installation de minidlna  
RUN apt-get -q update && apt-get -qy install minidlna  
RUN apt-get clean  
  
# Ajout du script de configuration  
ADD config.sh /config.sh  
RUN chmod +x /*.sh && \  
/bin/bash /config.sh  
  
# Montage des volumes  
VOLUME /config  
VOLUME /media  
  
# Ajout des droits à "/minidlna"  
RUN chown -R nobody:users /usr/bin/minidlna  
RUN chmod -R 775 /usr/bin/minidlna  
  
# Ajout du script de démarrage  
ADD start.sh /start.sh  
RUN chmod +x /*.sh  
  
# Passage en user "nobody"  
USER nobody  
  
ENTRYPOINT ["/start.sh"]  

