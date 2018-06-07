FROM maven:3.5.2-jdk-8  
MAINTAINER Yoann Vanitou <yvanitou@gmail.com>  
  
# Déclaration des variables d'envoronement  
ENV DEBIAN_FRONTEND noninteractive  
ENV KEYBOX_VERSION 2.90.03  
# Téléchargement du package  
RUN wget -qO-
https://github.com/skavanagh/KeyBox/archive/v"$KEYBOX_VERSION".tar.gz | tar
-xvz -C /tmp  
  
# Installation du package  
RUN cd /tmp \  
&& mv -v /tmp/KeyBox-"$KEYBOX_VERSION" /opt/keybox  
  
# Copie le nouveau executable  
COPY ./keybox.sh /opt/keybox/keybox.sh  
  
# Permission  
RUN chmod +x /opt/keybox/keybox.sh  
  
RUN mkdir -vp /opt/keybox/target/classes/keydb  
  
# Expose le port  
EXPOSE 8443/tcp  
  
# Déclaration du volume  
VOLUME ["/opt/keybox/target/classes/keydb"]  
  
# Répertoire par défaut  
WORKDIR /opt/keybox  
  
# Execute le programme  
CMD ["/opt/keybox/keybox.sh"]  

