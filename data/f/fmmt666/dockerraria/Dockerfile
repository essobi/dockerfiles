FROM debian  
  
MAINTAINER FMMT666 <fmmt666@users.noreply.github.com>  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install cowsay fortune joe mc wget && \  
echo "alias d='ls -la --color'" >> /root/.bashrc && \  
wget -O tserver.zip "http://terraria.org/server/terraria-server-1353.zip" && \  
unzip tserver.zip && \  
rm tserver.zip && \  
chmod +x '/1353/Linux/TerrariaServer.bin.x86_64' && \  
rm -rf /1353/Mac && \  
rm -rf /1353/Windows  
  
VOLUME /terraria  
  
COPY runthis.sh /  
COPY serverconfig.txt /  
  
ENTRYPOINT ["/runthis.sh"]  

