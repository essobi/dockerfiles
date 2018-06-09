# Base system is the Raspian ARM image from Resin  
FROM resin/rpi-raspbian  
  
RUN [ "cross-build-start" ]  
  
# 25565 is for minecraft  
EXPOSE 25565  
# Make sure we don't get notifications we can't answer during building.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Java 8 & curl  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get --yes update && \  
apt-get --yes install \  
#software-properties-common \  
curl \  
oracle-java8-installer && \  
# CLEANUP  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Download latest Minecraft Server  
RUN mkdir /minecraft-server  
  
COPY start_minecraft.sh /opt/  
  
RUN echo "eula=true" > /data/eula.txt && chmod +x /opt/start_minecraft.sh  
  
CMD [ "/opt/start_minecraft.sh" ]  
  
RUN [ "cross-build-end" ]  

