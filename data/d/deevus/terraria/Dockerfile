FROM mono:4.6.2  
MAINTAINER Simon Hartcher <simon@simonhartcher.com>  
  
# fix for favorites.json error  
RUN favorites_path="/root/My Games/Terraria" && mkdir -p "$favorites_path" &&
echo "{}" > "$favorites_path/favorites.json"  
  
# Download and install TShock  
ENV TSHOCK_VERSION=4.3.20 \  
TSHOCK_FILE_POSTFIX=""  
ENV SERVER_PARAMS ""  
ADD https://github.com/NyxStudios/TShock/releases/download/mintaka-
pre2-4.3.21-2.0-2.0.0.15/TShock_mintaka_prere_2.zip tshock.zip  
RUN apt-get update -q && apt-get install unzip -yq  
RUN unzip tshock.zip -d /tshock && \  
rm tshock.zip && \  
chmod 777 /tshock/TerrariaServer.exe  
  
# Allow for external data  
VOLUME ["/world", "/tshock/ServerPlugins", "/config", "/logs"]  
  
# Set working directory to server  
WORKDIR /tshock  
  
# run the server  
EXPOSE 7777  
ENTRYPOINT ["mono", "--server", "--gc=sgen", "-O=all", "TerrariaServer.exe",
"-configpath", "/config", "-worldpath", "/world", "-logpath", "/logs",
"$SERVER_PARAMS"]  

