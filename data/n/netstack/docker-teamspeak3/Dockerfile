FROM ubuntu:16.04  
MAINTAINER Andreas Pfeiffer <pfeiffer@netstack.de>  
  
#Set Locales  
#RUN locale-gen de_DE.UTF-8  
#RUN locale-gen en_US.UTF-8  
#Environment Variables  
ENV TEAMSPEAK_DOWNLOAD_URL
http://dl.4players.de/ts/releases/3.0.13/teamspeak3-server_linux_amd64-3.0.13.tar.bz2  
ENV TS3_UID 2000  
ENV LANG de_DE.UTF-8  
ENV LC_ALL de_DE.UTF-8  
#Update System  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get upgrade -y  
  
#Install software  
RUN apt-get install -y wget bzip2  
  
RUN useradd -m -u ${TS3_UID} ts3  
COPY ts3_install_start.sh /home/ts3/  
RUN chown -Rf ts3.ts3 /home/ts3/  
RUN chmod +x /home/ts3/ts3_install_start.sh  
  
USER ts3  
  
CMD /home/ts3/ts3_install_start.sh  
  
#EXPOSE TS3 PORTS  
EXPOSE 9987/udp 30033 10011  

