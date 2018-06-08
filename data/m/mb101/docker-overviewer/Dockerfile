FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get -y install \  
apt-transport-https \  
curl \  
python \  
sudo \  
wget  
  
RUN echo "deb https://overviewer.org/debian ./" >> /etc/apt/sources.list && \  
wget -O - https://overviewer.org/debian/overviewer.gpg.asc | sudo apt-key add
- && \  
apt-get update && \  
apt-get -y install minecraft-overviewer  
  
ADD ./overviewer/ /overviewer/  
  
VOLUME /overviewer/  
  
RUN chmod +x /overviewer/overviewer.sh  
  
CMD /overviewer/overviewer.sh  

