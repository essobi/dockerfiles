# Dockerfile for a TShock Terraria Server  
# https://github.com/kalhartt/docker-tshock  
FROM mono:latest  
MAINTAINER asimonf <alberto@simon.ph>  
  
# Install unzip package  
RUN apt-get -qq update && \  
apt-get -qqy install unzip  
  
# Download and setup TShock  
RUN curl -sL https://github.com/NyxStudios/TShock/releases/download/mintaka-
pre1-4.3.21-1.26-2.0.0.9/tshock_mintaka_prere_1.zip > /tmp/tshock.zip && \  
unzip /tmp/tshock.zip -d /opt && \  
mv /opt/tshock* /opt/tshock-server  
  
COPY InfChests.dll /opt/tshock-server/ServerPlugins/InfChests.dll  
  
# Start the server and expose the port  
EXPOSE 7777 7878  
VOLUME /opt/tshock-server/tshock  
VOLUME /opt/tshock-server/Terraria/Worlds  
  
WORKDIR /opt/tshock-server  
ENTRYPOINT ["mono", "--server", "--gc=sgen", "-O=all", "TerrariaServer.exe"]  
CMD ["-world", "Terraria/Worlds/Default.wld", "-autocreate", "3"]  

