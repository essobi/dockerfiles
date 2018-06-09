FROM mono:5.8  
  
MAINTAINER Hexer <hexrhj@gmail.com>  
  
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
# echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo
tee /etc/apt/sources.list.d/mono-xamarin.list && \  
# apt-get update && apt-get install -y \  
# mono-complete && \  
# apt-get clean  
  
RUN apt-get update && \  
apt-get install -y \  
zip \  
wget && \  
wget -P / http://terraria.org/server/terraria-server-1352.zip && \  
wget -P /
https://github.com/blushiemagic/tModLoader/releases/download/v0.10.1.3/tModLoader.Linux.v0.10.1.3.zip
&& \  
unzip terraria-server-1352.zip -d /server && \  
rm terraria-server-1352.zip && \  
rm -rf /server/Mac && \  
rm -rf /server/Windows && \  
mv /server/Linux/* /server/ && \  
rm -rf /server/Linux && \  
unzip tModLoader.Linux.v0.10.1.3.zip -d /server && \  
rm /tModLoader.Linux.v0.10.1.3.zip && \  
apt-get remove -y zip \  
wget && \  
apt-get clean && \  
chmod +x /server/tModLoaderServer.bin.x86_64 && \  
mkdir -p /root/.local/share/Terraria/ModLoader  
  
VOLUME ["/root/.local/share/Terraria/ModLoader"]  
EXPOSE 7777  
  
CMD /server/tModLoaderServer.bin.x86_64  

