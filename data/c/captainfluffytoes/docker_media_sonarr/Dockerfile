FROM debian:stable-slim  
  
RUN apt-get update -y &&\  
apt-get install apt-transport-https gnupg2 -y &&\  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys FDA5DFFC &&\  
echo "deb http://apt.sonarr.tv/ master main" >
/etc/apt/sources.list.d/sonarr.list &&\  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF &&\  
echo "deb http://download.mono-project.com/repo/debian stretch main" >
/etc/apt/sources.list.d/mono-official.list &&\  
apt-get update -y &&\  
apt-get upgrade -y &&\  
apt-get install mono-complete nzbdrone -y &&\  
apt-get clean &&\  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
VOLUME /TV /completed /download  
  
WORKDIR /opt/NzbDrone  
  
EXPOSE 8989  
  
CMD ["mono","--debug","NzbDrone.exe"]

