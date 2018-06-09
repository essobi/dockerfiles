FROM ubuntu:14.04  
ENV VERSION 3.0.11.4  
ENV URL http://dl.4players.de/ts/releases/${VERSION}/teamspeak3-server_linux-
amd64-${VERSION}.tar.gz  
  
RUN apt-get install -y curl && apt-get clean  
  
RUN mkdir -p /opt/teamspeak && \  
curl -Ss $URL -o /opt/teamspeak.tar.gz && \  
cd /opt/teamspeak && \  
tar --strip-components 1 -xf ../teamspeak.tar.gz  
  
ADD run.sh /run.sh  
  
EXPOSE 9987/udp  
EXPOSE 30033  
EXPOSE 10011  
VOLUME "/data"  
  
CMD ["/run.sh"]  

