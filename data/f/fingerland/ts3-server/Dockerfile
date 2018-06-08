FROM ubuntu  
MAINTAINER Caderrik <caderrik@gmail.com>  
  
ENV VERSION=3.0.13.5  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y update && \  
apt-get -y install bzip2  
  
RUN useradd -r -m -u 1000 teamspeak  
ADD ./scripts/run-server.sh /home/teamspeak/run-server  
ADD
http://teamspeak.gameserver.gamed.de/ts3/releases/${VERSION}/teamspeak3-server_linux_amd64-${VERSION}.tar.bz2
teamspeak3-server.tar.bz2  
RUN tar -jxf teamspeak3-server.tar.bz2 && \  
mv teamspeak3-server_linux_amd64 /home/teamspeak/server && \  
rm -f teamspeak3-server.tar.bz2 && \  
chmod +x /home/teamspeak/run-server && \  
mkdir /home/teamspeak/data && \  
chown -R teamspeak: /home/teamspeak  
  
USER teamspeak  
WORKDIR "/home/teamspeak"  
VOLUME ["/home/teamspeak/data"]  
EXPOSE 9987/udp 30033 10011  
CMD ["/home/teamspeak/run-server"]

