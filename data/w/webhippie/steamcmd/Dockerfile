FROM webhippie/ubuntu:precise  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
CMD ["bash"]  
  
ADD rootfs /  
  
RUN groupadd -r steam && \  
useradd \  
-r -d /home/steam -g steam steam && \  
apt-get \  
update && \  
apt-get install -y \  
lib32gcc1 && \  
apt-get \  
clean && \  
mkdir -p \  
/home/steam && \  
curl \  
http://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz \  
| tar -C /home/steam -xzf - && \  
chown -R steam:steam \  
/home/steam && \  
steamcmd \  
+login anonymous +quit && \  
rm -f \  
/home/steam/Steam/logs/*  
  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.version=$VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/dockhippie/steamcmd.git"  
LABEL org.label-schema.name="SteamCMD"  
LABEL org.label-schema.vendor="Thomas Boerger"  
LABEL org.label-schema.schema-version="1.0"  

