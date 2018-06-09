FROM ubuntu:latest  
  
# Add mono repository  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo tee
/etc/apt/sources.list.d/mono-xamarin.list  
  
# Update and install mono and a zip utility  
RUN apt-get update && apt-get install -y \  
zip \  
mono-complete && \  
apt-get clean  
  
# fix for favorites.json error  
RUN favorites_path="/root/My Games/Terraria" && mkdir -p "$favorites_path" &&
echo "{}" > "$favorites_path/favorites.json"  
  
# Download and install TShock  
ENV TSHOCK_DEV_BUILD 557  
ENV TSHOCK_DEV_ZIP tshock_release.zip  
  
# World size: 1(small) 2(medium) 3(large)  
ENV WORLD_SIZE 1  
# Difficulty: 0(Normal) 1(Expert)  
ENV DIFFICULTY 0  
ADD http://direct.tshock.co:8085/browse/TERRA-
TSHOCK-$TSHOCK_DEV_BUILD/artifact/shared/$TSHOCK_DEV_ZIP/$TSHOCK_DEV_ZIP /  
RUN unzip $TSHOCK_DEV_ZIP -d /tshock  
RUN rm $TSHOCK_DEV_ZIP  
  
# Allow for external data  
VOLUME ["/world", "/tshock/ServerPlugins"]  
  
# Set working directory to server  
WORKDIR /tshock  
  
ADD execterraria.sh /execterraria.sh  
# Set permissions  
RUN chmod 777 TerrariaServer.exe  
RUN chmod +x /execterraria.sh  
  
# run the server  
CMD /execterraria.sh  

