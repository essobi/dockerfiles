FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# get dependencies  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y \  
wget \  
lib32gcc1 && \  
rm -rf /var/lib/apt/lists/*  
  
# Install steam  
RUN mkdir -p /opt/steamcmd && \  
$( \  
cd /opt/steamcmd && \  
wget https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz &&
\  
tar -xf steamcmd_linux.tar.gz && \  
rm steamcmd_linux.tar.gz \  
) && \  
yes exit | /opt/steamcmd/steamcmd.sh  
  
  
# Install game server  
RUN mkdir -p /opt/citadel && \  
/opt/steamcmd/steamcmd.sh \  
+login anonymous \  
+force_install_dir /opt/citadel \  
+app_update 489650 validate \  
+quit  
  
# post install  
RUN cp /opt/steamcmd/linux64/steamclient.so \  
/opt/citadel/Citadel/Plugins/UWorks/Source/ThirdParty/Linux/steamclient.so &&\  
adduser --disabled-password --gecos "" steamserver && \  
chown -R steamserver:steamserver /opt/citadel  
  
# Docker Environment  
USER steamserver  
WORKDIR /home/steamserver  
  
EXPOSE 27015  
EXPOSE 7777  
CMD /opt/citadel/Citadel/Binaries/Linux/CitadelServer-Linux-Shipping
-nosteamclient -server -log  
  

