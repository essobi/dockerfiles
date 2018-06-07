FROM debian:jessie  
MAINTAINER Andreas Fahrecker<fahrecker.a@gmail.com>  
  
ENV TSV 3.0.13.8  
ENV TSPATH /opt/teamspeak  
ENV TSUSER teamspeak  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y update && \  
apt-get -y install bzip2 && \  
apt-get -y autoremove && \  
apt-get -y clean  
  
ADD
http://dl.4players.de/ts/releases/3.0.13.8/teamspeak3-server_linux_amd64-${TSV}.tar.bz2
./  
  
RUN tar -jxf teamspeak3-server_linux_amd64-$TSV.tar.bz2 && \  
mv teamspeak3-server_linux_amd64 $TSPATH && \  
rm teamspeak3-server_linux_amd64-$TSV.tar.bz2  
  
ADD ./run.sh /run.sh  
  
RUN chmod +x /run.sh  
  
EXPOSE 9987/udp  
EXPOSE 30033  
EXPOSE 10011  
RUN useradd $TSUSER && mkdir /data && chown $TSUSER:$TSUSER /data  
VOLUME ["/data"]  
USER $TSUSER  
CMD ./run.sh

