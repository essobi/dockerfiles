FROM it2use/sparkle:base  
  
ENV SPARKLE_IMAGE=barrier  
  
#*******************************************************************************  
RUN apt-get install --force-yes -qy apt-cacher-ng  
  
#*******************************************************************************  
WORKDIR /beacon/srv/$SPARKLE_IMAGE  
  
RUN mkdir -p /srv/ftp /srv/nfs /srv/afp /srv/samba  
  
#*******************************************************************************  
VOLUME /var/cache/apt-cacher-ng  
  
EXPOSE 53  
EXPOSE 3124  
EXPOSE 3142  

