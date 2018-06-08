FROM java:7  
MAINTAINER Yoann Vanitou <yvanitou@gmail.com>  
  
# Déclaration des variables d'envoronement  
ENV DEBIAN_FRONTEND noninteractive  
ENV SUBSONIC_VERSION 5.3  
ENV RUN_USER subsonic  
ENV RUN_GROUP subsonic  
  
# Création de l'utilisateur  
RUN useradd --no-create-home --system --user-group ${RUN_USER}  
  
# Création des répertoires  
RUN mkdir -p /var/subsonic  
RUN mkdir -p /var/music  
RUN mkdir -p /var/playlists  
  
# Téléchargement du package  
ADD https://s3-eu-west-1.amazonaws.com/subsonic-
public/download/subsonic-$SUBSONIC_VERSION.deb /tmp/subsonic.deb  
  
# Installation du package  
RUN dpkg -i /tmp/subsonic.deb && rm /tmp/subsonic.deb  
  
# Backup executable  
RUN mv /usr/share/subsonic/subsonic.sh /usr/share/subsonic/subsonic-
original.sh  
  
# Copie le nouveau executable  
COPY ./subsonic.sh /usr/share/subsonic  
  
# Création des liens symboliques  
RUN ln -s /var/subsonic/transcode/ffmpeg /usr/local/bin  
RUN ln -s /var/subsonic/transcode/lame /usr/local/bin  
  
# Application des permissions  
RUN chown -R ${RUN_USER}:${RUN_GROUP} /var/subsonic && chmod 755 /var/subsonic  
RUN chown -R ${RUN_USER}:${RUN_GROUP} /var/music && chmod 755 /var/music  
RUN chown -R ${RUN_USER}:${RUN_GROUP} /var/playlists && chmod 755
/var/playlists  
  
# Expose les ports  
EXPOSE 4040 4443  
# Déclaration du volume  
VOLUME ["/var/subsonic"]  
  
# Répertoire par défaut  
WORKDIR /var/subsonic  
  
# Change d'utilisateur  
USER ${RUN_USER}  
  
# Execute le programme  
CMD ["/usr/bin/subsonic"]  

