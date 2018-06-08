FROM eclipse/dotnet_core  
ENV LUNA_HOME LMPServerUpdater  
ENV LMP_URL
https://github.com/LunaMultiplayer/LunaMultiplayerUpdater/releases/download/1.0.0/LunaMultiplayerUpdater-
Release.zip  
ENV LMP_EXE Server.exe  
ENV LMP_UPDATER ServerUpdater.exe  
RUN sudo apt-get update && sudo apt-get install zip  
RUN sudo wget $LMP_URL \  
&& sudo unzip LunaMultiplayerUpdater-Release.zip \  
&& sudo mkdir -p $LUNA_HOME/logs  
EXPOSE 8800/udp  
EXPOSE 8801/udp  
WORKDIR $LUNA_HOME  
RUN sudo touch $LMP_EXE  
RUN sudo mono $LMP_UPDATER  
CMD ["mono", "$LMP_EXE"]  

