# Image: deltatrees/docker-ftbserver  
# Offical ubuntu base image  
FROM dockerfile/java:openjdk-7-jre  
MAINTAINER DeltaTrees <admin@deltatrees.de>  
  
# Update and install  
RUN apt-get update  
  
ENV MODPACK_NAME direwolf20_17  
ENV MODPACK_VERSION 1_0_3  
ENV MODPACK_FILE direwolf20_17-server.zip  
  
RUN mkdir /ftb  
WORKDIR /ftb  
RUN wget
http://ftb.cursecdn.com/FTB2/modpacks/$MODPACK_NAME/$MODPACK_VERSION/$MODPACK_FILE
\  
&& unzip * \  
&& rm $MODPACK_FILE  
  
COPY eula.txt server.properties ServerStart.sh /ftb/  
RUN chmod +x ServerStart.sh  
  
RUN sh FTBInstall.sh  
  
VOLUME ["/ftb/world", "/ftb/logs"]  
  
EXPOSE 25565  
CMD ["/bin/bash", "/ftb/ServerStart.sh"]  

