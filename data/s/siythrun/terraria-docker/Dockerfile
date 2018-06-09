FROM debian:7  
MAINTAINER Siythrun  
# Size of the map  
# 1: small  
# 2: normal  
# 3: big  
ENV TERRARIA_WORLD_SIZE 3  
# Name of your server  
ENV TERRARIA_WORLD_NAME terraria  
# Nb max players  
ENV TERRARIA_PLAYERS_MAX 10  
# Add mono repository  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/4.0.0
main" | tee /etc/apt/sources.list.d/mono-official.list  
  
# Update and install mono and a zip utility  
RUN apt-get update && apt-get install -y \  
zip \  
mono-complete && \  
apt-get clean  
  
# Run commands as the steam user  
RUN adduser \  
\--disabled-login \  
\--shell /bin/bash \  
\--gecos "" \  
terraria  
  
RUN mkdir /tshock /terraria && chown terraria /tshock /terraria  
  
# Download the latest version of TShock  
#ADD https://api.github.com/repos/NyxStudios/TShock/zipball/ /tmp/tshock.zip  
# can't use api github because there is an api limit  
ADD
https://github.com/Pryaxis/TShock/releases/download/v4.3.24/tshock_4.3.24.zip
/tmp/tshock.zip  
RUN unzip -d /tshock /tmp/tshock.zip  
# Allow to save default plugin and add them when we mount ServerPlugins  
RUN cp -r /tshock/ServerPlugins /tshock/DefaultServerPlugins  
  
# Add bash file  
ADD terraria.sh /etc/terraria.sh  
  
RUN chown -R terraria /tshock  
RUN chown -R terraria /terraria  
RUN chown -R terraria /etc/terraria.sh  
RUN chmod 755 -R /tshock  
RUN chmod 755 -R /terraria  
RUN chmod 755 -R /etc/terraria.sh  
  
# Allow for external data  
VOLUME /terraria  
VOLUME /tshock/ServerPlugins  
  
# 7777 : Game port  
# 7878 : REST port  
EXPOSE 7777 7878  
# Set working directory to server  
WORKDIR /tshock  
  
USER terraria  
  
# run the server  
CMD /etc/terraria.sh  

