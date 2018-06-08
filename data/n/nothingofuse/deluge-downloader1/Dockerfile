FROM ubuntu:latest  
MAINTAINER nothingofuse <mattmontmorency@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install python2.7 git -y  
RUN apt-get install openvpn deluge deluged deluge-console cifs-utils unzip -y  
RUN apt-get install nano curl wget sudo git net-tools vim openssh-server -y  
RUN git clone https://github.com/deluge-downloader  
RUN python /deluge-downloader/deluge.py  
CMD deluged  
EXPOSE 58846  

