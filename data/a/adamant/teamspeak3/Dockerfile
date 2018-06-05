#To Run: docker run --name ts-dev -p $IP:9987:9987/udp -p $IP:10011:10011 -p
$IP:30033:30033 -v **TS DATA LOCATION**:/data ts-dev  
FROM frolvlad/alpine-glibc  
MAINTAINER Adam Dodman <adam.dodman@gmx.com>  
  
ENV VERSION 3.0.13.6  
ENV DOWNLOADURL
http://dl.4players.de/ts/releases/${VERSION}/teamspeak3-server_linux_amd64-${VERSION}.tar.bz2  
  
ENV LD_LIBRARY_PATH /teamspeak  
  
# Download and configure teamspeak  
RUN mkdir /teamspeak \  
&& wget $DOWNLOADURL -O /tmp/teamspeak.tar.bz2 \  
&& tar jxf /tmp/teamspeak.tar.bz2 -C /teamspeak \  
&& mv /teamspeak/teamspeak3-server*/* /teamspeak \  
&& ls -lah /teamspeak/teamspeak3-server* \  
&& rmdir /teamspeak/teamspeak3-server* \  
&& rm /tmp/teamspeak.tar.bz2  
  
# Add custom files  
COPY start /  
  
#CHMOD start  
RUN chmod +x /start  
  
# Ports  
EXPOSE 9987/udp  
EXPOSE 10011  
EXPOSE 30033  
# Start command  
CMD ["/start"]  

