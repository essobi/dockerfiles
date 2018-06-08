FROM centos:7  
MAINTAINER Tobias Germer  
  
# Environment variables  
ENV STEAM_USER=steam \  
STEAM_HOME=/steam \  
GAMES_HOME=/games  
  
# Install the dependencies required to run SteamCMD  
RUN yum install glibc.i686 libstdc++.i686 wget.x86_64 -y && \  
yum update -y  
  
# Add user to run steam and create directories for files  
RUN useradd -m $STEAM_USER && \  
mkdir $STEAM_HOME && \  
mkdir $GAMES_HOME  
  
# Download SteamCMD tarball  
RUN wget -P $STEAM_HOME
https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz  
  
# Extract the contents to the directory  
RUN tar -xvzf $STEAM_HOME/steamcmd_linux.tar.gz -C $STEAM_HOME/  
  
# Remove tarball  
RUN rm $STEAM_HOME/steamcmd_linux.tar.gz  
  
# Change owner rights  
RUN chown -R $STEAM_USER:$STEAM_USER $STEAM_HOME $GAMES_HOME  
  
# Update Steam once  
RUN $STEAM_HOME/steamcmd.sh +quit  
  
# Bypass union filesystem for games  
VOLUME $GAMES_HOME  
  
# Use Steam home as workdir  
WORKDIR $STEAM_HOME  
  
# Set user for running steam  
USER $STEAM_USER  
  
# Start SteamCMD when running a container without parameters  
CMD $STEAM_HOME/steamcmd.sh +force_install_dir $GAMES_HOME +login anonymous  

